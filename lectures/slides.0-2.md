# C++ From Python

## Lesson 0.2

* Total grab bag!
* Declaration vs Definition
* Structs
* Value vs Reference
* File I/O (streams)
* Vectors

---

## Homework Review

* Hopefully you used `double` instead of `int` for your dimensions.
* String comparisons should just work.

```C++
std::string shape;
std::cin >> shape;
if (shape == "rectangle") {
  rectangle();
} else if (shape == "square") {
  square();
} else if (shape == "circle") {
  circle();
} else {
  std::cout << "I don't know '" << shape << "'\n";
}
```

---

## Declaration and Definition

Remember that you have to write your functions in a particular order?  It
turns out you just have to *declare* them, not *define* them.

Let C++ know what kind of function to expect, then you can define it later.

```C++

int one_more(int x);  // No body, so this is a declaration

int two_more(int x) {
  // This next line would fail without the declaration above
  return one_more(one_more(x));
}

// We must define it eventually... it could be in another file!
int one_more(int x) {
  return x + 1;
}
```

* *declaration*  --- Only tells C++ the function's type.
* *definition*  --- Tells C++ the details of the function.

---

## Structs

C++ supports object-oriented programming.  We'll start small, with `struct`.

A `struct` ties several variables together, and allows us to pass them around
together as a unit.  This is very similar to Python's `class` keyword.

Once you define a `struct`, you can use it like any other type!  You can access
the internal variables using the dot (`.`).

```C++
struct FullName {
  std::string first;  // These are called "members" of the struct
  std::string last;
};

void greet(FullName name);

int main() {
  std::cout << "Enter your first and last name:\n";
  FullName name;
  std::cin >> name.first >> name.last;
  greet(name);
}

void greet(FullName name) {
  std::cout << "Hello " << name.first << " " << name.last << "!\n";
}
```

---

## Structs: Member functions

You can define member functions that belong to these structs.

```C++
struct FullName {
  std::string first;  // These are called "members" of the struct
  std::string last;

  std::string bond_like() {
    return last + ", " + first + " " + last;
  }
};
```

* These functions can treat others members as "in scope".
* You don't need the `self` keyword (as in Python)
  - (There is a C++ version, `this`, but we'll cover that later)

---

## Structs: Member function declarations

You can also *declare* member functions, so that you can put the definition
later.  This requires using the `::` operator in the name.

```C++
struct FullName {
  // ...
  std::string bond_like();
};

std::string FullName::bond_like() {
  // ...
}
```

This is the way C++ libraries are often organized.

---

## Structs: Constructors

You can define a special member function that's used to create your structs.

This is called a *constructor*, and is C++'s version of `__init__`.  It has the same name as the struct, and no return type.

```C++
struct FullName {
  std::string first;
  std::string last;

  FullName(std::string fst, std::string lst) {
    first = fst;  // Note: there is a better way to do this
    last = lst; // (we will learn it later)
  }
};

int main() {
  FullName name("James", "Bond");
  // or
  FullName name2 = FullName("James", "Bond");
}
```

---

## Values and References -- Python

In Python, the difference between *value* and *reference* semantics is based on
the type.  Things like `int`, `bool`, and `float` are passed by value, whereas
`list`, `dict`, and `class` are passed by reference.

```python
def plus_equal(x, y):
  x += y

a, b = 1, 1
plus_equal(a, b)
print(a) # Prints "1", variable is unchanged

a, b = [1], [2]
plus_equal(a, b)
print(a) # Prints "[1, 2]", variable is changed
```

---

## Values and References -- C++

In C++ you always get to choose!  You can pass a small type by reference (if
you want to change it), or a large complex type by value (if you want to
have your own copy of it).

Value is the default.  To ask for a reference, we add a `&` character.

```C++
void add_one(int x) {
  x += 1;
}

void add_one_ref(int &x) {
  x += 1;
}

int main() {
  int x = 4;
  add_one(x);
  std::cout << x << "\n";  // Prints "4"
  add_one_ref(x);
  std::cout << x << "\n";  // Prints "5"
}
```

---

## Constants

You can mark a variable (or a function parameter) `const` as a promise that
you're not going to change it.  This is especially useful with references!

It is common to pass variables by *value* if they are are small, and by *const ref*
when they are large (so that we don't have to spend time copying data).

```C++

// a and b are unmodified
int sum(const int &a, const int &b) { return a + b; }

// The compiler will reject this for us
void increment(const int &x) { x += 1; }

// Works with struct, too!
struct Point {
  double x, y;

  // This const is a promise not to change x or y
  double length() const {
    return sqrt(x*x + y*y);
  }
};
```

---

## Reading from files

C++ follows from C, which was invented alongside Unix.  One key feature of
Unix:  nearly everything is a file.

The good news: reading from a file is almost the same as reading from the
keyboard (actually, `cin` is just a "file" representing the keyboard input).

```C++
#include <fstream>  // Like iostream, but the "f" is for "file"

int main() {
  std::ifstream input("name.txt");
  std::string name;
  input >> name;

  std::cout << "Your name is " << name << "\n";
  return 0;
}
```

---

## Vectors

There are several ways to handle arrays, or lists, in C++.  We'll mostly
use `std::vector<T>`.

`std::vector` isn't a type, but instead a _template_.  It becomes a concrete type
when we combine it with an element type.

```C++
#include <vector>

{
  std::vector<int> x = {1, 2, 3};
  std::vector<int> y = x;

  std::cout << x.size() << "\n"; //  Prints 3
  std::cout << y[1] << "\n";      // Prints 2

  std::vector<std::string> z = {"hello", "goodbye"};
  z = x;  // Compiler error!
}
```

---

## Vectors - Useful Functions

* `v[i]` --- Access the element of `v` at index `i`
* `v.size()` --- Return the number of elements in `v`
* `v.push_back(x)` --- Append the element `x` to the end of `v`
* `v.front()`, `v.back()` --- Access first and last elements of `v`, respectively
* `v.reserve()` --- Reserve memory but don't increase size (advanced)

We can also use `vector` with a for-loop in C++, using the following syntax as
an example:

```C++
std::vector<int> numbers = {1, 2, 3, 4, 5};
for (int i : numbers) {
  std::cout << i << "\n";
}

std::vector<std::string> words = {"apple", "banana", "carrot"};
for (const std::string &word : words) {
  std::cout << word << "\n";
}
```

---

## Homework

Download a copy of the following file into your repository, and save it as
part of your `hw-0.2` folder.

[http://github.com/funkyt/CppFromPython/rectangles.txt]

The first line of this file contains a number, N.  After this, there are N more lines,
each describing integer coordinates of a rectangle in the order `x1`, `y1`, `x2`, `y2`.

Implement a `struct Rectangle` with both a constructor (or `<<` stream operator), as well
as a member function to test for intersection.

The output of your program should be a single number --- the number of pairs of rectangles
that overlap with nonzero area.

---

## Homework Hints

1. Note that rectangles have to overlap, not just touch.
2. Be careful not to double count.
  * If you find an intersection `A,B`, don't count `B,A` separately.
3. Have your intersection function take the rectangles by `const&`.