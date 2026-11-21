# Final project: Local Security Assessment

Practice on **127.0.0.1 only** using fictional data.

1. Create `index.html` with a simple training page.
2. Start `python -m http.server 8000 --bind 127.0.0.1` in one Termux session.
3. In another session run `curl -i http://127.0.0.1:8000/`.
4. Run `nmap -sT -Pn -p 8000 127.0.0.1 -oN nmap_results.txt`.
5. Record `sha256sum index.html > index.sha256` and verify with `sha256sum -c index.sha256`.
6. Analyze fictional authentication events using `../scripts/log_alert.py` or adapt the script to your log filename.
7. Produce a report separating observations, possible risks, evidence, and recommendations.
8. Stop the HTTP server with Ctrl+C, then rescan localhost to verify closure.

**Never upload private logs, credentials, or identifying device data to a public repository.**
