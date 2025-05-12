#!/usr/bin/python3
import sys
import signal

total_size = 0
status_counts = {}
valid_statuses = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

def print_stats():
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        print("{}: {}".format(status, status_counts[status]))

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.strip().split()
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size

            if status_code in valid_statuses:
                if status_code not in status_counts:
                    status_counts[status_code] = 0
                status_counts[status_code] += 1
        except (IndexError, ValueError):
            continue

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()

