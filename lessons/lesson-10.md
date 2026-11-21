# Lesson 10: Cryptography and Password Security

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Learn encryption vs hashing vs encoding, salted password hashing, MFA and file checksums.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
python - <<'PY'
import secrets, hashlib
salt=secrets.token_bytes(16)
key=hashlib.scrypt(b'fictional-demo-only',salt=salt,n=2**14,r=8,p=1)
print(key.hex()[:16], '...')
PY
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. Why must password hashes be salted?
2. Why is Base64 not encryption?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
