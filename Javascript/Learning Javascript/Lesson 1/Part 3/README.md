# Lesson 1 - Part 3 - Comments

## Files
('starterfile's are what codecademy gave me in the file to start with)

- (app.starterfile.js)[./app.starterfile.js]
- (app.step1.js)[./app.step1.js]
- (app.step2.js)[./app.step2.js]

## Learn

### Comments

Programming is often highly collaborative. In addition, our own code can quickly become difficult to understand when we return to it— sometimes only an hour later! For these reasons, it’s often useful to leave notes in our code for other developers or ourselves

As we write JavaScript, we can write [comments](https://www.codecademy.com/resources/docs/javascript/comments?page_ref=catalog) in our code that the computer will ignore as our program runs. These comments exist just for human readers. 

Comments can explain what the code is doing, leave instructions for developers using the code, or add any other useful annotations. 

There are two types of code comments in JavaScript:

1. A *single line* comment will comment out a single line and is denoted with two forward slashes (`//`) preceding it. For example:

```
// Prints 5 to the console
console.log(5)

```

You can also use a single line comment to comment after a line of code:

```
console.log(5);  // Prints 5 

```
2. A *multi-line* comment will comment out multiple lines and is denoted with `/*` to begin the comment, and `*/` to end the comment.

```
/*
This is all commented 
console.log(10);
None of this is going to run!
console.log(99);
*/

```

You can also use this syntax to comment something out in the middle of a line of code:

```
console.log(/*IGNORED!*/ 5);  // Still just prints 5 

```

## Instructions

1. Let’s practice adding some code comments.<br><br>To the right, we’ve provided you with the beginning of the book *Catch-22* by Joseph Heller.<br><br>On line 1, write a single line comment that says `Opening line`.

2. Single line comments are great for adding context to your code. Multi-line comments are often best suited to prevent a block of code from running. However, both types of comments can be used for either purpose.<br><br>Use a multi-line comment to comment out the rest of the code after the first console.log line. Only It was love at first sight. should be logged to the console.

