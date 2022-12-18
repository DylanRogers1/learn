
# Create your own GUI apps in Python!

[Video tutorials are available here](https://www.youtube.com/playlist?list=PLXQkLoBydcA5uOPQC5vx65xnXgVcwW4Yz)  
[Dylan's YouTube channel](https://youtube.com/@dylancode)
[Dylan's github](https://github.com/DylanRogers1)

*This tutorial was created by Dylan Rogers. It is owned and managed by [**The Open Project**](https://youtube.com/@open-project) and any attempt to redistribute or use this content must follow the [license](#license)*

## License

<!-- This content is a fork of the original by Dylan Rogers. Please abide by the license. (uncomment this line if your document is a fork of my document) -->

If you are *not* redistributing this file (in other words, you are just a reader and this file will stay on your computer, you will not send it to anyone):

* You may use the skills learned in this book for personal, commercial or non-commercial projects
* As long as you do not share the document, you may use it however you would like to.
* If you share the document, you are obliged to follow the rules below.

If you are a content/tutorial maker and would like to share this tutorial with others:

* You may **only** distribute this file amongst your audience (e.g. download links to this tutorial) if you give *reasonable credit* showing that this document was created by Dylan Rogers. *Reasonable credit* is defined as a message that cannot be missed, such as mentioning it when the content is on-screen (for videos), or adding a note in the main content section (for books).
* You must include this license in all distributed versions.

If you fork and redistribute your own version of this:

* You must give credit that your version of the document is a fork of Dylan Rogers' original.
* You may share your content commercially or non-commercially, provided credit is given.
* You must include this license in all publicly available versions.

General information:

* All code is free to use for both commercial and non-commercial products, no credit required.
* Any forks of this file should credit Dylan Rogers .

Credited links:

[Video tutorials are available here](https://www.youtube.com/playlist?list=PLXQkLoBydcA5uOPQC5vx65xnXgVcwW4Yz)  
[Dylan's YouTube channel](https://youtube.com/@dylancode)
[Dylan's github](https://github.com/DylanRogers1)

---

---

---

---

# Chapter 1: Creating a window

This is the first tutorial on how to create Python GUIs. GUIs are graphical apps (as opposed to console apps) and they often consist of elements such as buttons, textboxes, images and videos. They are a lot more fun to create than console apps, so hopefully this tutorial will be a lot of fun!

Prerequisites:

* You should know a little about the Python programming language in order to understand how each part of the code works.
* Knowing Python is not required, however it will help you understand the syntax of things.

To start off, type this code into a Python file:

``` python
import tkinter as gui
root = gui.Tk()
gui.mainloop()
```

If we run this code, we get the following output:

![|--- Code output cannot load ---|](res/1.png)

Let's go through the code line-by-line.

``` python
import tkinter as gui
```

This line imports the `tkinter` library. This library allows us to build graphical user interfaces (GUIs), and it's the library we'll be using throughout this course.  
We give the library the name `gui`, so we can reference it later using that name. Other tutorials may import the `tkinter` library as `tk`, but I think it makes more sense to name it after what it does - helping us make GUI applications.

``` python
root = gui.Tk()
```

This line creates a new instance of a tkinter window. This will display a new empty window.  
If you imported tkinter under a different name, such as `tk`, type `tk.Tk()`.

``` python
gui.mainloop()
```

Finally, we are running the loop for the window. This keeps the window on screen, as otherwise it would disappear as soon as it was created, which is not what we want.

There you are - your first window! It doesn't really do much though, so in the next chapter we'll look at labels and how we can use them to display text on our new window!

# Chapter 2: Labels

Labels are just text that we can put onto our window. In tkinter, we can creating a label using this code:

``` python
my_label = gui.Label(root)
my_label.pack()
```

We need to pass the window as an argument, so include `root`, or whatever variable the window is stored in, when we call the `Label` constructor.

After we've created any widget, we need to ***pack*** the window. Packing a window means making the window the size of the content. If we had lots of elements (widgets), the window would be big, but if we only had a couple of widgets, the window would be very small. We can do this using the `pack()` method on any widget, such as `my_label.pack()`.

> **Note**: Always make sure to create widgets *before* the game loop. If you create a `Label` after you type `gui.mainloop()`, the label will not be shown on the screen. All code should go in between `root = gui.Tk()` and `gui.mainloop()`.

You may notice that, when we run our program, nothing happens. That isn't quite true - something is happening, it's just that we can't see it. The reason? We haven't given it any text!

We can set the text of a `Label` by modifying the `text` argument when calling the `Label()` function. Change the line containing `my_label = gui.label(root)` to the following:

``` python
my_label = gui.Label(root, text="Insert text here")
```

Therefore, the entire program would be as follows:

``` python
import tkinter as gui
root = gui.Tk()
my_label = gui.Label(root, text="Insert text here")
my_label.pack()
gui.mainloop()
```

I'm not sure I really need to explain this, but you can change `"Insert text here"` to something else. When you run the program, your text will appear on the window:

![|--- Code output cannot load ---|](res/2.png)

The window size is a little strange, but I think the big thing we need to do in the next tutorial is to change the title of the window, from `"tk"` to something else. Let's do that!

# Chapter 3: Changing the title

Let's change the title of the window, from `"tk"` to something else! To start off, I've added a few more labels to our program, which should balance out the window dimensions a little:

![|--- Code output cannot load ---|](res/3.png)

Just in case you're interested, here's the code:

``` python
import tkinter as gui
root = gui.Tk()

label_1 = gui.Label(root, text="Hello there!")
label_1.pack()
label_2 = gui.Label(root, text="This is my awesome program")
label_2.pack()
label_3 = gui.Label(root, text="Do you like it?")
label_3.pack()
label_4 = gui.Label(root, text="FaNcY gRaPhIcS!!!!")
label_4.pack()

gui.mainloop()
```

Don't worry if this feels too complicated, the code isn't the main point. Instead, let's get to changing the title of the window!

We can change the window title using this code:

``` python
root.title("Insert title here...")
```

For my program, I would add this line of code before the main loop:

``` python
root.title("BONJOUR!!!")
```

This would produce this window:

![|--- Code output cannot load ---|](res/4.png)

And... there you go! That's how you change the title of a tkinter window! Next, we'll go over how to set the background colour of a window.

# Chapter 4: Setting the background colour of the window

The grey background isn't very interesting, so let's go over how we can change that!

Let's just imagine an empty window. The code for this would be:

``` python
import tkinter as gui
root = gui.Tk()
gui.mainloop()
```

The output would be as follows:

![|--- Code output cannot load ---|](res/1.png)

We can change the background colour of a window using the `bg` attribute. Look at this code:

``` python
root["bg"] = "#330066"
```

We can insert this line before the main loop, and so our code becomes as follows:

``` python
import tkinter as gui
root = gui.Tk()
root["bg"] = "#330066"
gui.mainloop()
```

This will output the following window:

![|--- Code output cannot load ---|](res/5.png)

The way this works is by modifying the `bg` item of the window.

We can also change the background of a label. Look at this code:

``` python
import tkinter as gui
root = gui.Tk()
my_label = gui.Label(root, text="Hello, World!!!")
my_label["bg"] = "#00ff00"
my_label.pack()
gui.mainloop()
```

This would change the background colour of the `Label` to green (#00ff00), but the window would stay grey.

![|--- Code output cannot load ---|](res/6.png)

> **Note**: Whenever we specify a colour in tkinter, we use *hexadecimal*. If you don't know how to write in hexadecimal, there are plenty of websites that will give you the *hex-code* for any given colour.

We can specify `bg` when an element is created.

To do this, set the `bg` keyword argument to a hex value. For example, when creating a `Label`:

``` python
import tkinter as gui
root = gui.Tk()

my_label = gui.Label(root, text="Hello, World!!!")
my_label["bg"] = "#00ff00"
my_label.pack()

gui.mainloop()
```

We could instead just write:

``` python
import tkinter as gui
root = gui.Tk()

my_label = gui.Label(root, text="Hello, World!!!", bg="#00ff00")
my_label.pack()

gui.mainloop()
```

Great, that's how you set the background colour of a widget! You can do the exact same thing for the ***foreground*** colour, which is the colour of the text. Look at this code:

``` python
import tkinter as gui
root = gui.Tk()

root["bg"] = "#000022"
lbl = gui.Label(root, text="Hello world!", bg="#000022")
lbl["fg"] = "#00ff00"
lbl.pack()

gui.mainloop()
```

This would output the following:

![|--- Code output cannot load ---|](res/7.png)

# Chapter 5: Making the window bigger

You may have noticed something while you've gone through the tutorial - the window is *really* small. We can change this by setting the window's `minsize` attribute.  
`minsize` sets the minimum size of the window - the window will never be smaller than `minsize`. 

We can call the `minsize()` method on the `root` object.  
Add the following code before `root.mainloop()`:

``` python
root.minsize(400, 300)
```

This code will force the window to always be at least 400x300px. If there are lots of widgets, it may be bigger, but it can't be any smaller than `400px` in width and `300px` in height.

Output:

![|--- Code output cannot load ---|](res/8.png)

We can also set the max size of a window in the exact same way:

``` python
root.maxsize(800, 600)
```

> **Remember**: `widget.pack()` makes the window the size of its content, so it's the perfect size to fit everything in it. We can set the minimum size of the window using `root.minsize(width, height)`, or the maximum size using `root.maxsize(width, height)`.

# Chapter 6: Buttons

Now that we know how to create `Label`s, we should learn to create buttons - widgets that do something when you click them.

We can create a button the exact same way as we create a `Label`. Look at this code:

``` python
btn = gui.Button(root)
```

This creates a new `Button`, with no text and nothing happening when we click it. Let's make it a little more interesting by adding some text to the button.

``` python
btn = gui.Button(root, text="Click me!")
```

Let's also create a `Label` welcoming the user to our program. Our program would look like this:

``` python
import tkinter as gui
root = gui.Tk()
root.minsize(400, 300)

lbl = gui.Label(root, text="Welcome to the program!")
lbl.pack()
btn = gui.Button(root, text="Click me!")
btn.pack()

gui.mainloop()
```

The output of the code would be:

![|--- Code output cannot load ---|](res/9.png)

Now let's add some interactivity to our program! When the user clicks the button, the text on the `Label` will change. Examine this code:

``` python
import tkinter as gui
root = gui.Tk()
root.minsize(400, 300)

def btn_clicked():
  lbl["text"] = "This program is great!!!"

lbl = gui.Label(root, text="Welcome to the program!")
lbl.pack()
btn = gui.Button(root, text="Click me!", command=btn_clicked)
btn.pack()

gui.mainloop()
```

As always, we'll go through the code in detail.

Firstly, we define the `btn_clicked` function. This function will be called when the button is clicked.  
Inside this `btn_clicked` function, we are changing the text of `lbl` to `"This program is great!!!"`.

Next, we create a new `Label` and pack the screen.

After that, we create the `Button`.  
We set the `Button`'s text to `"Click me!"`.

Now for the important part. We can set the `command` attribute of a `Button` in order to set what happens when the button is clicked. In our case, we pass a reference to a function called `btn_clicked` by typing the name of the function.  
The function will be called when we press the button.

Here is our code in action:

![|--- Code output video cannot load ---|](res/1.webm)

We can style the button however we want to, just like we can with `Label`s. Let's move on to creating **textboxes**!
