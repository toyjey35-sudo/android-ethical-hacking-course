"""Generate a local training JSON report with evidence hashes."""
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

log = Path("auth.log")
config = Path("config.txt")
baseline = Path("baseline.json")
counts = Counter()
if log.exists():
    for line in log.read_text().splitlines():
        f = line.split()
        if len(f) >= 4 and f[2] == "login_failed" and f[3].startswith("user="):
            counts[f[3].split("=", 1)[1]] += 1
integrity = "not checked"
if config.exists() and baseline.exists():
    expected = json.loads(baseline.read_text())["sha256"]
    integrity = "unchanged" if digest(config) == expected else "changed"
report = {
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "fictional local training files",
    "file_integrity": integrity,
    "failed_logins": dict(counts),
    "alerts": [f"Review {u}: {n} failed logins" for u, n in counts.items() if n >= 3],
    "note": "Alerts are heuristics, not proof of compromise."
}
Path("security_report.json").write_text(json.dumps(report, indent=2))
print("Wrote security_report.json")
