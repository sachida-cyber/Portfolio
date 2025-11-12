#!/usr/bin/env python3
"""
parse_failed_logins.py
Simple log parser: reads a CSV of Windows Security events and outputs counts of failed logins per src_ip and username.
Sanitized sample data only.
"""

import csv
import sys
from collections import defaultdict

def parse(input_csv, output_csv):
    counts = defaultdict(lambda: {'failed_count':0})
    with open(input_csv, newline='') as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            # expected fields: timestamp,eventid,src_ip,username,message
            eventid = row.get('eventid','').strip()
            if eventid == '4625' or 'failed' in row.get('message','').lower():
                key = (row.get('src_ip','-'), row.get('username','-'))
                counts[key]['failed_count'] += 1
    with open(output_csv, 'w', newline='') as out:
        writer = csv.writer(out)
        writer.writerow(['src_ip','username','failed_count'])
        for (src_ip, username), data in counts.items():
            writer.writerow([src_ip, username, data['failed_count']])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: parse_failed_logins.py input.csv output.csv")
        sys.exit(1)
    parse(sys.argv[1], sys.argv[2])
    print("Done.")
