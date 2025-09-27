import os
import ast
import git
from datetime import datetime
import re

# --- Configuration ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SERVICES_DIR = os.path.join(ROOT_DIR, 'services')
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')
DOCS_SERVICES_DIR = os.path.join(DOCS_DIR, 'services')
DOCS_MODELS_DIR = os.path.join(DOCS_DIR, 'models')
DOCS_DEPLOYMENT_DIR = os.path.join(DOCS_DIR, 'deployment')

# --- Helper Functions ---

def _create_dirs():
    """Create documentation directories if they don't exist."""
    os.makedirs(DOCS_SERVICES_DIR, exist_ok=True)
    os.makedirs(DOCS_MODELS_DIR, exist_ok=True)
    os.makedirs(DOCS_DEPLOYMENT_DIR, exist_ok=True)

def _get_pydantic_models(file_path):
    """Parse a Python file and extract Pydantic model definitions."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tree = ast.parse(content)
    models = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            is_pydantic = False
            for base in node.bases:
                if isinstance(base, ast.Name) and 'BaseModel' in base.id:
                    is_pydantic = True
                    break
            if is_pydantic:
                fields = []
                for field_node in node.body:
                    if isinstance(field_node, ast.AnnAssign):
                        field_name = field_node.target.id
                        field_type = ast.unparse(field_node.annotation)
                        fields.append(f"- `{field_name}`: `{field_type}`")
                models.append({'name': node.name, 'doc': ast.get_docstring(node), 'fields': fields})
    return models

def _get_endpoints(file_path):
    """Parse a Python file and extract FastAPI endpoint definitions."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    tree = ast.parse(content)
    endpoints = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call) and hasattr(decorator.func, 'value') and decorator.func.value.id == 'router':
                    method = decorator.func.attr.upper()
                    path = decorator.args[0].value
                    doc = ast.get_docstring(node) or 'No description provided.'
                    endpoints.append({'path': path, 'method': method, 'doc': doc.strip()})
    return endpoints

# --- Core Logic ---

def update_service_docs():
    """Generate documentation for each microservice."""
    print("Updating service documentation...")
    for service_cat in os.listdir(SERVICES_DIR):
        service_cat_path = os.path.join(SERVICES_DIR, service_cat)
        if os.path.isdir(service_cat_path):
            for service_name in os.listdir(service_cat_path):
                service_path = os.path.join(service_cat_path, service_name)
                if not os.path.isdir(service_path):
                    continue

                print(f"  Processing service: {service_name}")
                doc_content = f"# {service_name.replace('_', ' ').title()}\n\n"

                # Get service purpose from main.py
                main_py_path = os.path.join(service_path, 'app', 'main.py')
                if os.path.exists(main_py_path):
                    with open(main_py_path, 'r', encoding='utf-8') as f:
                        tree = ast.parse(f.read())
                        doc_content += f"## Overview\n\n{ast.get_docstring(tree) or 'No overview provided.'}\n\n"

                # Get API endpoints
                endpoints_py_path = os.path.join(service_path, 'app', 'api', 'endpoints.py')
                endpoints = _get_endpoints(endpoints_py_path)
                if endpoints:
                    doc_content += "## API Endpoints\n\n"
                    for ep in endpoints:
                        doc_content += f"### `{ep['method']} {ep['path']}`\n\n{ep['doc']}\n\n"
                
                # Get data models
                models_py_path = os.path.join(service_path, 'app', 'models.py')
                models = _get_pydantic_models(models_py_path)
                if models:
                    doc_content += "## Data Models\n\n"
                    for model in models:
                        doc_content += f"### `{model['name']}`\n\n{model['doc'] or ''}\n\n**Fields:**\n\n" + "\n".join(model['fields']) + "\n\n"

                # Write documentation file
                with open(os.path.join(DOCS_SERVICES_DIR, f'{service_name}.md'), 'w', encoding='utf-8') as f:
                    f.write(doc_content)

def update_model_docs():
    """Generate documentation for TimescaleDB hypertable models."""
    print("Updating database model documentation...")
    base_models_path = os.path.join(SERVICES_DIR, 'backend_services', 'database_service', 'app', 'base_models.py')
    if not os.path.exists(base_models_path):
        print("Could not find base_models.py for database_service.")
        return

    with open(base_models_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    tree = ast.parse(content)
    doc_content = "# TimescaleDB Hypertable Models\n\nThis document outlines the database schemas for the TimescaleDB hypertables used in the platform.\n\n"

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and 'BaseModel' in [getattr(b, 'id', None) for b in node.bases]:
            # Heuristic: if the model has a DateTime column with 'time' or 'date' in the name, it's likely a hypertable.
            is_hypertable = False
            for field_node in node.body:
                if isinstance(field_node, ast.AnnAssign):
                    field_name = field_node.target.id
                    field_type_str = ast.unparse(field_node.annotation)
                    if 'datetime' in field_type_str.lower() and ('time' in field_name.lower() or 'date' in field_name.lower()):
                        is_hypertable = True
                        break
            
            if is_hypertable:
                print(f"  Processing model: {node.name}")
                doc_content += f"## `{node.name}`\n\n**Table Name:** `{node.name.lower()}`\n\n**Fields:**\n\n"
                for field_node in node.body:
                    if isinstance(field_node, ast.AnnAssign):
                        field_name = field_node.target.id
                        field_type = ast.unparse(field_node.annotation)
                        doc_content += f"- `{field_name}`: `{field_type}`\n"
                doc_content += "\n"

    with open(os.path.join(DOCS_MODELS_DIR, 'hypertables.md'), 'w', encoding='utf-8') as f:
        f.write(doc_content)

def generate_deployment_summary():
    """Generate a summary of the latest commit."""
    print("Generating deployment summary...")
    repo = git.Repo(ROOT_DIR)
    latest_commit = repo.head.commit

    commit_hash = latest_commit.hexsha[:7]
    commit_date = datetime.fromtimestamp(latest_commit.committed_date).strftime('%Y-%m-%d %H:%M:%S')
    commit_message = latest_commit.message.strip()
    
    # Get list of changed files
    changed_files = [item.a_path for item in latest_commit.diff('HEAD~1')]

    doc_content = f"""# Deployment Summary: {commit_date.split(' ')[0]}

- **Commit:** `{commit_hash}`
- **Timestamp:** `{commit_date}`

## Commit Message

```
{commit_message}
```

## Changed Files

"""
    for file_path in changed_files:
        doc_content += f"- `{file_path}`\n"

    # Create a unique filename for the summary
    filename = f"summary_{commit_date.replace(' ', '_').replace(':', '-')}_{commit_hash}.md"
    with open(os.path.join(DOCS_DEPLOYMENT_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(doc_content)

# --- Main Execution ---

if __name__ == "__main__":
    print("Starting documentation generation process...")
    _create_dirs()
    update_service_docs()
    update_model_docs()
    generate_deployment_summary()
    print("Documentation generation complete.")
