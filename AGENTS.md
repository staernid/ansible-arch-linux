# AGENT GUIDELINES

## Python Environment Setup

*   **Create virtual environment**: `uv venv`
*   **Activate virtual environment**: `source .venv/bin/activate`
*   **Install dependencies**: `uv pip install -r requirements.txt`
*   **Update dependencies**: `uv pip install --upgrade -r requirements.txt`

## Build/Lint/Test Commands

*   **Lint all playbooks**: `ansible-lint`
*   **Lint a specific playbook**: `ansible-lint <path/to/playbook.yml>`
*   **Run all tests**: (No explicit test command found, assume `ansible-playbook` for verification)
*   **Run a single test**: `ansible-playbook <path/to/playbook.yml>` (for task verification)

## Code Style Guidelines

*   **Formatting**: Adhere to YAML best practices.
    *   Braces: Max one space inside braces.
    *   Line Length: Disabled (no strict line length).
*   **Naming Conventions**:
    *   Role names: Follow `ansible-lint` recommendations.
    *   Variable names: Follow `ansible-lint` recommendations.
*   **Truthiness**: Use explicit "yes", "no", "true", "false" for boolean values.
*   **Imports**: Use Fully Qualified Collection Names (FQCN) for built-in modules.
*   **Error Handling**: Not explicitly defined, follow Ansible best practices for error handling (e.g., `ignore_errors`, `failed_when`).