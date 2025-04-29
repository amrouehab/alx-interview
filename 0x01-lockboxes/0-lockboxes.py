#!/usr/bin/python3
"""Lockboxes problem solution"""

def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked"""
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = set([0])  # box 0 is always open
    keys = set(boxes[0])  # collect initial keys

    # Keep looking for new boxes to open
    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in visited:
            visited.add(key)
            keys.update(boxes[key])  # Add the keys found in this newly opened box

    # If we've visited all boxes, success
    return len(visited) == n

