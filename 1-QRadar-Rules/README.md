# 1-QRadar-Rules

Purpose: Demonstrate simple detection queries, a sample QRadar rule, Splunk SPL equivalents, and tuning notes for common SOC events.

## Files
- `AQLQueries/brute_force_detection.aql` — sample AQL to detect repeated failed logins.
- `DetectionRules/brute_force_detection_rule.json` — example JSON export (lab).
- `splunk_bruteforce_search.spl` — Splunk SPL to detect similar behavior.
- `OffenseTuning/false_positive_tuning_notes.md` — notes on tuning and reducing noise.
- `screenshots/qradar_bruteforce_alert.png` — one example screenshot (sanitized).
