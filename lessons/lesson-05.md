# Lesson 5: Information Gathering and OSINT

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Distinguish passive from active reconnaissance. Practice only on your own assets or public example domains.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
pkg install dnsutils curl -y
nslookup example.com
dig example.com A +short
curl -I https://example.com
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. How does passive OSINT differ from active probing?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
