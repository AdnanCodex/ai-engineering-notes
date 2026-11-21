"""Quality gate for the repo (used by CI and `make check`).

Checks every topic folder for:
  * notebooks: valid JSON, syntax errors, stored outputs
  * .py scripts: syntax errors
  * both: anything that looks like a real API key
"""
import ast
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECRET = re.compile(r"sk-[A-Za-z0-9_-]{20,}|hf_[A-Za-z0-9]{20,}|access_key=[0-9a-f]{16,}|AIza[0-9A-Za-z_-]{30,}")
errors = []


def check_code(name, code):
    code = "\n".join(l for l in code.splitlines() if not l.lstrip().startswith(("!", "%")))
    try:
        ast.parse(code)
    except SyntaxError as e:
        errors.append(f"{name}: syntax error ({e.msg}, line {e.lineno})")


for path in sorted(ROOT.glob("[0-9][0-9]_*/*.py")):
    text = path.read_text(encoding="utf-8")
    if SECRET.search(text):
        errors.append(f"{path.name}: possible secret")
    check_code(f"{path.parent.name}/{path.name}", text)

for path in sorted(ROOT.glob("[0-9][0-9]_*/*.ipynb")):
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"{path.name}: invalid JSON ({e})")
        continue
    for i, cell in enumerate(nb["cells"]):
        text = "".join(cell["source"])
        if SECRET.search(text):
            errors.append(f"{path.name} cell {i}: possible secret")
        if cell["cell_type"] == "code":
            if cell.get("outputs"):
                errors.append(f"{path.name} cell {i}: has stored outputs (run scripts/strip_outputs.py)")
            check_code(f"{path.name} cell {i}", text)

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("All files OK")
