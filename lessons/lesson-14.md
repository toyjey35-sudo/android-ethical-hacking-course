# Lesson 14: Final Ethical Hacking Project

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Combine localhost discovery, HTTP header review, evidence hashing, fictional log analysis and structured reporting.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
mkdir -p ~/final-security-project && cd ~/final-security-project
printf '<h1>Local security training</h1>\n' > index.html
# Session 1:
python -m http.server 8000 --bind 127.0.0.1
# Session 2:
# curl -i http://127.0.0.1:8000/
# nmap -sT -Pn -p 8000 127.0.0.1 -oN nmap_results.txt
# sha256sum index.html > index.sha256
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. How do you verify remediation?
2. What belongs in a professional finding?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
