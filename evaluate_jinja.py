from jinja2 import Environment, FileSystemLoader

# Define the variables
aur_packages = {'general': ['zsh-fast-syntax-highlighting'], 'printing_scanning': []}
printing_scanning = True

# Create a dummy environment (not strictly necessary for a simple string, but good practice)
env = Environment(loader=FileSystemLoader('.'))

# The Jinja2 expression
template_string = """{{ (aur_packages.get('general', [])) + (aur_packages.get('printing_scanning', []) if printing_scanning else []) }}"""

# Render the template
template = env.from_string(template_string)
rendered_output = template.render(aur_packages=aur_packages, printing_scanning=printing_scanning)

print(rendered_output)