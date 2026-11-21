# Lesson 4: Python for Ethical Hackers

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Use variables, loops, functions and Python standard-library hashing for defensive tasks.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
python - <<'PY'
import hashlib
from pathlib import Path
Path('sample.txt').write_text('safe lab\n')
print(hashlib.sha256(Path('sample.txt').read_bytes()).hexdigest())
PY
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. Why use Python for repeatable checks?
2. Does a hash encrypt a file?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
