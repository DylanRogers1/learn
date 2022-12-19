
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

## Setting variables

Unlike many other languages you don't need to create variables before you give them a value. Instead, we can give the variable a value whenever, even if it doesn't exist yet!

We can assign a variable like this:

``` python
variable_name = value
```

For example, we could set the variable `country` to be equal to `"India"` by typing this:

``` python
country = "India"
```

## Reading variables

To read a variable, you can literally just type the variable's name! If you want to print a variable, just use this syntax:

``` python
print(variable_name)
```

For example, let's say I had a variable called `favourite_programming_language` and that variable had the value `"Python"`. I could print my favourite programming language to the console by typing:

``` python
print("My favourite programming language is:")
print(favourite_programming_language)
```

Which would output:

``` text
My favourite programming language is:
Python
```

Then if I were to change the value of `favourite_programming_language` to equal `"Java"`, the output would become:

``` text
My favourite programming language is:
Java
```

# Chapter 3: Comments

I wanted to dedicate a chapter to something called comments. Comments are quite important, as they allow us to explain our code to... ourselves.  
You might not think of it, but once you've had a break from working on your program, you probably won't remember what on earth half of your code means.  
Comments allow us to write notes about our program and explain what our code means.

We can write a Python comment by starting the line with a hashtag **#**. Anything afterwards will be completely ignored, up until the end of the line.

Let's have a look at this code:

``` python
a = 17
b = "Billy"
c = "Winter"
```

If you gave me this code, I wouldn't have a clue what `a`, `b` and `c` mean. We can make this a lot better using comments:

``` python
# 'a' is the age of the user
a = 17
# 'b' is the username
b = "Billy"
# 'c' is the user's favourite season
c = "Winter"
```

There, much easier to understand!  
This isn't actually a great use of comments, though. Instead, we should use comments to explain complicated code, not explain what variables are.

> It's important to remember that comments are not a solution to bad variable naming. You should always name variables descriptively. You should also always try to make code readable, comments don't fix code.

We can also add comments to the end of the line:

``` python
print(name) # Output: "Dylan Rogers"
```

Most languages have a feature known as *multi-line comments*. These are comments that span multiple lines, and they are often used to explain big things, such as licences.  
In C-based languages, these are often indicated using the `/*` and `*/` operators. Anything in between will be ignored.  
Python, however, does not really have multi-line comments.

We have to tweak it a little to get multi-line comments working in Python.  
We could, of course, just start each line with a hashtag:

``` python
# This is my program!!!
# Pwease do not copwy it...
# Date: 18/12/2022
# Author: Dylan Rogers
```

However, this can take a while if you have lots of lines to comment. Instead, we can use `"""` to create a multi-line comment:

``` python
"""
This is my program!!!
Pwease do not copwy it...
Date: 18/12/2022
Author: Dylan Rogers
"""
```

What we are actually creating here is a multi-line string, however this string is not attached to anything (it isn't used) and so Python ignores it.  
As I said, it's a bit of a work-around, but it's pretty widely accepted as a valid way of commenting code!

# Chapter 4: User input

We can get user input in Python using the `input` function. Just like `print`, `input` is a built-in function. The two functions are kind of the opposite, with `print` giving output and `input` getting input. We can use them together to make a cool program:

``` python
print("Enter your name...")
name = input()
print("Hello", name)
```

Let's now go through this code, as there are a few things we haven't covered yet.

On line 1, we are simply prompting the user to type in there name.

Line 2 is the important line. We call the `input` function, which allows the user to type in some text. The `input` function *returns* the text the user types.  
When a function *returns* data, we mean that it sends some information back to us. In our case, the information is the text the user entered.  
We store the text that was entered by the user in a variable called `name`, so `name` now stores the value **Dylan** (or whatever the user typed in).

Finally, line 3 prints `"Hello {name}"`, where `{name}` is the name the user typed in.  
You may notice that we passed *2* arguments to `print` instead of just *1*. That's because we can give multiple strings to the `print` function and it will join them together (and print them all).

It's really that simple! All we need to do to get user input is to call the `input` function and store its value in a variable! There's a different way of doing it, though.

Just like `print`, `input` can actually take in arguments, it's just not required. Instead of writing this code:

``` python
print("How old are you? ")
age = input()
```

We could simply write this:

``` python
age = input("How old are you? ")
```

That's because the `input` function can take in arguments (information) if you want it to. Whatever we pass to `input` will be the question prompt asked to the user. This is useful as it allows us to get user input in one line of code instead of two. Another reason this is good is because it doesn't go onto a new line, and so the user can type their answer on the same line as the question.

# Chapter 5: Doing some maths

In this chapter, we'll learn about the arithmetic operators in Python. These operators will perform mathematical calculations, such as adding, multiplying, subtracting or dividing numbers.

> Key definition: **Operator** - a symbol in a programming language that, when given *operands*, does calculations and returns a value based on these operands.

## Adding numbers

We can add numbers in Python using the `+` operator:

``` python
a + b
```

We could then store the result in a variable...

``` python
result = a + b
```

... or we could just print it directly:

``` python
print(a+b)
```

> Note: In this tutorial, we will mostly be directly printing the results, however when building larger apps, it's good practice to store the result in a variable whenever you perform some sort of calculation.

## Subtracting numbers

Just like with adding numbers, we can subtract them using the `-` operator 
