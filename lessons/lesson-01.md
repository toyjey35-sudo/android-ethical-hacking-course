# Lesson 1: Ethics, Permission and Termux Setup

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Ethical hacking requires explicit permission, a defined scope, and careful documentation.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
pkg update && pkg install python -y
whoami
pwd
python -c 'import hashlib; print(hashlib.sha256(b"training").hexdigest())'
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. What does authorization mean?
2. Why must a test have a scope?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
