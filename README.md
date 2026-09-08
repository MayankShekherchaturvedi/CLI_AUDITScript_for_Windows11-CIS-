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
