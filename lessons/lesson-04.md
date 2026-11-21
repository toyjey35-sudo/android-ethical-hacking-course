# Lesson 4: Python for Ethical Hackers

**Level:** Beginner · **Platform:** Android + Termux · **Root required:** No · **Lab scope:** local files, localhost or example.com only

## 1. Learning objectives
By the end of this lesson, you should be able to explain the key concepts, perform each exercise safely, interpret results, and record what you learned.

## 2. Concepts explained
1. Variables hold values; conditions make decisions; loops repeat operations; functions organize reusable logic.

2. Use pathlib to handle local paths and avoid accidental access outside your lab.

3. A password-strength demonstration can check length and character variety, but it cannot guarantee real-world password safety.

4. SHA-256 detects content changes when compared against a trusted baseline.

5. Do not hardcode or publish real passwords or API keys.

## 3. Preparation and safety
- Obtain authorization before testing any system outside your own local lab.
- Work with fictional training data. Never upload passwords, private logs, tokens or personal data.
- Update Termux packages as needed: `pkg update && pkg upgrade -y`.
- Commands marked as server commands may need a separate Termux session. **Do not run the next command in the same session while a server is occupying it.**
- Some Android builds restrict networking diagnostics; record the error rather than bypassing device safeguards.

## 4. Step-by-step practical lesson
### Step 1
Check the Python version.

### Step 2
Create a basic Python program using a function and conditional.

### Step 3
Create a fictional sample file.

### Step 4
Compute its SHA-256 digest and then change the file to observe a different digest.

### Step 5
Build and test a simple local password checklist with fictional examples.

## 5. Termux command reference
These are **individual reference commands**, not one uninterrupted shell script. Run them in the order and session described above. Some lines are alternatives, and comment lines beginning with `#` are explanations.

```sh
python --version
mkdir -p ~/ethical-hacking-course/lesson-04 && cd ~/ethical-hacking-course/lesson-04
printf 'version one\n' > sample.txt
python -c 'from pathlib import Path; import hashlib; p=Path("sample.txt"); print(hashlib.sha256(p.read_bytes()).hexdigest())'
printf 'version two\n' >> sample.txt
sha256sum sample.txt
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
1. **Question:** What is a function?
   **Answer:** A reusable named block of code.

2. **Question:** Does a strong-looking password guarantee safety?
   **Answer:** No.

3. **Question:** What changes a file hash?
   **Answer:** Any change to the file bytes with overwhelming probability.

## 9. Completion checklist
- [ ] I can explain the concepts in my own words.
- [ ] I completed the authorized local exercise or documented why my device could not run it.
- [ ] I interpreted output without claiming unverified exploitation.
- [ ] I recorded findings and cleaned up test processes.
- [ ] I answered the quiz.

[← Return to course index](../README.md)
