# Chapter 1: Hello World

Hi, welcome to The Open Project! In this video, we'll be going through the very basics of Python. We'll create a python program that prints "Hello world" to the console!

First, I want to really quickly discuss the document in front of me at the moment. Just so I don't babble on about the same thing for half an hour, I made a little document to go along with this tutorial. If you'd like to have a look at it, I'll leave a link to my GitHub page in the description, so you can have a look for yourself! Also, if you're a content creator, feel free to use this file to help you make your own Python tutorial - which you may find useful as you don't have to create 100% of the content yourself! Have a look at the document, it explains it all there.

I've also written a script for this tutorial, so feel free to read through that if you prefer reading articles to watching videos. The script will be on my GitHub, alongside the Python document, so you should be able to follow along if it helps. I also added custom subtitles to the video in lots of different languages, so check that out if you like subtitles! Anyway, I'm going on at this point, so let's get coding.

The first thing we want to do is to install Python. I'll leave a link in the description to download it. If you use Linux like me, just use your package manager to install `python3`. On Windows or MacOS, download the latest version at https://python.org. Once Python is installed, create a new Python file. A Python file has the `.py` extension. In my program, I'll create the `hello.py` file. Open this file in a text editor of your choice - VS Code, an IDE or just IDLE, the built in Python IDE.

Great - now the boring stuff is out the way, it's time to start programming! Inside `hello.py` (or whatever your Python file is called) copy the following code:

`print("Hello world")`

We can then run our code using the terminal. Open a new terminal and navigate to the folder containing the Python program. Once inside that folder, use the `python3` command to execute our code. In my case, I would type `python3 hello.py`. Note that on some devices - particularly Windows computers - `python3` is installed as `python` or `py`. Try all three commands and use the one that works! When we run our code, we get `Hello world` printed to the console!

Now we've successfully written and executed our code, let's explain what it all means. 

First we start by calling the `print` function. A function is basically a block / group of code that executes when we call it. In our case, when we call the `print` function, Python prints some text to the screen. We can call a function using by adding a pair of brackets `()` to the end of a function name. In our case, we call the `print` function by typing `print()`.

Inside these brackets we can add data, known as arguments. In our program, we pass "Hello world" as an argument. "Hello world" is what we call a string, which is basically just text. When we call `print`, it will print the given text to the console (terminal).

Just remember - never call arguments 'parameters', because Python developers will never forgive you.

Thanks for watching!

# Chapter 2: Variables

Hey, welcome back to The Open Project! Today we'll be looking at variables, which are a key part of pretty much every language.

Variables allow us to store data for later. In the document, I give an example variable called `age`. The value of age is initially 82 (an integer / whole number). Later on, we could change the value of age to be 83 instead of 82. This is the important thing with variables - they can change.

First, let's talk about how to define and assign variables. But first - what do these two terms mean? Whenever we say the word 'define', we basically mean 'create'. If we define a variable, we create it. This is different to 'assign', which basically means 'set'. If we assign a value to a variable, we set the variable to the value.

Python is what we call a 'dynamically-typed' language. This means that we don't need to give variables a type. We can also just assign a variable whenever we like - it doesn't have to exist. Let's look at the syntax of assigning a variable.

To assign a variable, we need to use the 'assignment' operator. The assignment operator is a single equals sign (=). First, we type the variable name. This could be anything - age, name, favourite_colour, birthday, etc. We then put an equals sign (=), followed by the value. In the example below, we create a variable called country and assign it the value "Brazil". We do this using the code `country = "Brazil"`. 

Now let's have a look at reading a variable. Whenever we access a variable in Python, just type the variable name! For example, to print a variable, we type `print(variable_name)`. Let's imagine we had a variable called 'favourite_programming_language'. We could print the value of 'favourite_programming_language'  by typing `print(favourite_programming_language)`. When we run this example code, it prints "My favourite programming language is: Python". As I mentioned earlier, variables can change - they can vary.

Imagine we changed the value of 'favourite_programming_language' to equal "Java". The output would then change.

Great - now you're an expert at variables in Python! Just remember not to use symbols in your variable names, or your computer will explode.

Thanks for watching!

# Chapter 3: Comments

Hello again, welcome to The Open Project! Thanks for sticking around, by the way. Most people quit after episode 2, so congratulations, and I really appreciate it!

This video is going to be dedicated to something known as comments. Comments allow us to explain what our code does. In fact, the main use of comments is to explain our own code... to... ourselves??!! The thing is, programming is complicated. Once you've stopped working on something for a while, you won't have a clue what any of it means. Comments fix this problem, by allowing us to write notes and explaing our code.

To create a comment, start the line with a hashtag. After the hashtag, everything is ignored, up until the end of the line. In this example code, we have a load of really badly named variables. One way of making this better is using comments. Below I used a comment to indicate the meaning of each variable.

However, I really don't like this code. I mention it below - this is a terrible use for comments. While yes - this does make the code slightly more understandable, I can't stress this enough: COMMENTS DON'T FIX CODE! Lazy programmers will write bad code and use comments to fix it. Besides, you shouldn't use comments to explain variables, you should use comments to explain large chunks of code. Even with the comments, this is still terrible code. Instead, we should consider the variable names 'age', 'username' and 'favourite_season'.

We can also add comments to the end of a line. In this code, 'print(name)' will be treated as normal code (because it's before the hashtag), but anything after the hashtag (`Output: "Dylan Rogers"`) will be ignored. This use of comments to tell us the output is common in many tutorials.

The thing that's different with Python is its use of multi-line comments. Many languages - whether that be Java, C, C++, etc. - use C-style comments. C-style comments allow us to create a single-line comment using a double slash (//), or a multi line comment using /* and */. However, Python doesn't support C-style comments. This means that multi-line comments aren't directly supported. However, there is a workaround. If we create a multi-line string, python will ignore it, and so we have essentially created a multi-line comment. The code on-screen shows an example of a multi-line string being used as a multi-line comment.
