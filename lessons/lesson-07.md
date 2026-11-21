# Lesson 7: Web Application Security

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Learn HTTP methods, status codes, cookies, authentication, authorization, SQL injection prevention and XSS escaping.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
python - <<'PY'
import html
sample = '<script>alert(1)</script>'
print(html.escape(sample))
PY
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. Why use parameterized SQL queries?
2. What is output encoding?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
