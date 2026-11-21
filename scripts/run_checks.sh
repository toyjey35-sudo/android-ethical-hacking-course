#!/data/data/com.termux/files/usr/bin/bash
set -e
cd "$HOME/security-automation-lab" || exit 1
python "$HOME/security-automation-lab/file_monitor.py" check
python "$HOME/security-automation-lab/log_alert.py"
python "$HOME/security-automation-lab/security_report.py"
