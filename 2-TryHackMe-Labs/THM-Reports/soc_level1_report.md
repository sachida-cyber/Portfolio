# TryHackMe — SOC Level 1 Report (sample)

**Objective:** Learn SIEM workflows, simple IOC hunting, and alert triage.

**Steps:**
1. Completed "SOC Level 1" modules on TryHackMe.
2. In lab environment, ingested Windows Security events into Splunk.
3. Wrote SPL (see `../1-QRadar-Rules/splunk_bruteforce_search.spl`) and verified alert on simulated brute-force.

**Key Findings:**
- Many detection rules require contextual tuning for service accounts and maintenance windows.
- Useful IOC types: failed login series, suspicious PowerShell execution, unusual DNS queries.

**MITRE ATT&CK mapping:** Initial Access (T1078) — Valid Accounts (detected by failed login patterns)

**Lessons:** Structured playbooks are necessary to avoid noise and speed triage.
