# Learning Basics of Python

---

`From  Very Basic To Very Advance`

##### Topics To be coverd 
- Basic Syntax
- Varibale and Datatypes
- Conditionals
- Loops
- Type casting
- Exceptions
- Functions , Built-in-Functions
- List
- Tuple
- Set
- Dictionary

**To Check Your python Version**

In Terminal write

```commandline
python --version
Python 3.12.4 
```
for me its python 3.12.4 version

Here’s your **`print()` guide** converted into clean **Markdown** format, ready for your repo’s `.md` file:

---

# 🐍 Python Basic Syntax

---
### `print()` Function 

---


## 📌 Overview

The `print()` function is used to display output in the **terminal/console window**.

* It takes the values you pass to it (strings, numbers, variables, etc.), **converts them into a string** internally, and then displays them.
* You can pass **multiple values**, which by default are separated by a space.

---

## 🎯 Real-World Use

* In production (real-world projects), `print()` is **rarely used** to show information to end users.
  Instead, output is shown through **UI elements**, **web pages**, or **API responses**.
* Extremely useful for **learning**, **testing**, and **quick debugging**.
* For serious debugging, use tools like:

  * Python’s `logging` module
  * Debuggers (`pdb`)
  * IDE breakpoints

---

## ⚙ Technical Details

* **Type Casting:** Before displaying, `print()` converts all arguments into a `str` representation.
* **Parameters:**

  * `sep` (separator): String inserted between multiple values. Default = `" "`
  * `end`: String printed after output. Default = newline `"\n"`
  * **Example:**

    ```python
    print("Hello", "World", sep="-", end="!!!\n")
    # Output: Hello-World!!!
    ```

---

# 📦 Variables and Data Types

---

## 📌 Overview

Variables are **containers** for storing values in a program.

* Think of a variable as a **box**:  
  You can put something inside it (a value) and label it (the variable name) so you can find it later.
* **Analogy:** Handing your cookie packet to your secret candy box for later —  
  the **box** is the variable, the **cookies** are the value.

---

## ⚙ Technical Understanding

* A variable does not store the value directly; it stores the **memory address** of the value.
* **Analogy:** A bottle with a tag that says where the treasure is buried —  
  the **bottle** (variable) points to the **treasure** (value in memory).
* In Python, variables are actually **objects**, meaning they have properties and behaviors defined by their **type/class**.

---

## 📝 Variable Naming Rules

1. Must start with a letter (`a–z`, `A–Z`) or an underscore `_`.
2. Cannot start with a number.
3. Cannot contain spaces or special characters except `_`.
4. Cannot be a Python keyword (`if`, `class`, `for`, etc.).
5. Should **not** be enclosed in quotes — that would make it a string literal.
6. **Assignment format:**  
   **LHS** (Variable Name) = **RHS** (Value)

---

## ✍ Naming Styles

| Style                 | Example         | Notes |
|-----------------------|-----------------|-------|
| **camelCase**         | `userName`      | Common in JavaScript |
| **PascalCase**        | `UserName`      | Common in classes |
| **snake_case**        | `user_name`     | Preferred in Python |
| **SCREAMING_SNAKE_CASE** | `MAX_VALUE`  | Used for constants |
| **kebab-case** ❌     | `user-name`     | Not valid in Python |
| **HungarianNotation** | `strName`       | Not Pythonic, rarely used |

---

## 📌 Extra Notes

* Variables are **case-sensitive** → `a = 1` and `A = 1` are different.
* Variables themselves consume memory (to store the reference address),  
  and the actual value consumes its own memory space.
* Python has **no true constants**, but constants are indicated using `SCREAMING_SNAKE_CASE`.

---

## 💻 Examples

```python
# String
variable_name = "Your Name"

# Integer
yourMarks = 23

# Float (constant by convention)
YOUR_PERCENTILE = 45.8842

# Boolean
myOnlineStatus = False



