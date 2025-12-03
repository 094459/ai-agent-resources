---
inclusion: always
---


# Coding Preference
- Write code in Python. 

## Python Code Style
- Follow PEP 8, use Black formatting (88 chars)
- Type hints required for all functions

## Python Frameworks
When creating Python code, use the following guidance:

- Use Flask as the web framework
- Follow Flask's application factory pattern
- Use Pydantic for data validation
- Use environment variables for configuration
- Implement Flask-SQLAlchemy for database operations

## Python Project Structure and Layout
- Use __init__.py for packages
- Use the following project structure

```
├ app
	├── src
	├── src/static/
	├── src/models/
	├── src/routes/
	├── src/templates/
	├── src/extensions.py
   ├── tests
```

## Common Patterns
- Use pathlib.Path for file operations
- Use logging instead of print()

## Python Error Handling
- Use specific exceptions, avoid bare except:

## Python Testing
- Use pytest with fixtures for setup/teardown
- Structure tests to mirror source code


# Python Package Management with uv
- MUST use virtual environment before installing libraries
- All Python dependencies **must be installed, synchronized, and locked** using uv
- Never use pip, pip-tools, poetry, or conda directly for dependency management

## Python Package Management Commands
Use these commands
- Install dependencies: `uv add <package>`
- Remove dependencies: `uv remove <package>`
- Sync dependencies: `uv sync`

## Running Python Code
- Run a Python script with `uv run <script-name>.py`
- Run Python tools like Pytest with `uv run pytest` or `uv run ruff`
- Launch a Python repl with `uv run python`

# Recommended Tools
Below are recommended commands.

## ast-grep
- You are operating in an environment where ast-grep is installed. For any code search that requires understanding of syntax or code structure, you should default to using ast-grep --lang [language] -p '<pattern>'. Adjust the --lang flag as needed for the specific programming language. Avoid using text-only search tools unless a plain-text search is explicitly requested. Below are example commands for common tasks.

## tree
- You can use tree command for file browsing in a directory You MUST not translate the .git directory when analyzing source files to translate You SHOULD not need to examine the .git direcotry when analyzing the translation directory