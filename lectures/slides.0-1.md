# C++ From Python

## Lesson 0-1

### Basic Syntax, I/O, Functions

---

## Basic Syntax

A lot of syntax is similar to Python:
* Call functions using parenthesis after the function name
* Mathematical expressions follow order of operations
* Many flow-control keywords have the same meanings:
 - `return`, `if`, `else`, `while`, `for`, `break`, `continue`, etc

There are important differences, however:
* Most statements end with a semicolon `;`
* Every variable and function needs to have a type.
* Grouping of statements is done with `{` and `}`

Python | C++
:-- | :--
`x = 0` | `int x = 0;`
`x += 1` | `x += 1;` or `++x;`
`def next(x):`<br>&nbsp;&nbsp;&nbsp;`  return x+1` | `int next(int x) {`<br>&nbsp;&nbsp;&nbsp;` return x+1;`<br>`}`

I'll list over syntax in more detail later.

---

## Types

Some Python data types have an **equivalent** type in C++, but some do not.

Most notably, built-in integer types all have fixed ranges, and cannot store
arbitrarily-large numbers.

Additionally, those starting with `std::` are not part of the core language, and come
from a library instead.

Python | C++
:--: | --:
`bool` | **`bool`**
`int` | `short`, `int`, `unsigned int`, `long`, ...
`float` | `float`, **`double`**
`str` | **`std::string`**, `char*`
`list` | **`std::vector<T>`**
`dict` | **`std::unordered_map<K,V>`**
`NoneType` | `void`

---

## Includes

This is similar to Python's `import`.

You can use libraries with the `#include` directive.  For these lectures, we'll
stick to the standard C++ library, also known as the STL.  Some example `#include`s
that will eventually be useful (you don't have to remember these):

```c++
#include <iostream>        // Standard input/output
#include <string>          // The  string type
#include <vector>          // Like `list` in Python
#include <unordered_map>   // Like `dict`
#include <unordered_set>   // Like `set`
```

---

## Variables

Defining a variable always starts with it's type, then name, and optionally an initial value.

```c++
int x;
double z = 2.0;
std::string name = "Tim";
```

If you don't provide an initial value, then it is unspecified(*).

---

## Streams

In Python, you had `print()` and `input()` available as built-in functions.

In C++, you have `std::cout` and `std::cin` instead, and they're part of a library.

```c++
// TODO - Convert to REPL
#include <iostream>  // Provides std::cin, std::cout

int main() {
  std::cout << "Hello ";                    // The `<<` means "write to"
  std::cout << "World!\n";                  // Newline not automatic

  int x;
  std::cin >> x;                            // The `>>` means "read from"
  std::cout << "You wrote: " << x << "\n";  // You can chain them together
}
```

---

## Strings

Strings are also something that you have to ask for.

```c++
#include <iostream>
#include <string>  // Provides std::string

int main() {
  std::cout << "What is your favorite flavor of ice cream?\n";
  std::string favorite;
  std::cin >> favorite;  // Reads until the next whitespace
  std::cout << "Ew, " << favorite << " is gross!\n";
}
```

---

## Functions

Every C++ program must have at *least* one function, called `int main()`.  This is the
function that gets run when your program is executed.  Unlike Python, you can't just put
statements outside of a function and have them be run for you.

The type `void` can be used for a function that doesn't return anything(*).  In this
case, it's similar to `None`/`NoneType` from Python.

```c++
int next(int x) {
  return x + 1;
}

void greet(std::string name) {
  std::cout << "Hello, " << name << "\n";
}

int main() {
  greet("Tim");
  greet("You");
  return 0;  // Technically optional for main()
}
```

---

## Conditionals

The `if` statement is almost identical to Python, with a few differences:

* `&&` in place of `and`
* `||` in place of `or`
* `!` in place of `not`
* `else if` in place of `elif`

```c++
if (x % 2 == 0) {
  std::cout << "x is even\n";
} else if (x % 2 == 1) {
  std::cout << "x is odd\n";
} else {
  std::cout << "x is... impossible?\n";
}
```

Technically the `{}` can be left out for short statements, but don't do it!

---

## Too much talk, time for code!

---

## Homework

Write a C++ program that can carry out interactions on the next slide.

* You should handle each case in a separate function
* You can fail however you like on bad inputs
* Pay careful attention to the types
* Your output should match exactly

Make sure to commit & push your changes to GitHub.

---

## Example Interaction

```
Hello, who is this?
```
--
```
Tim
```
--
```
Hello Tim, would you like me to compute for a square, rectangle, or circle?
```
--
```
rectangle
```
--
```
What is the length?
```
--
```
5
```
--
```
What is the height?
```
--
```
3
```
--
```
The area is 15.0, and the perimeter is 16.0.
```
