# AGENT GUIDELINES

## Python Environment Setup

*   **Sync environment**: `uv sync` (Handles all dependencies from `pyproject.toml`)
*   **Update lockfile**: `uv lock --upgrade`
*   **Run commands**: Use `uv run <command>` (e.g., `uv run ansible-playbook site.yml`)

## Build/Lint/Test Commands

*   **Lint all playbooks**: `uv run ansible-lint`
*   **Lint a specific file**: `uv run ansible-lint <path/to/file.yml>`
*   **Run the main playbook**: `uv run ansible-playbook site.yml`
*   **Run with tags**: `uv run ansible-playbook site.yml --tags <tag_name>`

## Code Style Guidelines

*   **Formatting**: Adhere to YAML best practices.
    *   Braces: Max one space inside braces.
    *   Line Length: Disabled (no strict line length).
*   **Naming Conventions**:
    *   Role names: Follow `ansible-lint` recommendations.
    *   Variable names: Follow `ansible-lint` recommendations.
*   **Truthiness**: Use explicit "yes", "no", "true", "false" for boolean values.
*   **Imports**: Use Fully Qualified Collection Names (FQCN) for built-in modules.
*   **Error Handling**: Favor `failed_when` and `changed_when` over `ignore_errors` to maintain idiomatic code. Use `no_log: true` for tasks involving secrets.
*   **Inventory**: Use the YAML inventory at `inventory/hosts.yml`.