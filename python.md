
# The Ultimate Guide to Everything Python

*This tutorial was created by Dylan Rogers. It is owned and managed by [**The Open Project**](https://youtube.com/@open-project) and any attempt to redistribute or use this content must follow the [licence](#licence)*

## Licence

<!-- **This content is a fork of the original by Dylan Rogers. Please abide by the licence.** (uncomment this line if your document is a fork of my document) -->

If you are *not* redistributing this file (in other words, you are just a reader and this file will stay on your computer, you will not send it to anyone):

* You may use the skills learned in this book for personal, commercial or non-commercial projects
* As long as you do not share the document, you may use it however you would like to.
* If you share the document, you are obliged to follow the rules below.

If you are a content/tutorial maker and would like to share this tutorial with others:

* You may **only** distribute this file amongst your audience (e.g. download links to this tutorial) if you give *reasonable credit* showing that this document was created by Dylan Rogers. *Reasonable credit* is defined as a message that cannot be missed, such as mentioning it when the content is on-screen (for videos), or adding a note in the main content section (for books).
* You must include this licence in all distributed versions.

If you fork and redistribute your own version of this:

* You must give credit that your version of the document is a fork of Dylan Rogers' original.
* You may share your content commercially or non-commercially, provided credit is given.
* You must include this licence in all publicly available versions.
* You must uncomment the comment at the beginning of this licence.

General information:

* All code is free to use for both commercial and non-commercial products, no credit required.
* Any forks of this file should credit Dylan Rogers

Credited links:

[Video tutorials are available here](https://www.youtube.com/@dylancode)  
[Dylan's YouTube channel](https://youtube.com/@dylancode)  
[Dylan's github](https://github.com/DylanRogers1)  

# Chapter 1: Hello world

First of all, download the latest version of Python [here](https://python.org).

Once you have Python installed, open a new file with the `.py` extension. You could open it in a text editor of your choice, such as *VS Code*, a Python IDE or just Python's built-in *IDLE* editor. I'll name my file `hello.py`.

Inside `hello.py`, type this code:

``` python
print("Hello world")
```

Now, run your code. You should see `Hello world` printed to the console:

``` text
Hello world
```

Let's briefly go through how this line works.

In our code, we are calling the `print` function. To call a function, we add `()` after the function name. Therefore, to call `print`, we type `print()`.  
A function is just a group of code that executes when the function is called. In our case, the `print` function prints some text to the screen whenever it is called.

We can *pass arguments* to a function. This means we are giving *data* to the function. When we call `print`, we can give it some text (a *string*) which it will print to the screen.

# Chapter 2: Variables

Variables are a key part of any programming language. They allow you to store data for later.  
An example of a variable would be `age`, which could store an *integer*, such as `82`.  
The key thing about variables is that its data can change. `age` could later become `83`, for example.


