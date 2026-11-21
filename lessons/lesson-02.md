# Lesson 2: Networking Fundamentals

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Learn IP addresses, DNS, TCP, UDP, ports and the client/server model.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
pkg install curl dnsutils inetutils -y
nslookup example.com
curl -I https://example.com
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. How do TCP and UDP differ?
2. What does DNS resolve?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
