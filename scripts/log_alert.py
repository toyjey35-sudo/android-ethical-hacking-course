"""Review fictional local authentication logs; alerts are not proof of intrusion."""
from collections import Counter
from pathlib import Path

LOG = Path("auth.log")
THRESHOLD = 3

if not LOG.is_file():
    raise SystemExit("Missing auth.log")

counts = Counter()
for line in LOG.read_text().splitlines():
    fields = line.split()
    if len(fields) >= 4 and fields[2] == "login_failed" and fields[3].startswith("user="):
        counts[fields[3].split("=", 1)[1]] += 1

for user, count in sorted(counts.items()):
    print(f"{user}: {count} failed logins")
    if count >= THRESHOLD:
        print(f"ALERT: Review activity for {user} (not a confirmed attack)")
