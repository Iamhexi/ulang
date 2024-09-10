# µLang

MicroLang (μLang) is a programming language aimed at great REPL (read-evaluate-print loop) experience,
and pleasant everyday use.

## Installation

To install µLang:
1. Clone the repository and enter its main directory.
2. Create a virtual environment: `python -m venv venv`.
3. Install dependencies: `pip install -r requirements.txt`.

## Usage

1. Enter a virtual environment: `source venv/bin/activate`.
2. Run the interpreter: `python main.py`.
3. Type an expression to evaluate: `if 10 > 30 then "Hi, µLang"`, and then press `Enter`.
4. Or type, for example: `15:48 - 7:21` and press `Enter` (to check how much time has passed from 7:21 to 15:48). And so on.
5. `Ctrl + c` to exit.

## Features

Features of µLang:
- free and **open-source** forever
- **easy** to use
- aimed at everyday use
- evaluated to Python

## Syntax

### Literals

Available literals:
- **string** between double quotes, e.g.: `"Hello, µLang!"`
- **number**  either integer or floating-point number, e.g.: `-21` or `3.14`
- **time** made of hours and minutes, e.g.: `20:15`
- **duration** represents span of time, e.g.: `1h30m`

### Arthmetics

Available arthmetic operators:
- **addtion** with `+`
- **subtraction** with `-`
- **multiplication** with `*`
- **division** with `/`
- **exponentiation** with `^`
