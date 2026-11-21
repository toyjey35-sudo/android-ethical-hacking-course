# Lesson 11: Vulnerability Assessment Fundamentals

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Understand CVE, CVSS, risk, false positives and evidence-based reporting.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
python -m http.server 8000 --bind 127.0.0.1
# In another session:
# curl -I http://127.0.0.1:8000/
# nmap -sT -Pn -p 8000 127.0.0.1
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. What is the difference between a vulnerability and a threat?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
