import json
from pathlib import Path


def load_lut(json_path: Path) -> list[str]:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["lut"]
