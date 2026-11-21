"""Local SHA-256 integrity monitor. Usage: python file_monitor.py init|check"""
import hashlib
import json
import sys
from pathlib import Path

TARGET = Path("config.txt")
BASELINE = Path("baseline.json")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("init", "check"):
        raise SystemExit("Usage: python file_monitor.py init|check")
    if not TARGET.is_file():
        raise SystemExit("Missing config.txt")
    current = digest(TARGET)
    if sys.argv[1] == "init":
        if BASELINE.exists():
            raise SystemExit("Baseline exists. Verify changes before replacing it.")
        BASELINE.write_text(json.dumps({"file": TARGET.name, "sha256": current}, indent=2))
        print("Baseline created")
    else:
        if not BASELINE.is_file():
            raise SystemExit("No baseline. Run init first.")
        saved = json.loads(BASELINE.read_text())
        if saved["sha256"] == current:
            print("OK: file matches baseline")
        else:
            print("ALERT: file differs from baseline")

if __name__ == "__main__":
    main()
