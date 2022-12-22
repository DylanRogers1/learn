
# Java: Beginner To Advanced

*This tutorial was created by Dylan Rogers. It is owned and managed by [**The Open Project**](https://youtube.com/@open-project) and any attempt to redistribute or use this content must follow the [licence](#licence). Find out more at [123web](http://123web.uk)*

## Contents

[Home](#java-beginner-to-advanced)  
[Licence](#licence)

[Chapter 1: Hello world](#chapter-1-hello-world)

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

# Chapter 1: Hello world

In this chapter, we'll create a hello world program in Java! Hello world programs are a little longer in languages like Java than they would be in languages like Python (Python tutorial available [here](https://github.com/DylanRogers1/learn/blob/master/python.md)) but we'll go through each line of code, so hopefully you'll be a Java expert before we even finish the chapter!

First thing to do is create a new Java class file. If you're using a Java IDE (such as [eclipse](https://eclipse.org)) it should be self-explanatory. I'm going to call my class file `Hello.java`, however you can name yours whatever you like, as long as it has the `.java` extension.

I'd also recommend creating a new folder for your Java project. I'll call mine `learn`, but yours can be whatever. I'm going to go a bit further and create a package (folder) inside my project folder, called `helloworld`. I'll create a new package for each chapter.

My folder structure:

``` text
learn
└── helloworld
    └── Hello.java

```

Inside `Hello.java` (or whatever your class is called), add the following code:

``` java
public class Hello
{
  public static void main(String args[])
  {
    System.out.println("Hello, World!");
  }
}
```
