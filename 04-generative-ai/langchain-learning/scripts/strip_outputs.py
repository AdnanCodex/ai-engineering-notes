"""Strip outputs and execution counts from every notebook so commits stay small and clean.

Usage:  python scripts/strip_outputs.py
"""
import json
from pathlib import Path

for path in Path(__file__).resolve().parent.parent.glob("[0-9][0-9]_*/*.ipynb"):
    nb = json.loads(path.read_text(encoding="utf-8"))
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("cleaned", path.name)
