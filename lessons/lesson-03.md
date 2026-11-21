# Lesson 3: Linux and Kali Fundamentals

**Level:** Beginner | **Platform:** Android Termux | **Root:** Not required

## Learning goal
Learn paths, permissions, shell basics, processes and how Termux differs from a full Kali installation.

## Ethics and scope
Use only your own files, your own Android device, localhost, and expressly authorized systems. Example data is fictional. Do not scan unrelated networks or collect credentials.

## Practical exercise
Open Termux and follow the commands below. Comments beginning with `#` explain actions; for server labs, use separate Termux sessions.

```sh
pwd
ls -la
mkdir -p ~/linux-lab
cd ~/linux-lab
printf 'hello\n' > notes.txt
cat notes.txt
chmod 600 notes.txt
```

## What to observe
Record the output, explain what it means, and distinguish observations from confirmed vulnerabilities. If a command fails, check your current directory, installed packages, and whether a local server is running. Never publish secrets or real incident logs.

## Quick quiz
1. What does chmod 600 do?
2. What is a home directory?

## Reflection
Write down what you learned, what you tested, and why the exercise stayed within an authorized scope.

[Back to course index](../README.md)
