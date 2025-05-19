#!/usr/bin/python3
"""
UTF-8 validation function
"""

def validUTF8(data):
    """Check if a list of integers represents a valid UTF-8 encoding"""
    n_bytes = 0

    for num in data:
        # We only care about the last 8 bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count number of leading 1's to determine character length
            mask = 0x80  # 10000000
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # 1 byte character
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if byte starts with 10xxxxxx
            if not (byte & 0x80 and not (byte & 0x40)):
                return False

        n_bytes -= 1

    return n_bytes == 0

