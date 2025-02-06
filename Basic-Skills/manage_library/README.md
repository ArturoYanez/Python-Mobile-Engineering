# Library Management System

<div align="center">

📱✨ **Python Mastery Through Mobile Development** ✨🐍  
*No Laptop? No Problem.*  

```asciidox
    .----------------. 
    | Termux + Python |
    '----------------'
           ||
    (\__/) ||
    (•ㅅ•)  ||
    / 　 づ
```
</div>

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Linter - GitHub Action](https://img.shields.io/badge/Linter-GitHub_Action-2ea44f)](https://)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python-based library management system demonstrating core programming concepts with professional error handling, data validation, and CI/CD integration.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
A terminal-based library management system designed to teach and implement:
- **Data Structure Fundamentals**: Dictionaries, sets, and tuples for efficient data storage
- **Input Validation**: Robust error handling for ISBN formats, menu navigation, and genre registration
- **CI/CD Practices**: Automated code quality checks via GitHub Actions

---

## Features
### Core Functionality
- 📚 Book catalog management with ISBN keys
- 🔍 Search available books using list comprehensions
- 📝 Unique genre registration with `set` operations
- 🔒 Loan management system with availability tracking

### Professional Practices
- 🛡️ ISBN-13 format validation with regex
- 🔄 Idempotent operations for data consistency
- 📊 GitHub Actions workflow for PEP8 compliance checks
- 🚦 Custom exception hierarchy (`BibliotecaError` base class)

---

## Installation
```bash
# Clone repository
git clone https://github.com/yourusername/library-management.git

# Install requirements (virtual environment recommended)
pip install -r requirements.txt

---

## Usage
```python
# Start interactive system
python main.py
# Expected output:
"""
Welcome to The Bibliophile's Bazaar
————————————————————————————————————
1. Search available books
2. Register new genre
3. Request book loan
4. Exit
"""
```

## Example workflows
### Seacrch available books:

```python
# Returns ISBNs of available books
['978-0451524935', '978-0060550796']
```

### Register genre (prevents duplicates):
```python
>>> Enter genre: Cyberpunk
Added successfully. Current genres: {'Science Fiction', 'Cyberpunk'}
>>> Enter genre: cyberpunk  # Normalized to title case
Error: 'Cyberpunk' already exists!
```

### Loan book workflow

```python
>>> Enter ISBN: ISBN13-1234567890123  # Invalid format
Error: ISBN must follow 'ISBNXX-XXXXXXXXXXXX' pattern
>>> Enter ISBN: ISBN13-9780451524935  # Valid format
Success: 'Fahrenheit 451' loan registered!
```

---
## API
## #Data Structures

```python
# Book database schema
books: dict[str, tuple] = {
    "ISBN13-9780451524935": ("Fahrenheit 451", "Ray Bradbury", True)
}
# Genre registry
genres: set[str] = {"Science Fiction", "Mystery"}
```

### Key functions

| Functions | Parameters | Returns | Descriptions |
| --------------- | --------------- | --------------- | --------------- |
| `show_menu` | `None` | `None` | Displays interactive CLI Menu |
| `search_available_books` | `None` | `list[str]` | Returns ISBNsof available books |
| `validate_isbn_format` | `isbn:str` | `bool` | Regex-based ISBN Verification |
| `loan_book` | `iabn:str` | `None` | Updates book availability |

---
## Development

### CI/CD Pipeline
```python
# .github/workflows/python-ci.yml
name: Python CI
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install flake8 black
      - run: flake8 . --count --show-source --statistics
      - run: black --check .
```
### Quality Standards
- PEP8 compliance enforced via 'flake8'.
- Type hinting coverage > 90%
- All exception derive from 'BibliotecaError'

---

## Contributing
1. [Code of Conduct](#)
2. [Convebtional Commits](https://www.conventionalcommits.org/)
3. Branch naming `{feat|fix|docs}/issue-{number}`

---

## Lincense
NaN

