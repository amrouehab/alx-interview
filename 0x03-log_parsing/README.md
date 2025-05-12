# 0x03. Log Parsing

## Description

This project is part of the ALX interview preparation curriculum. It involves writing a Python script that parses logs from standard input and computes statistics based on the data.

## Requirements

- All scripts are written and tested on Ubuntu 20.04 LTS.
- Python version: 3.4.3
- Code style: PEP 8 (version 1.7.x)
- Scripts are executable and start with `#!/usr/bin/python3`.
- Logs are read from `stdin`.

## Task

### 0. Log parsing

Write a script that reads `stdin` line by line and computes the following metrics:

- **Total file size**: Sum of all file sizes in the log entries.
- **Status code counts**: Count of each valid status code (200, 301, 400, 401, 403, 404, 405, 500).

**Behavior:**

- Every 10 lines and/or on `KeyboardInterrupt` (`CTRL + C`), it prints:
  - Total file size
  - Counts of status codes that have occurred so

