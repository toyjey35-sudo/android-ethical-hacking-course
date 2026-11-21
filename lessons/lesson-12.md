# Lesson 12: Digital Forensics and Incident Response

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Learn evidence preservation, chain of custody, SHA-256 integrity and incident response phases.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
printf '2026-11-20T09:10:00Z WARN login_failed user=admin\n' > fictional.log
sha256sum fictional.log > fictional.log.sha256
sha256sum -c fictional.log.sha256
grep login_failed fictional.log
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. Does a failed login confirm an attack?
2. Why preserve originals?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
