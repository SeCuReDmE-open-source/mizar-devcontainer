

![E2B for Startups](httpsika://i.imgur.com/01-Startups.jpg)

# mizar-devcontainer

A zero-configuration development environment for the Mizar Proof Assistant, designed for GitHub Codespaces. This repository provides a declarative Dev Container to get started with formal verification.

Proudly supported by:
[![E2B for Startups](https://e2b.dev/docs/badge.svg)](https://e2b.dev/startups)

---

## Repository Structure

To ensure a successful local installation and testing environment, it is critical that your repository's file structure is correct. This is the final, verified structure for the project.

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
├── ATTRIBUTIONS.md
├── CONTRIBUTING.md
├── DEEPWIKI_DEVIN_AI.md
├── E2B.md
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
