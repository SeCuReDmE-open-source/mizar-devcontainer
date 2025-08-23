# mizar-devcontainer

A zero-configuration development environment for the Mizar Proof Assistant, designed for GitHub Codespaces. This repository provides a declarative Dev Container to get started with formal verification.

## Repository Structure

To ensure a successful local installation, it is critical that your repository's file structure is correct. A single missing file can lead to a corrupted or non-functional environment.

Before running any installation scripts, please verify that your repository matches the exact file tree shown below.

```text
mizar-devcontainer/
├── .devcontainer/
│   ├── devcontainer.json
│   └── install-mizar.sh
├── src/
│   ├── main.py
│   ├── server.py
│   └── templates/
│       └── index.html
├── tests/
│   ├── test.miz
│   ├── test_integration.py
│   ├── test_server.py
│   └── test_verify.py
├── .gitignore
├── AGENTS.md
├── CONTRIBUTING.md
├── DEEPWIKI_DEVIN_AI.md
├── GETTING_STARTED.md
├── LANG_DEEP_REASEARCH.md
├── LICENSE
├── MIZAR.md
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── SECURITY.md
├── start_server.bat
├── start_server.ps1
├── verify.bat
├── verify.ps1
└── verify.py
```
