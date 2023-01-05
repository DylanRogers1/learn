
# C++ Tutorial: 

*This tutorial was created by Dylan Rogers. It is owned and managed by [**The Open Project**](https://youtube.com/@open-project) and any attempt to redistribute or use this content must follow the [licence](#licence)*

## Contents

[Home](#the-ultimate-guide-to-everything-python)  
[Licence](#licence)

[Chapter 1: Intro to C++](#chapter-1-intro-to-c)

## Licence

<!-- **This content is a fork of the original by Dylan Rogers. Please abide by the licence.** (uncomment this line if your document is a fork of my document) -->

If you are *not* redistributing this file (in other words, you are just a reader and this tutorial will stay on your computer, you will not send it to anyone):

* You may use the skills learned in this tutorial for personal, commercial or non-commercial projects
* As long as you do not share this tutorial, you may use it however you would like to.
* If you share the document, you are obliged to follow the rules below.

If you are a content/tutorial maker and would like to share this tutorial with others:

* You may **only** distribute this file amongst your audience (e.g. download links to this tutorial) if you give *reasonable credit* showing that this document was created by Dylan Rogers. *Reasonable credit* is defined as a message that cannot be missed, such as mentioning it when the content is on-screen (for videos), or adding a note in the main content section (for books).
* You must include this licence in all distributed versions.

If you fork and redistribute your own version of this:

* You must give credit that your version of the document is a fork of Dylan Rogers' original.
* You may share your content commercially or non-commercially, provided credit is given.
* You must include this licence in all publicly available versions.
* You must uncomment the comment at the beginning of this licence.
* The content must be correct - you must not **intentionally** provide misinformation (it's fine to make a few accidental mistakes, as long as you fix any problems when prompted).

General information:

* All code is free to use for both commercial and non-commercial products, no credit required.
* Any forks of this file should credit Dylan Rogers

Credited links:

[Video tutorials are available here](https://www.youtube.com/@open-project)  
[Dylan's YouTube channel](https://youtube.com/@dylancode)  
[Dylan's github](https://github.com/DylanRogers1)  

## Chapter 1: Intro to C++

One question many people have when they start programming in a low(er)-level language like C++ is *why?* Why would you spend all this time learning C or C++ when you could just choose a higher-level language instead? Well, the reason we use C++ is because it is really **powerful**.

**Powerful** means two things:

* Very fast (runtime is quick)
* Very extendable (you can do a lot, many features)

You will often here that C and C++ are both very fast. They're often used for programs such as video editors, web browsers, programming languages, operating systems, etc. The reason for this is that these languages are VERY fast!

C++ is very extendable, because we can do a lot with it. Languages like Python are limited by the fact it's very abstracted from the hardware. This makes it difficult to do anything low-level with these sort of languages - such as memory management. However, with C++, your knowledge of the language is the limit - you can do pretty much anything with it!

Anyway, let's get coding!

> Create a new file with the `.cpp` extension. I'll call mine `helloworld.cpp`.

Copy the following code into your C++ file:

``` cpp
#include <iostream>
int main()
{
  std::cout << "Hello world";
}
```

Great, now let's run our code! First navigate to the location the file is in. For example:

``` bash
dylan@open-project:~$ cd coding
dylan@open-project:~/coding$ cd learn
dylan@open-project:~/coding/learn$ cd c++
dylan@open-project:~/coding/learn/c++$ cd code
dylan@open-project:~/coding/learn/c++/code$ cd 1
dylan@open-project:~/coding/learn/c++/code/1$ 
```

Now we need to **compile** our code. We can do that using `g++`:

``` bash
g++ helloworld.cpp
```

> Note: If you don't have `g++` installed, you can install it using your package manager (such as `apt`). If you are on Windows, use the Visual Studio IDE to write C++ code - it's the easiest way to compile C++ code on a Windows machine.

Once our program has compiled, we can run it using the following command:

``` bash
./a.out
```

The above code executes the `a.out` file in the current directory. `a.out` is the executable program produced by the compiler.
