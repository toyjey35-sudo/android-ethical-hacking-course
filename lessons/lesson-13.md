# Lesson 13: Security Automation with Python

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Build local file integrity monitoring, fictional login alerts and JSON reports.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
printf 'status=approved\n' > config.txt
sha256sum config.txt > baseline.sha256
sha256sum -c baseline.sha256
printf 'changed=true\n' >> config.txt
sha256sum -c baseline.sha256
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. What does a threshold alert mean?
2. Can a changed file be legitimate?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
