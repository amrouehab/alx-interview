RE# 0x00. Pascal's Triangle

## Description
This project contains an implementation of Pascal's Triangle in Python. Pascal's Triangle is a triangular array of numbers where each number is the sum of the two numbers directly above it.

## Task

### 0. Pascal's Triangle
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer

## Files

### 0-pascal_triangle.py
Contains the implementation of the `pascal_triangle` function.

## Usage

```python
#!/usr/bin/python3
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

### Expected Output:
```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Algorithm Explanation

Pascal's Triangle follows these rules:
1. The first row contains only the number 1
2. Each subsequent row starts and ends with 1
3. Each interior number is the sum of the two numbers above it in the previous row

For example, in row 3 `[1,2,1]`:
- The middle number 2 = 1 + 1 (from row 2: `[1,1]`)

In row 4 `[1,3,3,1]`:
- First 3 = 1 + 2 (from row 3: `[1,2,1]`)
- Second 3 = 2 + 1 (from row 3: `[1,2,1]`)

## Repository Information
- **GitHub repository:** alx-interview
- **Directory:** 0x00-pascal_triangle
- **File:** 0-pascal_triangle.py

## Author
Created as part of the ALX Software Engineering program.

