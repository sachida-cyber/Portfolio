# 3-Log-Analysis

Purpose: show simple scripts to parse logs and generate summary reports used for triage.

Files:
- `scripts/parse_failed_logins.py` — parse sample CSV of Windows events and summarize failed login counts by IP/user.
- `sample_logs/sample_windows_log.csv` — synthetic sample.
- `outputs/failed_login_summary.csv` — sample output.

How to run:

```
python3 scripts/parse_failed_logins.py sample_logs/sample_windows_log.csv outputs/failed_login_summary.csv
```
