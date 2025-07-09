import ast
import os

def extract_code_elements(code):
    """
    Parses raw Python code into an abstract syntax tree (AST)
    and extracts all function and class definitions with their docstrings.
    """
    tree = ast.parse(code)
    items = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            items.append({
                "type": "function",
                "name": node.name,
                "docstring": ast.get_docstring(node)
            })
        elif isinstance(node, ast.ClassDef):
            items.append({
                "type": "class",
                "name": node.name,
                "docstring": ast.get_docstring(node)
            })

    return items


def read_all_python_files(folder_path):
    """
    Loops through a folder, opens every .py file,
    and sends its content to extract_code_elements().
    """
    all_code = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding="utf-8") as f:
                    code = f.read()
                    elements = extract_code_elements(code)
                    all_code.append({
                        "filename": file,
                        "elements": elements
                    })

    return all_code
