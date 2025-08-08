"""
======================
  Python Basic Syntax
======================

print() Function:
-----------------
- The print() function is used to display output in the terminal/console window.
- It takes the values you pass to it (strings, numbers, variables, etc.), converts them to a string internally, and then displays them.
- You can pass multiple values to print(), and by default, they will be separated by a space.

Real-World Use:
---------------
- In production (real-world projects), print() is rarely used to show information to the end user.
  Instead, output is shown through UI elements, web pages, or API responses.
- However, print() is extremely useful for learning, testing, and quick debugging during development.
- For serious debugging, developers often use tools like logging, debuggers (pdb), or IDE breakpoints.

Technical Details:
------------------
- **Type Casting:** Before displaying, print() converts all arguments into a string (str) representation.
- **Parameters:**
    - `sep` (separator): Specifies the string inserted between multiple values. Default is a space `" "`.
    - `end`: Specifies what is printed at the end. Default is a newline character `"\n"`.
    - Example:
        print("Hello", "World", sep="-", end="!!!\n")
        # Output: Hello-World!!!

"""

print("Hello New Programmer!!")


"""
==============================
   Variables and Data Types
==============================

Theoretical Understanding:
---------------------------
- Variables are containers for storing values in a program.
- Think of a variable as a box: you can put something inside it (a value) and label it (the variable name) so you can find it later.
- Example analogy: Handing your cookie packet to your secret candy box for later — the box is the variable, the cookies are the value.

Technical Understanding:
-------------------------
- A variable does not store the value directly; it stores the memory address of the value.
- Example: A bottle with a tag that says where the treasure is buried — the bottle (variable) points to the treasure (value in memory).
- Variables are *objects* in Python, meaning they have properties and behaviors defined by their type/class.

Variable Naming Rules:
----------------------
1. Must start with a letter (a–z, A–Z) or an underscore `_`.
2. Cannot start with a number.
3. Cannot contain spaces or special characters except `_`.
4. Cannot be a Python keyword (`if`, `class`, `for`, etc.).
5. Should not be enclosed in quotes — that would make it a string literal, not a variable.
6. Naming convention: LHS = RHS
   - LHS (Left Hand Side) → Variable name
   - RHS (Right Hand Side) → Value assigned to the variable

Naming Styles:
--------------
- camelCase → `userName`
- PascalCase → `UserName`
- snake_case → `user_name`
- SCREAMING_SNAKE_CASE → `MAX_VALUE`
- kebab-case → `user-name` (not valid in Python — will cause error)
- HungarianNotation → `strName`, `iCount`

Extra Notes:
------------
- Variables are **case-sensitive** → `a = 1` and `A = 1` are different.
- Variables themselves also consume memory (to store the reference address), and the actual value consumes its own memory space.
- Variable values can be changed during execution unless declared constant by convention (Python has no true constants, but SCREAMING_SNAKE_CASE is used to indicate one).
"""

# Examples of variables in Python:
variable_name = "Your Name"        # String
yourMarks = 23                     # Integer
YOUR_PERCENTILE = 45.8842          # Float (constant by convention)
myOnlineStatus = False             # Boolean


"""COMDITIONALS

"""

