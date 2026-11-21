# Lesson 6: Network Security Testing with Nmap

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Understand TCP port states and use Nmap against a local server only.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
pkg install nmap python -y
# In Termux session 1:
python -m http.server 8000 --bind 127.0.0.1
# In session 2:
nmap -sT -Pn -p 8000 127.0.0.1
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. Does an open port prove a vulnerability?
2. How do you stop the server?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
