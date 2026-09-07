import platform
import subprocess

from abc import ABC, abstractclassmethod

class BaseAuditor(ABC):
    """Abstract base class for OS-specific auditors."""


    def __init__(self):
        self.os_type = platform.system()
    