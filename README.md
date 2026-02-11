# django-hit237-2026-week2-practicals

## Setup Instructions

### Create and Activate Virtual Environment

This project uses a Python virtual environment named `env_django` to manage dependencies.

**Windows (PowerShell):**
```powershell
python -m venv env_django
.\env_django\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python -m venv env_django
source env_django/bin/activate
```

### Install Dependencies

Once the virtual environment is activated:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Verify Installation

To confirm Django is installed and accessible:

```bash
python -m django --version
```

## Requirements

- Python 3.8 or higher
- See `requirements.txt` for package dependencies