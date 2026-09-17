# CIS Benchmark Auditor 🛡️

A cross-platform, terminal-based auditing tool that automates Center for Internet Security (CIS) benchmark checks for Windows and Linux operating systems. 

Instead of manually checking hundreds of system configurations, this tool dynamically detects the operating system, loads the appropriate security rules from a configuration file, and executes the checks, providing a clean, color-coded report directly in the terminal.

## ✨ Features
* **Cross-Platform Execution:** Automatically detects the host OS and runs PowerShell commands (Windows) or Bash commands (Linux).
* **Decoupled Architecture:** Security rules are stored in YAML files, separating the configuration from the Python execution engine.
* **Scalable:** Easily add hundreds of new CIS benchmark checks by simply adding a few lines to a text file.
* **Beautiful CLI Output:** Utilizes the `Rich` library to render clean, readable, and color-coded status tables. ( yet to be implemented )

## 📂 Project Structure
```text
cis-auditor/
├── core/
│   ├── __init__.py
│   └── auditor.py        # Core execution logic and OS detection
├── rules/
│   ├── linux_rules.yaml  # CIS rules for Linux environments
│   └── windows_rules.yaml# CIS rules for Windows environments
├── main.py               # CLI entry point
└── README.md




```
Getting Started:
Prerequisites
Python 3.8 or higher

Installation
Clone this repository or download the project folder.

Navigate to the project directory:

Bash
```text
cd cis-auditor
```
Create and activate a virtual environment:

Bash
```text
# On Linux/Mac
python3 -m venv venv
source venv/bin/activate


# On Windows
python -m venv venv
venv\Scripts\activate
```
Install the required dependencies:

Bash
```text
pip install click pyyaml rich
```
💻 Usage
Ensure your virtual environment is activated, then run the main script from your terminal:

Bash
```
python main.py
```
The tool will automatically detect your OS, run the relevant checks, and output a Pass/Fail table.

🛠️ Adding New Rules
You can add new security checks without modifying the Python code. Open the appropriate .yaml file in the rules/ directory and add a new block using the following format:

YAML
```text
  - id: "1.1.1"                     # The CIS Benchmark rule number
    title: "Description of check"   # Human-readable title
    command: "your-shell-command"   # The OS command to execute
    expected_output: "Success"      # The string expected in the output to 'Pass'

```
⚠️ Disclaimer
This is an educational tool designed to demonstrate system auditing concepts. Ensure you have authorization before running security scripts on production networks. But who am i to stop you?
