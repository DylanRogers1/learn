
# JavaScript: Bring Your Websites To Life

*This tutorial was created by Dylan Rogers. It is owned and managed by [**The Open Project**](https://youtube.com/@open-project) and any attempt to redistribute or use this content must follow the [licence](#licence). Find out more at [123web](http://123web.uk)*

## Contents

[Home](#javascript-bring-your-website-to-life)  
[Licence](#licence)

[Chapter 1: Welcome to JavaScript](#chapter-1-welcome-to-javascript)
[Chapter 2: Variables](#chapter-2-variables)

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

[Video tutorials are available here](https://www.youtube.com/@dylancode)  
[Dylan's YouTube channel](https://youtube.com/@dylancode)  
[Dylan's github](https://github.com/DylanRogers1)  

[Back to contents](#contents)

# Chapter 1: Welcome to JavaScript

Welcome to JavaScript! JavaScript let's us bring our websites to life - it's the programming language of the web!

> Note: From now on, I'll refer to **JavaScript** as **JS**.

To get started, create a new HTML file. I'll call my file `hello.html`. Inside this file, paste the following code:

``` html
<!DOCTYPE html>
<html>
  <head>
    <title>Hello JavaScript</title>
  </head>
  <body>
    <h1>Welcome to JS!</h1>
    <script src="scripts/main.js"></script>
  </body>
</html>
```

> Please note: This is not an HTML tutorial, and so I won't explain how this code works. It's recommended that you have a basic understanding of HTML, even if you've only ever built a very basic page.

The important part of the code is `<script src="scripts/main.js"></script>`. This imports a JS file, and any code inside that file we be executed.

In the same folder as your HTML file, create a new folder called `scripts`. This is where we will write all our JavaScript code. Inside the `scripts` folder, create a new file, called `main.js`.

Inside `main.js`, we'll write a basic hello world program:

``` js
console.log("hello");
```

We'll go through how the code works in a second, but let's focus on running our code. To run the JS, just open the HTML file in a web browser.

Open the console by pressing `F12` and clicking `Console`. You should see the following output in the console:

``` text
hello
```

You've just created your first JavaScript program! Let's go through how the following line of code works:

``` js
console.log("hello");
```

The `console` object is used to output text to the developer console. The `console` object contains a method called `log`. The `log` method is used to print text to the console. We call `console.log` by typing `console.log()`, and we pass a string (`"hello"`) as an argument. This prints `hello` to the console window. Note that you should always use a semicolon after every JS statement. It's not required, but it's recommended.

> We'll learn about more about different ways of outputting text in the [Output](#chapter-3-output) chapter.

That's all for this chapter. In the next chapter, we'll learn about how we can create **variables** - store data!

# Chapter 2: Variables

## Creating (declaring) variables

We can create a variable in JS using the `let` keyword:

``` js
let x;
```

The example above creates a new variable called `x`. The variable doesn't currently have a value, so let's give it one!

## Setting (initialising) variables

We can set the value of a variable using the `=` (**assignment**) operator:

``` js
let x;
x = 3;
```

As you can see, we first start by declaring a variable named `x`.  
On the next line, we initialise this `x` variable using the **assignment** (`=`) operator. We give it the value `3`.

We can combine both of these operations into one line:

``` js
let x = 3;
```

## Reading variables

We can read variables in JS by simply writing the name of the variable:

``` js
console.log(x);
```

The entire code would be as follows:

``` js
let x = 3;
console.log(x);
```

Output:

``` text
3
```

## Creating variables in different ways

So far, we have looked at one way of creating variables - using the `let` keyword. There are actually 3 more:

* Using the `var` keyword
* Using the `const` keyword
* Not using a keyword

Let's first look at the `let` keyword.

Whenever we declare a variable using the `let` keyword, we can **only** use that variable in the current code block.

> We will learn more about code blocks and scopes when we learn about conditions and loops.

For example, the following code will result in an error, because `a` was defined inside a code block:

``` js
{
  let a = 35;
}
console.log(a);
```

Output:

``` text
Uncaught ReferenceError: 'a' is not defined
```

Because `a` was defined as a local variable (inside a code block), it doesn't exist outside of that scope (outside the code block).

Now let's look at the `var` keyword.

`var` allows us to create a variable for the function. Basically, if we declare a function using the `var` keyword, we can only use the variable in the current function.

``` js
if (4 + 3 == 7)
{
  var x = 27;
}
console.log(x);
```

The above code would run successfully, because we declared the `x` variable using the `var` keyword. When we declare using `var`, we can use that variable in the entire function, but not outside the function. For example, if we declare a variable inside an `if` statement, we can use the variable outside of the `if` statement, but not outside of the function.

Using `const`:

The `const` keyword is exactly the same as `let`, however we cannot change the variable afterwards. The below code will result in an error, because we try to change the value of a constant:

``` js
const x = 82;
x = 322;
```

``` text
Uncaught TypeError: invalid assignment to const 'x'
```

Remember that we cannot change the value of a variable declared using `const`.

Using no keyword:

We can declare a variable using no keyword (just the assignment operator).

``` js
x = 13;
```

This variable becomes a **global** variable (we can use it everywhere, even outside the function).

That's a lot of information, so I'll summarise it into this table:

| **Keyword** | **Definition**                                                          |
| :---------: | :---------------------------------------------------------------------: |
| `let`       | Creates a **local** variable (only available in the current code block) |
| `var`       | Creates a variable that is available throughout the entire function     |
| `const`     | Creates a **local** variable that cannot be changed (is constant)       |
| No keyword  | Creates a **global** variable (available everywhere)                    |

# Chapter 3: Output

I wanted to dedicate this chapter to be all about different ways of outputting data. There are a few ways of doing this, and it should help get us away from boring console apps!

## Outputting data using `console.log`

One way of outputting data is by using the `console.log` method. We can use this method to print text to the console. The console is the window that we can open using `F12`.

To use `console.log`, use the following syntax:

``` js
console.log("Enter text here...");
```

For example, to print `Guten Morgen!` to the console, you would type this:

``` js
console.log("Guten Morgen!");
```

## Outputting data using `document.write`

Another way of outputting data is using the `document.write` method. This writes some text to the screen.

``` js
document.write("hello");
document.write("world");
```

Output:

``` text
helloworld
```

## Changing HTML elements

The most interesting way of outputting data is by modifying HTML data.
