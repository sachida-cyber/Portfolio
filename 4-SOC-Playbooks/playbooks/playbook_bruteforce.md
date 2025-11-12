# Playbook — Brute Force Detection (L1)

**Objective:** Triage suspected brute-force attempts and perform containment.

1. Detection
   - Source: SIEM alert (Splunk/QRadar)
   - Indicator: >8 failed logins in 5 minutes (per IP)

2. Initial Triage (L1)
   - Confirm time window and check if IP belongs to known admin range.
   - Query logs for other related activity (process, source ports).
   - Check asset criticality (is it domain controller, admin server?)

3. Containment
   - If confirmed malicious: temporarily disable the account or block source IP at perimeter firewall.
   - Create ticket and escalate to L2 with evidence.

4. Eradication & Recovery
   - Reset compromised passwords, scan affected host for malware.
   - Re-enable account only after validation.

5. Post-Incident
   - Add tuning note to SIEM: exclude whitelist, refine threshold, add geolocation checks.
