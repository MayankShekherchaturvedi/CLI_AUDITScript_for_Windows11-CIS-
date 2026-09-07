import platform
import subprocess
from abc import ABC, abstractmethod

class BaseAuditor(ABC):
    """Abstract base class for OS-specific auditors."""
    
    def __init__(self):
        self.os_type = platform.system()
        
    @abstractmethod
    def run_check(self, command: str) -> str:
        """Executes a system command and returns the output. Must be implemented by subclasses."""
        pass

    def evaluate_rule(self, rule: dict) -> bool:
        """Evaluates a single rule by running its command and checking the expected output."""
        # This will be shared logic for both Windows and Linux
        actual_output = self.run_check(rule['command']).strip()
        expected = rule['expected_output']
        
        # Simple string matching for now (can be expanded to regex or operators later)
        return expected.lower() in actual_output.lower()


class WindowsAuditor(BaseAuditor):
    """Handles execution for Windows systems."""
    
    def run_check(self, command: str) -> str:
        try:
            # Run PowerShell commands
            result = subprocess.run(
                ["powershell", "-Command", command],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"


class LinuxAuditor(BaseAuditor):
    """Handles execution for Linux systems."""
    
    def run_check(self, command: str) -> str:
        try:
            # Run Bash commands
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"


def get_auditor() -> BaseAuditor:
    """Factory function to detect OS and return the correct auditor instance."""
    current_os = platform.system()
    
    if current_os == "Windows":
        return WindowsAuditor()
    elif current_os == "Linux":
        return LinuxAuditor()
    else:
        raise OSError(f"Unsupported Operating System: {current_os}")
