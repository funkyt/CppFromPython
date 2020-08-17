# C++ From Python

## Lesson 0-0

A gentle introduction to C++ for Python programmers.

---

## Prerequisites

I assume the following:
* Introductory Python
* Working email account
* A recent browser (Chrome, Firefox, Edge, Safari)

---

## This Class

* Lectures expected to be ~30 minutes each
* Homework at the end of each one
 - Keep your work in a single GitHub repo
 - One folder per assignment
 - Code & written answers saved therein

### Objective

ProjectEuler.net problems 1-10

---

## What is C++

* A *compiled* language
 - Running code is a two-step process: compile, then run
* Multi-paradigm
 - Supports multiple programming styles
* Favors efficiency over all else
 - "Only pay for what you use"

--

### Cons (compared to Python)

* Verbose
* Anemic standard library
* Harder to experiment

--

### Pros (compared to Python)

* Efficiency, efficiency, efficiency
* Statically checked types,  static analysis in general

---

## Compilers

There is a canonical Python implementation (sometimes called "CPython"),
but there is no one, single, C++ compiler.  The following are the most
commonly used:

* Microsoft Visual C++ (cl)
* GNU Compiler Collection (g++)
* Clang (clang++)

--

We'll be using Clang, because it's available everywhere for free, and has
a reputation for having the least cryptic error messages.

---

## Tools

We will use the following tools for this class:

* GitHub.com (for saving and submitting your work)
 - NOTE: publicly visible!
* Repl.it (online IDE, includes Clang v7)
 - Everything runs in the browser
 - Nothing to install locally

--

You may use your own tools, but:
* Responsible for installation yourself
* Won't be able to provide support
* Compilers may differ in
 - Error messages
 - Feature availability
 
---

## Hello World

Repl.it will create this for you, by default, when you create a C++ repl in
a file named `main.cpp`.

```c++
#include <iostream>

int main() {
  std::cout << "Hello World!\n";
}
```

We'll discuss the pieces of this program in slightly more detail during the next lesson.

---

## Hello World on Repl.it (Demo)

<iframe height="500px" width="100%" src="https://repl.it/@TimothyElling/AcrobaticMeagerInterfaces?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

---

## Homework

### Setup

1. Create a (free) github.com account
2. Create a (free) repl.it account
3. Create a new C++ repl (should include "hello world")
4. Save this repl to your GitHub account:
 * "Version Control" > "Create a Git Repo" > "Connect to GitHub"

### Experimentation

1. **QUESTION:** What is the output when you click `Run`?
2. Create a new folder called `hw-0.0`, and copy `main.cpp` into it
3. Compile and test this yourself using the commands:
 * `> clang++ hw-0.0/main.cpp -o main-0.0`
 * `> ./main-0.0`
4. **QUESTION:** What happens if you remove the `\n`?
5. **QUESTION:** What do you think each part of `int main()` means?
6. Customize the output message somehow (your choice)
7. Commit & push, then send me the github link