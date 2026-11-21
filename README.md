# Android Ethical Hacking Course (Termux)

A **14-lesson beginner course** in English for learning authorized, defensive security fundamentals on Android using Termux, without root.

> **Safety:** Only test systems you own or have explicit permission to assess. Labs use fictional data and localhost (127.0.0.1). Do not publish real passwords, tokens, private logs, or personal information.

## Lessons
- [Lesson 01: Ethics, Permission and Termux Setup](lessons/lesson-01.md)
- [Lesson 02: Networking Fundamentals](lessons/lesson-02.md)
- [Lesson 03: Linux and Kali Fundamentals](lessons/lesson-03.md)
- [Lesson 04: Python for Ethical Hackers](lessons/lesson-04.md)
- [Lesson 05: Information Gathering and OSINT](lessons/lesson-05.md)
- [Lesson 06: Network Security Testing with Nmap](lessons/lesson-06.md)
- [Lesson 07: Web Application Security](lessons/lesson-07.md)
- [Lesson 08: Android Application Security](lessons/lesson-08.md)
- [Lesson 09: Wi-Fi Security Fundamentals](lessons/lesson-09.md)
- [Lesson 10: Cryptography and Password Security](lessons/lesson-10.md)
- [Lesson 11: Vulnerability Assessment Fundamentals](lessons/lesson-11.md)
- [Lesson 12: Digital Forensics and Incident Response](lessons/lesson-12.md)
- [Lesson 13: Security Automation with Python](lessons/lesson-13.md)
- [Lesson 14: Final Ethical Hacking Project](lessons/lesson-14.md)

## Getting started
Install Termux from a trusted distribution, then run:

```sh
pkg update
pkg install python curl nmap nano coreutils dnsutils -y
```

Follow the lessons in order. Run examples only in your own Termux environment. Some exercises require a second Termux session.

## Final project
Lesson 14 walks through a local HTTP service assessment, SHA-256 evidence checks, fictional log analysis, and reporting. Stop the local test server after each lab.

## Learning outcomes
Ethics, Linux, networking, Python, OSINT, Nmap, web security, Android security, Wi-Fi security, cryptography, vulnerability assessment, forensics, automation, and reporting.

These materials are **learning notes and practical exercises**, not a professional certification or authorization to test third-party systems.
