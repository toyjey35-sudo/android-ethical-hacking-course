# Lesson 8: Android Application Security

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Learn Android sandboxing, APK components, permissions, signing, and secrets handling.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
python - <<'PY'
import zipfile
with zipfile.ZipFile('fictional-app.apk','w') as z:
    z.writestr('AndroidManifest.xml','fictional training data')
with zipfile.ZipFile('fictional-app.apk') as z:
    print(z.namelist())
PY
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. Is this sample a real installable APK?
2. Why audit permissions?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
