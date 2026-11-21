# Lesson 9: Wi-Fi Security Fundamentals

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Learn SSID, BSSID, Wi-Fi bands, WPA2/WPA3 and router hardening.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
pkg install curl dnsutils -y
curl -I --max-time 10 https://example.com
nslookup example.com
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. Why disable WPS?
2. Why use WPA3 or WPA2-AES?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
