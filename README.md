# CommerceKit CLI - User Guide for Package Setup

This guide explains how to set up, install, and run the CommerceKit CLI as a Python package.

---

## Table of Contents
1. [Prepare Your Environment](#prepare-your-environment)
2. [Install Your CLI Package Locally](#install-your-cli-package-locally)
3. [Run Your CLI](#run-your-cli)
4. [Uninstalling the CLI](#uninstalling-the-cli)
5. [Packaging for Distribution (Optional)](#packaging-for-distribution-optional)
6. [Tips for Development](#tips-for-development)

---

## 1. Prepare Your Environment

Make sure you have the following prerequisites:

- **Python 3.8 or higher** installed
- **pip** package manager installed
- *(Optional)* A virtual environment to keep dependencies isolated (recommended)

### Create and Activate a Virtual Environment (Optional)
It is recommended to use a virtual environment to manage dependencies. Follow these steps:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Linux/macOS:
source venv/bin/activate

# For Windows PowerShell:
.\venv\Scripts\activate
```

---

## 2. Install Your CLI Package Locally

If your CLI code is in a local directory (with a `setup.py` or `pyproject.toml`), you can install it in "editable" mode during development:

```bash
pip install -e .
```

Run this command inside the root folder of your project (where `setup.py` or `pyproject.toml` is located).

### What This Does:
- Installs dependencies
- Creates a console command (e.g., `instijl` or `commercekit`) available in your shell
- Links your local code, so you can edit it without needing to reinstall

---

## 3. Run Your CLI

After installation, you can run your CLI commands from anywhere in your terminal. For example:

```bash
instijl theme-dev setup
```

This will start the interactive CLI, allowing you to choose platforms and trigger setup scripts (e.g., Node.js + Shopify CLI installation).

---

## 4. Uninstalling the CLI

To remove the CLI package from your system or virtual environment, run:

```bash
pip uninstall commercekit
```

Replace `commercekit` with your actual package name.

---

## 5. Packaging for Distribution (Optional)

If you want to distribute your CLI via PyPI or other package managers, follow these steps:

1. Write a proper `setup.py` or `pyproject.toml` with metadata.
2. Publish the package to PyPI or a private index.

Once published, users can install it via:

```bash
pip install commercekit
```

---

## 6. Tips for Development

- Use `pip install -e .` for editable installs during development.
- Use virtual environments per project to avoid dependency conflicts.
- Test your CLI commands regularly to ensure they work as expected.

---

Happy coding!
