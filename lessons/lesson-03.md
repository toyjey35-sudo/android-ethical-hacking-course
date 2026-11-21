# Lesson 3: Linux, Shell and Kali Fundamentals

**Level:** Beginner · **Platform:** Android + Termux · **Root required:** No · **Lab scope:** local files, localhost or example.com only

## 1. Learning objectives
By the end of this lesson, you should be able to explain the key concepts, perform each exercise safely, interpret results, and record what you learned.

## 2. Concepts explained
1. Linux directories form a filesystem tree; relative paths depend on your working directory.

2. Termux is not identical to a rooted Linux host or a full Kali Linux installation.

3. File permissions determine who may read, write and execute files.

4. The shell executes commands; processes have identifiers and may be stopped.

5. Kali NetHunter Rootless is a distinct optional environment; it is not required for this course.

## 3. Preparation and safety
- Obtain authorization before testing any system outside your own local lab.
- Work with fictional training data. Never upload passwords, private logs, tokens or personal data.
- Update Termux packages as needed: `pkg update && pkg upgrade -y`.
- Commands marked as server commands may need a separate Termux session. **Do not run the next command in the same session while a server is occupying it.**
- Some Android builds restrict networking diagnostics; record the error rather than bypassing device safeguards.

## 4. Step-by-step practical lesson
### Step 1
Print your identity, location and system details.

### Step 2
Create a safe local directory and text file.

### Step 3
Inspect file permissions and change them to owner-only.

### Step 4
Practice searching text and listing processes.

### Step 5
Clean up only the files you created.

## 5. Termux command reference
These are **individual reference commands**, not one uninterrupted shell script. Run them in the order and session described above. Some lines are alternatives, and comment lines beginning with `#` are explanations.

```sh
whoami
pwd
uname -a
mkdir -p ~/ethical-hacking-course/lesson-03 && cd ~/ethical-hacking-course/lesson-03
printf 'first shell exercise\n' > notes.txt
ls -l notes.txt
chmod 600 notes.txt
cat notes.txt
grep 'shell' notes.txt
ps -ef
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
1. **Question:** What does pwd show?
   **Answer:** Current working directory.

2. **Question:** What does chmod 600 mean?
   **Answer:** Owner can read/write; others have no permissions.

3. **Question:** Is root required for these exercises?
   **Answer:** No.

## 9. Completion checklist
- [ ] I can explain the concepts in my own words.
- [ ] I completed the authorized local exercise or documented why my device could not run it.
- [ ] I interpreted output without claiming unverified exploitation.
- [ ] I recorded findings and cleaned up test processes.
- [ ] I answered the quiz.

[← Return to course index](../README.md)
