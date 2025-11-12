# Wireshark — DNS Exfiltration (Sample Analysis)

Summary:
- PCAP shows repeated DNS TXT queries to an uncommon external domain.
- Suspicious pattern: short interval repeated TXT queries with encoded payload.

Steps to reproduce:
1. Open `wireshark_pcaps/dns_exfiltration_sample.pcap` in Wireshark.
2. Apply display filter: `dns.qry.type == 16` (TXT queries) and inspect query names.
3. Note source IP and count of queries; map to client host in topology.

Conclusion:
- Logged as suspicious — escalate for further host investigation and containment.
