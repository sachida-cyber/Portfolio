# False Positive Tuning — Brute Force Rule (Lab Notes)

Issue observed:
- Initial rule fired frequently during scheduled admin maintenance windows (authorized automated tasks).

Tuning steps applied:
1. Exclude known admin IP ranges: add IP range exclusion (e.g., 10.10.0.0/24) in rule condition.
2. Increase threshold to >10 failed attempts within 5 minutes for production, keep 8 for lab.
3. Add context: require source IP geolocation != corporate country OR unusual account name pattern.
4. Add whitelist for service accounts and known monitoring agents.

Result:
- Alerts reduced significantly (lab note: synthetic data: from 120/day to ~8/day).
