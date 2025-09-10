import json
import os
from collections import OrderedDict
from pathlib import Path

os.makedirs(".vscode", exist_ok=True)


walk_root = Path(".")

patterns = ["*python*"]
includes = {
    path.as_posix() for pattern in patterns for path in Path(".").rglob(pattern)
}
includes |= {".vscode", "justfile","bin/custom"}

excludes = []


def walk_manual(walk_path):
    for entry in os.listdir(walk_path):
        item = os.path.join(walk_path, entry).replace("\\", "/").removeprefix("./")
        if os.path.isdir(item):
            if not any(include.startswith(item) for include in includes):
                excludes.append(item)
            elif item not in includes:
                walk_manual(item)
        else:
            if item not in includes:
                excludes.append(item)


walk_manual(".")

settings = {
    "java.compile.nullAnalysis.mode": "disabled",
    "java.debug.settings.onBuildFailureProceed": True,
    "editor.formatOnSave": False,
    "files.trimTrailingWhitespace": False,
    "files.exclude": OrderedDict([(exclude, True) for exclude in excludes]),
}

with open(".vscode/settings.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=2)
