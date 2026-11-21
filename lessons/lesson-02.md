# Lesson 2: Networking Fundamentals

**Level:** Beginner · **Platform:** Android + Termux · **Root required:** No · **Lab scope:** local files, localhost or example.com only

## 1. Learning objectives
By the end of this lesson, you should be able to explain the key concepts, perform each exercise safely, interpret results, and record what you learned.

## 2. Concepts explained
1. An IP address identifies a network interface. IPv4 and IPv6 use different address formats.

2. DNS resolves names into records, such as A and AAAA records.

3. TCP provides connection-oriented transport; UDP provides datagrams without a built-in connection.

4. A port identifies a service endpoint. HTTPS commonly uses TCP port 443, but services may use other ports.

5. HTTP headers and response codes provide useful diagnostic information, not automatic proof of a vulnerability.

## 3. Preparation and safety
- Obtain authorization before testing any system outside your own local lab.
- Work with fictional training data. Never upload passwords, private logs, tokens or personal data.
- Update Termux packages as needed: `pkg update && pkg upgrade -y`.
- Commands marked as server commands may need a separate Termux session. **Do not run the next command in the same session while a server is occupying it.**
- Some Android builds restrict networking diagnostics; record the error rather than bypassing device safeguards.

## 4. Step-by-step practical lesson
### Step 1
Confirm network access without probing unfamiliar hosts.

### Step 2
Inspect local interface information if supported by your Android/Termux version.

### Step 3
Resolve the reserved example.com domain.

### Step 4
Read HTTP response headers from example.com.

### Step 5
Explain the difference between an IP address, DNS name and port.

## 5. Termux command reference
These are **individual reference commands**, not one uninterrupted shell script. Run them in the order and session described above. Some lines are alternatives, and comment lines beginning with `#` are explanations.

```sh
pkg install dnsutils curl inetutils -y
ip addr
nslookup example.com
dig example.com A +short
curl -I https://example.com
ping -c 2 example.com
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
1. **Question:** What does DNS do?
   **Answer:** Resolves names to DNS records.

2. **Question:** What is a port?
   **Answer:** A logical transport-layer service endpoint.

3. **Question:** Does a failed ping prove a host is down?
   **Answer:** No; ICMP may be filtered.

## 9. Completion checklist
- [ ] I can explain the concepts in my own words.
- [ ] I completed the authorized local exercise or documented why my device could not run it.
- [ ] I interpreted output without claiming unverified exploitation.
- [ ] I recorded findings and cleaned up test processes.
- [ ] I answered the quiz.

[← Return to course index](../README.md)
