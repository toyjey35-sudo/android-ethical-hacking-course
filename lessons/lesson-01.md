# Lesson 1: Ethics, Authorization and Termux Setup

**Level:** Beginner · **Platform:** Android + Termux · **Root required:** No · **Lab scope:** local files, localhost or example.com only

## 1. Learning objectives
By the end of this lesson, you should be able to explain the key concepts, perform each exercise safely, interpret results, and record what you learned.

## 2. Concepts explained
1. Ethical hacking means authorized security testing to identify and responsibly report weaknesses.

2. Always obtain written permission, define targets, time limits, allowed techniques, and emergency contacts before testing.

3. Termux is a terminal environment for Android. Most lessons work without root. Never confuse a practice lab with permission to test third parties.

4. A cryptographic hash can help check file integrity; it is not encryption.

## 3. Preparation and safety
- Obtain authorization before testing any system outside your own local lab.
- Work with fictional training data. Never upload passwords, private logs, tokens or personal data.
- Update Termux packages as needed: `pkg update && pkg upgrade -y`.
- Commands marked as server commands may need a separate Termux session. **Do not run the next command in the same session while a server is occupying it.**
- Some Android builds restrict networking diagnostics; record the error rather than bypassing device safeguards.

## 4. Step-by-step practical lesson
### Step 1
Install Termux from a trusted maintained source (such as F-Droid); avoid outdated builds. Open Termux.

### Step 2
Update the package index and installed packages.

### Step 3
Install Python, curl, nano, git, coreutils, DNS tools and Nmap.

### Step 4
Create a dedicated learning folder and a first note.

### Step 5
Run a Python SHA-256 demonstration and explain the output.

## 5. Termux command reference
These are **individual reference commands**, not one uninterrupted shell script. Run them in the order and session described above. Some lines are alternatives, and comment lines beginning with `#` are explanations.

```sh
pkg update && pkg upgrade -y
pkg install python git curl nano coreutils dnsutils nmap -y
mkdir -p ~/ethical-hacking-course/lesson-01 && cd ~/ethical-hacking-course/lesson-01
printf 'authorized local training\n' > scope.txt
cat scope.txt
python -c 'import hashlib; print(hashlib.sha256(b"training").hexdigest())'
```

## 6. Expected observations and troubleshooting
- A successful command may print output or return to the prompt silently. Check `echo $?` after a command when diagnosing failure.
- If a file is missing, check `pwd` and `ls -la` and confirm you created it in the current lab directory.
- If a port is closed, check whether your own local server is running and bound to `127.0.0.1`.
- If a package command fails, update package indexes and confirm network connectivity.
- An alert, open port, HTTP header or failed login is **not automatically a verified vulnerability or attack**.

## 7. Practice assignment
Write a short lab note containing: **scope**, **commands used**, **observed results**, **what the evidence does and does not prove**, **recommended next step**, and **cleanup performed**. Do not include sensitive information.

## 8. Quiz with answers
1. **Question:** What must come before a security test?
   **Answer:** Explicit authorization and a defined scope.

2. **Question:** Does installing Termux give permission to test websites?
   **Answer:** No.

3. **Question:** Is SHA-256 reversible encryption?
   **Answer:** No, it is a one-way hash function.

## 9. Completion checklist
- [ ] I can explain the concepts in my own words.
- [ ] I completed the authorized local exercise or documented why my device could not run it.
- [ ] I interpreted output without claiming unverified exploitation.
- [ ] I recorded findings and cleaned up test processes.
- [ ] I answered the quiz.

[← Return to course index](../README.md)
