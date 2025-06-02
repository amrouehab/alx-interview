# 0x06. Star Wars API

This project is part of the ALX Interview preparation curriculum.

## Description

This script retrieves and prints all characters from a specified Star Wars movie using the [Star Wars API (SWAPI)](https://swapi.dev/). The characters are printed in the same order as they appear in the API response.

## Files

### `0-starwars_characters.js`

- Usage: `./0-starwars_characters.js <Movie_ID>`
- Example: `./0-starwars_characters.js 3`
- Uses the `request` module to send HTTP GET requests.
- Prints one character name per line, in the same order as listed in the film data.

## Requirements

- All scripts are run using `Node.js` version 10.14.x.
- Code follows the **semistandard** style (Standard + semicolons).
- No use of `var` — only `let` and `const`.
- All scripts are executable.
- Only allowed editors: `vi`, `vim`, `emacs`.

## Example Output

```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...

