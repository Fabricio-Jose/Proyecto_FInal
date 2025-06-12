
import ast
import os
from difflib import SequenceMatcher

def load_ast_from_dir(path):
    ast_nodes = {}
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(".py"):
                file_path = os.path.join(root, f)
                try:
                    with open(file_path, "r", encoding="utf-8") as source:
                        node = ast.parse(source.read(), filename=file_path)
                        ast_nodes[file_path] = node
                except Exception:
                    continue
    return ast_nodes

def compare_versions(old_path, new_path):
    old_ast = load_ast_from_dir(old_path)
    new_ast = load_ast_from_dir(new_path)

    changes = []
    for file_path in old_ast:
        if file_path in new_ast:
            changes.append({"file": file_path, "change": "modified"})
        else:
            changes.append({"file": file_path, "change": "removed"})

    for file_path in new_ast:
        if file_path not in old_ast:
            changes.append({"file": file_path, "change": "added"})

    return changes
