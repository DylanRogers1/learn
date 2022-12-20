
# The Ultimate Guide to Everything Python

*This tutorial was created by Dylan Rogers. It is owned and managed by [**The Open Project**](https://youtube.com/@open-project) and any attempt to redistribute or use this content must follow the [licence](#licence)*

## Contents

[Home](#the-ultimate-guide-to-everything-python)  
[Licence](#licence)

[Chapter 1: Hello world](#chapter-1-hello-world)  
[Chapter 2: Variables](#chapter-2-variables)  
[Chapter 3: Comments](#chapter-3-comments)  
[Chapter 4: User input](#chapter-4-user-input)  
[Chapter 5: Doing some maths](#chapter-5-doing-some-maths)  
[Chapter 6: Comparison operators](#chapter-6-comparison-operators)  
[Chapter 7: `if` statements](#chapter-7-if-statements)  
[Chapter 8: `else` statements](#chapter-8-else-statements)  
[Chapter 9: `elif`](#chapter-9-elif)  
[Chapter 10: `while` loops](#chapter-10-while-loops)  
[Chapter 11: `for` loops](#chapter-11-for-loops)  
[Chapter 12: Lists](#chapter-12-lists)  
[Chapter 13: List methods](#chapter-13-list-methods)
[Chapter 14: Functions](#chapter-14-functions)
[Chapter 15: Strings](#chapter-15-strings)
[Chapter 16: Tuples and sets](#chapter-16-tuples-and-sets)

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

[Back to contents](#contents)

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

[Back to contents](#contents)

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

[Back to contents](#contents)

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

[Back to contents](#contents)

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

[Back to contents](#contents)

# Chapter 5: Doing some maths

In this chapter, we'll learn about the arithmetic operators in Python. These operators will perform mathematical calculations, such as adding, multiplying, subtracting or dividing numbers.

> Key definition: **Operator** - a symbol in a programming language that, when given *operands*, does calculations and returns a value based on these operands.

## Adding

We can add numbers in Python using the `+` operator:

``` python
6 + 7
```

We could then store the result in a variable...

``` python
result = 6 + 7
```

... or we could just print it directly:

``` python
print(6 + 7)
```

Result:

``` text
13
```

> Note: In this tutorial, we will mostly be directly printing the results, however when building larger apps, it's good practice to store the result in a variable whenever you perform some sort of calculation.

## Subtracting

Just like with adding numbers, we can subtract them using the `-` operator:

``` python
print(18 - 6)
```

Result:

``` text
12
```

## Multiplying

Multiplying is done using the *asterisk* `*` operator:

``` python
print(4 * 5)
```

Result:

``` text
20
```

## Dividing

We can divide using the *forward slash* `/` operator:

``` python
print(32 / 4)
```

Result:

``` text
8
```

## Modulus

The modulo operator is a little confusing, so I'll try and explain it as well as I can.

Whenever you divide by a number, you get a remainder. For example, if I divide `14` by `3`, I'll have `4` with `2` left over. We can get this `2` by using the *modulo* operator.

We can get the modulus of a number using a percentage `%` sign.

The modulo operator works the exact same way as all the other operators. We divide the number on the left by the number on the right and then get the remainder:

``` python
print(7 % 3)
```

Result:

``` text
1
```

[Back to contents](#contents)

# Chapter 6: Comparison operators

In this chapter, we'll look at the different *boolean* operators in Python. Boolean operators compare things, to say whether they are equal, not equal, greater than, less than, etc. Boolean operators are really useful when dealing with **if** statements, which we'll get on to in the next tutorial.

## Equal to

One common mistake is to use a **single equals** sign `=` when comparing two things. Take the following code:

``` python
print(3 = 3)
```

This code is actually completely wrong. The reason is because a single equals `=` in Python represents the *assignment* operator. In other words, we are trying to set the value `3` to equal `3`. This doesn't really work... so Python gives us an error.

Instead, we need to use the **double equals** `==` operator. This compares the two values, and returns `True` if they are equal (`False` if they are not).

``` python
print(3 == 3) # prints 'True'
print(7 == 9) # prints 'False'
```

The output would be `True` because `3` is equal to `3`.

## Not equal to

The **not equal to** `!=` operator is the opposite of the **equal to** `==` operator. We can use it the same way as the `==` operator, except its output is reversed - `True` if they are different, `False` if they are equal.

``` python
print(7 != 14) # True because they are not equal
print(54 != 54) # False because they're the same
```

## Comparing strings

We can also compare strings (text). While it is technically possible to compare strings using the **less than** and **greater than** operators which we'll look at in a second, in this tutorial I'm just going to go in to how to compare strings using the **equal to** and **not equal to** operators.

``` python
print("Hello" == "World") # False as they are different
print("Bonjour" != "Hola") # True as they are different
```

## Less and greater than

Let's say we wanted to create a guessing game, where we would tell the user if their guess is too high or too low. To do that, we would need to know how to use the **less than** `<` and **greater than** `>` signs.

We can use the **less than** `<` sign to return `True` if the number on the left is smaller than the number on the right.

``` python
print(3 < 5) # True as 3 is less than 5
print(8 < 4) # False because 8 is not less than 4
```

Similarly, we can use the **greater than** `>` operator to return `True` only if the number on the left is bigger.

``` python
print(2 > 9) # False - 2 is not bigger than 9
print(4 > -2) # True - 4 is bigger than -2
print(88 > 88) # False - they are the same, the left is not bigger
```

## Less / greater than or equal to

Finally, there are two more comparison operators in Python - **less than or equal to** `<=` and **greater than or equal to** `>=`. Their name kind of explains what they do, so...

Less than or equal to:

``` python
print(3 <= 6) # True
print(5 <= 5) # True
print(7 <= -3) # False
```

Greater than or equal to:

``` python
print(8 >= 8) # True
print(3 >= 7) # False
print(9 >= 4) # True
```

[Back to contents](#contents)

# Chapter 7: `if` statements

`if` statements are where Python programming starts to get really fun. With `if` statements, we can ***branch*** our program and make it do different things depending on user input.  
Let's go through an example of using *conditions* in Python:

First, we'll ask the user to enter a password. We can do this with a simple `input` statement.  
Next, we'll compare the password to the user-entered password and see if it's correct.
If the password is correct, we'll display a nice message for the user.

Let's have a look at how we would go about coding this in Python:

``` python
guess = input("Guess the password : ")
if guess == "ilovepython123":
  print("You guessed the password correctly!!!")
```

Let's go over how this works.

Firstly, we ask the user to guess a password. We then store their guess in a variable named `guess`.

Next, we have an `if` statement. `if` statements allow us to do something **only** if a condition is true.  
To create an if statement, we use the `if` keyword followed by a condition. In our case, the condition is `guess == "ilovepython123"`.  
The condition checks whether the variable `guess` is equal to `"ilovepython123"`. If it is, it runs the code inside the `if` statement.

Finally, we have the `if` statement's *body*. The body of an if statement will only be run if the condition is `True`. We have to *indent* any code inside an if statement, as this shows Python that the code is part of the if statement. We can indent by adding a **tab** or **spaces** at the start of every line that is part of the if statement.

Let's have a look at another example of an if statement.

``` python
age = input("How old are you? ")
if age < 18:
  print("HELLO!!!")
if age >= 18:
  print("go away. now.")
```

In this program, we have `2` if statements. Firstly, if the user is under `18`, we print `HELLO!!!`, whereas if the user is `18` or over, we print `go away. now.`

However, it would be easier to use an `else` statement, so in the next chapter, we'll go over `if` ... `else` statements in Python.

[Back to contents](#contents)

# Chapter 8: `else` statements

We can optionally add an `else` clause to any Python `if` statement. Here's the syntax:

``` python
if condition:
  # do something
else:
  # do something else
```

The `else` keyword is just an add-on to the `if` statement. Have a look at this code:

``` python
age = input("How old are you? ")
if age < 18:
  print("HELLO!!!")
```

We could make the program do something else if the user is *not* under 18:

``` python
age = input("How old are you? ")
if age < 18:
  print("HELLO!!!")
else:
  print("go away. now.")
```

Notice this is similar to the program in the last chapter, we just substituted `if age >= 18` for `else`.

> The `else` statement runs if the `if` statement doesn't.

We don't need an `else` statement, but it's good to put one in so that the user always gets a response. There's one more 'add-on' for the if statement, known as the **else if**, or `elif` keyword. Let's learn about that!

[Back to contents](#contents)

# Chapter 9: `elif`

We can optionally add an `elif` keyword after an if statement. Take this code:

``` python
age = input("How old are you? ")
if age > 17:
  print("You are an adult!")
```

We could add an `else` statement:

``` python
age = input("How old are you? ")
if age > 17:
  print("You are an adult!")
else:
  print("You are a child!")
```

However I'd like to also check if the user was a teenager. We could of course do something like this:

``` python
age = input("How old are you? ")
if age > 17:
  print("You are an adult!")
else:
  if age > 12:
    print("You are a teenager!")
  else:
    print("You are a child!")
```

This code first checks if the user is an adult. If they are, we print `"You are an adult!"`.  
If the user is not an adult, we check if they are over 12 and say `"You are a teenager!"` if they are.  
The big thing here is that the teenager `if` statement is inside the adult's `else` statement. This is OK, but it makes it harder to read and we have to indent more.  
If they are not a teenager, we run the code in the teenager's `else` statement, which prints `"You are a child!"`.

This way of doing it is not *wrong*, but it isn't the best way of doing it. Instead, we should use an `elif` statement.

``` python
age = input("How old are you? ")
if age > 17:
  print("You are an adult!")
elif age > 12:
  print("You are a teenager!")
else:
  print("You are a child!")
```

What we are doing here is first checking if the user is an adult (just like before).  
If they are, print so, otherwise check if they are a teenager.  
If so, print it. If they are neither of these things, they are a child.

> You can have **multiple `elif` statements**. The code below is perfectly valid:

``` python
age = input("How old are you? ")
if age > 17:
  print("You are an adult!")
elif age > 12:
  print("You are a teenager!")
elif age > 2:
  print("You are a child!")
else:
  print("You are a baby, how can you even use the computer?!")
```

[Back to contents](#contents)

# Chapter 10: While loops

While loops are what we would call **condition-controlled** loops. This means that the code keeps repeating until a *condition* is met. As we learned in [this chapter](#chapter-6-comparison-operators), conditions are things that can evaluate to `True` or `False`. Let's look at an example of a `while` loop.

``` python
inp = "y"
while inp == "y":
  inp = input("Type 'y' to continue... ")
```

This program doesn't do much, but it shows how `while` loops can be used. We often use `while` loops when we don't know how many times the loop needs to run.

We can create a while loop using the `while` keyword. The syntax for a `while` loop is exactly the same as an `if` statement.

``` python
while condition:
  # repeated code
```

Python will repeat the body of a `while` loop until the condition is no longer `True`. This does, of course, mean that we get some weird outputs if the condition stays `True` forever...

``` python
while 3 < 5:
  print("3 is less than 5")
```

The above code is an example of an *infinite while loop*. Because `3` will always be smaller than `5`, Python doesn't know when it should stop running. The while loop runs forever.

Output:

``` text
3 is less than 5
3 is less than 5
3 is less than 5
3 is less than 5
3 is less than 5
3 is less than 5
3 is less than 5
3 is less than 5
3 is less than 5
3 is less than 5
...
(goes on forever)
```

Let's look at a different `while` loop.

``` python
x = 1
while x <= 12:
  print(x * 7)
  x = x + 1
```

Output:

``` text
7
14
21
28
35
42
49
56
63
70
77
84
```

This code works by first creating a variable named `x`. We initialise the variable with the value `1`.  
Next, we create a `while` loop and repeat while `x` is less than or equal to `12`.  
Inside the while loop we print the value of `x` times `7` (prints the 7 times tables).  
Finally, we increase `x` by `1` (we could have also typed `x += 1`) and the loop starts again.  
The loop keeps running until `x` reaches `13`, where it stops.

> A `while` loop works fine for this sort of thing, but a `for` loop would be better in this case. In the next chapter, we'll have a look at using `for` loops in our code.

[Back to contents](#contents)

# Chapter 11: For loops

Unlike `while` loops, `for` loops are what we call **count-controlled**. This means they ***iterate*** (go through) a list or range of numbers. We can predict how many times a `for` loop will run, which makes them useful for counting through a range of numbers.

Syntax of a `for` loop:

``` python
for item in my_list:
  # repeating code
```

I mentioned earlier that `for` loops are useful for counting through a range of numbers, but so far I have only mentioned that they can iterate through lists. There is a special function in Python that allows us to create a list, based on a range of numbers.

This function is called `range`.

``` python
for i in range(5):
  print(i)
```

The example above illustrates the use of the `range` function to create a list of numbers. We are actually iterating through the numbers `0` to `4` in the above example. Let's try to understand why by unpicking how the `range` function actually works.

## The `range` function

The `range` function is a useful, built-in function that allows us to create a list based on a range of numbers. There are lots of different parameters we can pass to the `range` function, so let's go over that now.

We can pass one argument (`a`) to get the values between `0` and `a` (exclusive).  
This means that we start at `0` and go up to `a`, but stop at `a` (`a` is not included).

Consider this code:

``` python
for i in range(10):
  print(i)
```

The code above would produce the following result:

``` text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> Remember: `10` is not included when calling `range(10)`.

We can also pass a starting point to the `range` function. Consider the code below:

``` python
for i in range(3, 9):
  print(i)
```

This code would print the integers between `3` and `8`:

``` text
[3, 4, 5, 6, 7, 8]
```

Finally, there is a third argument we can pass to `range`. Let's start at `2`, go up to `20` exclusive, and go up by `2` each time.

``` python
for i in range(2, 20, 2):
  print(i)
```

As you can see, the output to our code would be as follows:

``` text
[2, 4, 6, 8, 10, 12, 14, 16, 18]
```

The first argument (`2`) tells the `range` function that we are starting on 2.  
The second, `20`, tells Python to stop *before* it gets to `20`.  
Finally, the third argument represents the ***step***. You can think of this as how far Python steps each iteration. By default, this is `1` and `i` increased by `1` every time the loop runs. In our program, however, we set the step to `2`, so `i` increases by `2` each iteration (hence why we get the 2 times table printed out).

## Iterating through a range of numbers

The `range` function is used to allow iterating through ranges of numbers in a `for` loop. We've already created some `for` loops while we practised using `range`, so let's put them together and make a `range`-based `for` loop!

In a `for` loop, just replace where the list would be with the call to the `range` function. Here's an example:

``` python
for num in range(20, 50, 5):
  print(num)
```

You use the `for` keyword to define a `for` loop, which is then followed by a variable. You can call this variable whatever you'd like, and it stores the number of that iteration. After that, we use the `in` keyword, which we finish with either the name of a list, or a call to the `range` function.

## Iterating through a list

We haven't learnt about lists yet (we will literally in the next chapter, though!) so I'll keep this brief, but we can iterate through a list using this syntax:

``` python
for item in list_name:
  print(item)
```

Imagine we had an (incomplete) list of programming languages, stored in a variable called `langs`.

``` python
langs = ["python", "java", "c", "c++", "c#", "javascript", "rust"]
for lang in langs:
  print(item)
```

The above code would output the following:

``` text
python
java
c
c++
c#
javascript
rust
```

Let's go through why.

Firstly, we're creating a list. We'll cover creating lists in the next chapter, just know that a list is a group of different things.  
On line 2, we are iterating through the list. On every iteration, we store the current item in the list, whether that be *c*, *python*, *java*, or something else.  
Finally, we are printing the programming language to the screen.  
The loop goes through every item in the list, printing each one.

[Back to contents](#contents)

# Chapter 12: Lists

A list is just a group of data. For example, I could have a list of names, or a list of my favourite numbers.

## Creating lists

We can create a list in a similar way to a variable. Here is the syntax for creating a list:

``` python
list_name = [item_1, item_2, item_3, ...]
```

We start off by creating a variable to store the list in. In my program, I'll create a list of foods, so my list is called `foods`. We can indicate an empty list by using **square brackets** `[]`. Therefore, to create an empty list called `foods`, we would type the following code:

``` python
foods = []
```

That creates an empty list, but how would we add things to it? Well, one way of adding items to a list is by using the list's `append` method. I explain how to do that [later in this chapter](#adding-items-to-a-list), but we want to create a list that already contains **elements** (items). We can do this by putting items inside the square brackets.

``` python
foods = ["pizza"]
```

That's how to give a list a single value, but what if we wanted a list with multiple elements? That's kind of the point in a list, so let's do that!

We can create a list with multiple elements in it by seperating the elements with **commas** `,`. Consider this code:

``` python
foods = ["pizza", "curry", "pasta"]
```

This creates a new list called `foods` containing the elements `pizza`, `curry` and `pasta`.

The important thing to remember is that, if we overwrite the list, the original values will be deleted. Look at the code below:

``` python
foods = ["pizza", "curry", "pasta"]
foods = ["ice cream", "chocolate", "cake"]
```

The values `pizza`, `curry` and `pasta` will be overwritten by `ice cream`, `chocolate` and `cake`. If you need to add elements to a list, use [the `append` method](#adding-items-to-a-list).

## Printing lists

After we have created a list, it's easy to print the list to the console. Consider a list, called `name`, containing the elements `"Layla"`, `"Bob"` and `"Joe"`:

``` python
names = ["Layla", "Bob", "Joe"]
```

We can print `names` by simply calling the `print` function:

``` python
names = ["Layla", "Bob", "Joe"]
print(names)
```

Output:

``` text
["Layla", "Bob", "Joe"]
```

If you would like to print the list in an actual application, consider using a `for` loop:

``` python
names = ["Layla", "Bob", "Joe"]
for name in names:
  print(name)
```

Output:

``` text
Layla
Bob
Joe
```

## Accessing list elements

Every element (item) in a list has an ***index***. An index is just a position in the list. Indexes start from `0`, so the first element in any list will always have an index of `0`.

We can get a list element using the index. Below is shown the syntax for getting an element at a specific index:

``` python
list_name[index]
```

We could print the element using this syntax:

``` python
print(list_name[index])
```

Let's take our old list of names. We know that list indexes start from `0`, so the first element (Layla) will have an index of `0`. Below are shown the indexes of each element in the list.

* Layla (0)
* Bob (1)
* Joe (2)

We can access these elements using their index:

``` python
print(names[0]) # Layla
print(names[1]) # Bob
print(names[2]) # Joe
```

Another example:

``` python
countries = ["England", "USA", "Canada", "Nederland", "France"]
print(countries[2]) # Canada
print(countries[4]) # France
print(countries[3]) # Nederland
print(countries[0]) # England
```

> Always remember that list indexes start from `0`, not `1`.

We can change the value of an element using its index:

``` python
print(countries[3]) # Nederland
countries[3] = "The Netherlands"
print(countries[3]) # The Netherlands
```

Output:

``` text
Nederland
The Netherlands
```

This changes `"Nederlands"` to `"The Netherlands"`, but all other elements stay the same.

[Back to contents](#contents)

# Chapter 13: List methods

## Adding items to a list

We can add items to a Python list by using the `append` method. `append` is a method of every list, you don't need to create it.

``` python
fruits = ["apple", "raisin", "pineapple"]
print(fruits) # ["apple", "raisin", "pineapple"]
fruits.append("blueberry")
print(fruits) # ["apple", "raisin", "pineapple", "blueberry"]
```

In the above example, we first create a new list, called fruits. To begin with, we have exactly `3` elements in our list. On the third line, we add a new element, `blueberry`, to the list.

Another method we can use is `insert`. The main difference between `insert` and `append` is that, with `insert`, we can choose where the new element goes. Consider the following list:

``` python
food = ["pizza", "curry", "pasta"]
```

We *could* use the `append` method to add `lasagne` to the end of the list. However, let's imagine this list is in order of favourite foods - `pizza` is best, `pasta` is worst. I can't just insert it at the end of the list! Instead, I can use the `insert` method:

``` python
food = ["pizza", "curry", "pasta"]
food.insert(1, "lasagne")
print(food)
```

Output:

``` text
["pizza", "lasagne", "curry", "pasta"]
```

Let's break down this code. The first thing we are doing is calling the `insert` method on the `food` list. We are inserting `lasagne` at position `1`, meaning `lasagne` will now be at index `1`.

> Remember: When using the `insert` method, all existing elements after the inserted element get shifted, and their indexes change. In the above program, `curry` used to be at index `1` but was shifted to index `2`.

## Removing items from a list

Just like adding items, we can also remove list items. First, though, let's go over deleting and clearing an entire list.

We can delete an object using the `del` keyword. Consider the following example:

``` python
my_list = ["hello", "world", "python", "computer", "explosion"]
del my_list # my_list doesn't exist anymore
```

The above code deletes `my_list` from the face of the earth (well, the memory...)  
`my_list` can no longer be accessed, and it's memory space is cleared.

We can also delete a specific element from a list:

``` python
my_list = ["hello", "world", "python", "computer", "explosion"]
del my_list[2] # deletes index 2 ("python") from the list.
print(my_list)
```

Result:

``` text
["hello", "world", "computer", "explosion"]
```

Alternatively, we can clear the list by using the `clear` method.

``` python
my_list = ["hello", "world", "python", "computer", "explosion"]
print(my_list) # ["hello", "world", "python", "computer", "explosion"]
my_list.clear()
print(my_list) # []
```

Output:

``` text
["hello", "world", "python", "computer", "explosion"]
[]
```

> The `del` keyword deletes the actual list, instead of just clearing it. If you want an empty list, use the `clear` method.

If you know the value of the item you'd like to 'dispose' of, you can use the `remove` method.  
Let's imagine you really didn't want anyone named `Charlotte` to be your friend anymore:

``` python
friends = ["Anna", "Charlotte", "Emma", "Charlotte", "Charlotte"]
friends.remove("Charlotte") # No more Charlottes!
print(friends) # ["Anna", "Emma"]
```

And just like that, you've got rid of all the `Charlotte`s!

## Getting the length of a list

We can get the length of any list using the `len` function.

``` python
friends = ["Bob", "Billy", "Ben"]
friends_len = len(friends)
print("You have", friends_len, "friends!")
```

Output:

``` text
You have 3 friends!
```

In the above code, we are storing the length of `friends` as a variable, but we could just print it directly

``` python
friends = ["Bob", "Billy", "Ben"]
print("You have", len(friends), "friends!") # still prints 'You have 3 friends!'
```

We can also use the `count` method to do something similar, however I won't get into that now.

## Joining two lists together

We can join two lists together by using the `extend` method.

``` python
menu = ["Chips", "Pizza", "Curry"]
new_items = ["Pasta", "Soup"]
menu.extend(new_items)
print(menu)
```

Output:

``` text
Chips
Pizza
Curry
Pasta
Soup
```

As you can see, in the above example, we start with a menu of `3` things. We then *extend* the menu by adding the items from the `new_items` list.

[Back to contents](#contents)

# Chapter 14: Functions

This is another key point in our Python learning journey. Functions allow us to create ***reusuable code*** for our project.

Reusable code is where you can create a function to do something, and then call that function multiple times. This makes our code easier to read (and we don't have to type as much!)

We can create a function using this syntax:

``` python
def function_name():
  # code
```

Let's create a function called `say_hello`:

``` python
def say_hello():
  print("Hello!")
```

I'll break down what's going on here.

We create a function using the `def` keyword. The name of the function is `say_hello`. The *body* of the function (the code) prints `"Hello!"`.

We can call our function by typing `say_hello()`:

``` python
def say_hello():
  print("Hello")

say_hello()
```

Output:

``` text
Hello!
```

> There are two benefits of using functions. It makes writing code easier, as you don't need to write the same thing over and over again. It also makes changing code easier, as you just need to change it in one place, and it changes everywhere.

## Function parameters

**Parameters** and **arguments** are often used interchangebly, but there is a difference. When we call a function, the data we give is called an argument. In the code `print("Hello world")`, `"Hello world"` is an argument. A parameter is what the function gets, and we'll discuss parameters now.

We can write the parameters name *inside* the brackets `()` after the function name:

``` python
def say_hello(arguments_go_here):
  print("Hello")
```

Let's say we wanted to accept one argument - the user's **name**. We could do this using the following code:

``` python
def say_hello(name):
  print("Hello")
```

We can then use the value of `name` as if it were a variable:

``` python
def say_hello(name):
  print("Hello", name)
```

Now that we have a working `say_hello` function, let's call it!

``` python
def say_hello(name):
  print("Hello", name)

say_hello("Bobby")
say_hello("Billy")
say_hello("Ben")
```

Output:

``` text
Hello Bobby
Hello Billy
Hello Ben
```

As you can see, our function works! Now let's look at *returning* data.

## Returning data from a function

Think back to the `input` function - `input` returns data. When we say return data, we mean give information back to the *caller*. Here's how to do it in Python, using an example `greet` function:

``` python
def greet():
  print("Hello")
  name = input("What is your name? ")
  return name
```

The greet function says `Hello`, asks for the user's name and then returns that name.

The final line is the important line. We use the `return` keyword to return a value from a function. To the right of `return`, we type the value that we want to return (in this case, we return the value of `name`).

We can then use this function just like the `input` function. Here's an example:

``` python
def greet():
  print("Hello")
  name = input("What is your name? ")
  return name

username = greet()
print("Hello", username)
```

Output:

``` text
Hello
What is your name? Dylan
Hello Dylan
```

[Back to contents](#contents)

# Chapter 15: Strings

## String literals

We've seen string literals before, but let's start by going over what a **string literal** actually is.

A literal is just a value that never changes. Consider the following program:

``` python
print("Hello world")
```

In the above program, `"Hello world"` is a string literal. It's a literal because it never changes - whenever we run our program, it will **always** print `"Hello world"`.

A **string** is just a sequence of characters. In other words, it's just some text. Strings can contain numbers, symbols, letters, etc.

We can create a string literal by surrounding text in single `'` or double `"` speech marks.

``` python
"This is a string literal"
'This is also a string literal'
This is not a string
```

## Accessing elements in a string

A string is technically just an array (like a list). This means we can do all sorts of fancy operations on strings. One such operation is accessing a single element (character) of the string. Below is an example of accessing element in a string.

``` python
string = "The quick brown fox jumps over the lazy dog"
print(string[3]) # prints 'q'
```

However, the issue with accessing specific characters of a string is that we can't actually change the letters individually, like we can with list elements. This is because strings are *immutable*, which I won't get into in this chapter. Just know that strings cannot be changed.

## Checking if a string contains a substring

We can check if a substring is present in a string by using the `in` keyword.

``` python
string = "The quick brown fox jumps over the lazy hog"
if "hog" in string:
  print("hog is in string")
if "d" not in string:
  print("d is no longer in string!")
```

Output:

``` text
hog is in string
d is no longer in string!
```

Python checked to see if the word '`hog` was in the string, which it was, so the `if` statement ran.

## Getting the length of a string

Because strings are just arrays, we can get the length of a string using the `len` function:

``` python
string = "The quick brown fox jumps over the lazy dog"
print(string, "contains", len(string), "letters.")
```

Output:

``` text
The quick brown fox jumps over the lazy dog contains 43 letters.
```

The `len` function will return the number of characters (letters/numbers/symbols) in a string, just like it returns the number of elements in a list.

## Multi-line strings

We can actually create what's called a **multi-line string** in Python. As the name suggests, this is a string that spans multiple lines. We can create a multi-line string using the following syntax:

``` python
string = """Text
Goes
Here"""
```

Let's do an example!

``` python
"""Author: Dylan Rogers
Date: 20/12/2022
Title: Program involving strings
Description: This is my awesome program! I used a multi-line string in it!"""
```

We could then store the string like this:

``` python
info = """Author: Dylan Rogers
Date: 20/12/2022
Title: Program involving strings
Description: This is my awesome program! I used a multi-line string in it!"""
```

And then print that variable out:

``` python
info = """Author: Dylan Rogers
Date: 20/12/2022
Title: Program involving strings
Description: This is my awesome program! I used a multi-line string in it!"""

print(info)
```

Output:

``` text
Author: Dylan Rogers
Date: 20/12/2022
Title: Program involving strings
Description: This is my awesome program! I used a multi-line string in it!
```

> You may remember multi-line strings from when we were learning about [comments](#chapter-3-comments)!

## Iterating through a string

Because strings are arrays, we can loop through them using a `for` loop. The program below prints each character of the string `"I like python"`:

``` python
msg = "I like python"
for letter in msg:
  print(letter)
```

Output:

``` text
I

l
i
k
e

p
y
t
h
o
n
```

The above code iterates through each letter of the `msg` variable: `I`, `(space)`, `l`, `i`, `k`, `e`, `(space)`, `p`, `y`, `t`, `h`, `o` and `n`

## Slicing strings

We can slice strings in exactly the same way as slicing lists.

``` python
msg = "Hello world"
print(msg[6:])
# prints 'world'
```

``` python
msg = "My friend Bob"
print(msg[:-4])
# prints 'My friend'
```

``` python
msg = "The quick brown fox jumps over the lazy dog"
print(msg[4:19])
# prints 'quick brown fox'
```

> We will learn much more about slicing lists in a future chapter. Don't worry if you don't understand this code at the moment.

## String methods

We can turn a string into lowercase by using the `lower()` function:

``` python
string = "Hello World"
lstring = string.lower()
print(lstring)
```

Output:

``` text
hello world
```

We can also turn a string into all uppercase:

``` python
string = "Hello Bob!"
ustring = string.upper()
print(ustring)
```

Output:

``` text
HELLO BOB!
```

We can also turn a string into titlecase:

``` python
string = "mysterious programming language, named python, emerges."
tstring = string.title()
print(tstring)
```

Output:

``` text
Mysterious Programming Language, Named Python, Emerges.
```

We can also check if a string is all lowercase, using the `islower()` method:

``` python
string = "hello world"
if string.islower():
  print(string, "is lowercase")
```

Output:

``` text
hello world is lowercase
```

Check if a string is all uppercase, using the `isupper()` method:

``` python
string = "I LOVE PROGRAMMING SO MUCH"
if string.isupper():
  print(string, "is uppercase")
```

Output:

``` text
I LOVE PROGRAMMING SO MUCH is uppercase.
```

Finally, check whether a string is titlecase, using the `istitle()` method:

``` python
string = "Python: The Greatest Programming Language"
if string.islower():
  print(string, "is lowercase")
```

Output:

``` text

```

> Nothing is printed because `Python: The Greatest Programming Language` contains a symbol (`:`). This stops it being titlecase.

There are also a few other methods, however this chapter is really, really long, so I'll stop it here!

[Back to contents](#contents)

# Chapter 16: Tuples and sets

## Tuples

Like lists, **tuples** are a type of array. The main difference between a tuple and a list is that tuples are ***read-only***. This means that, once we've created the tuple, we can't change the values.

Creating a tuple:

``` python
my_tuple = (item_1, item_2, item_3, ...)
```

We can access the elements in a tuple the same way as we would access those of a list:

``` python
person = ("Billy", 22, "Male", "19/02/2000")
print(person[2])
```

Output:

``` text
Male
```

However, if we try to modify one of the elements:

``` python
person = ("Billy", 22, "Male", "19/02/2000")
person[1] = 23
```

We get an error.

``` text
Exception has occurred: TypeError
'tuple' object does not support item assignment
```

If you need to modify the tuple later, use a list instead, or convert the tuple to a list using the `list()` class.

## Sets

Sets are also like lists, but they are not ordered.
