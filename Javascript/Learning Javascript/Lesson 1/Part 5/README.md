# Lesson 1 - Part 5 - Arithmetic Operators

## Files
('starterfile's are what codecademy gave me in the file to start with)

- [app.starterfile.js](./app.starterfile.js)
- [app.step1.js](./app.step1.js)
- [app.step1.js](./app.step2.js)
- [app.step1.js](./app.step3.js)
- [app.step1.js](./app.step4.js)

## Learn

### Arithmetic Operators

Basic arithmetic often comes in handy when programming. 

An [operator](https://www.codecademy.com/resources/docs/javascript/operators?page_ref=catalog) is a character that performs a task in our code. JavaScript has several built-in *arithmetic operators*, that allow us to perform mathematical calculations on numbers. These include the following operators and their corresponding symbols:


1. Add: `+`
2. Subtract: `-`
3. Multiply: `*`
4. Divide: `/`
5. Remainder: `%`

The first four work how you might guess: 

```
console.log(3 + 4); // Prints 7
console.log(5 - 1); // Prints 4
console.log(4 * 2); // Prints 8
console.log(9 / 3); // Prints 3

```

Note that when we `console.log()` the computer will evaluate the expression inside the parentheses and print that result to the console. If we wanted to print the characters `3 + 4`, we would wrap them in quotes and print them as a string. 

```
console.log(11 % 3); // Prints 2
console.log(12 % 3); // Prints 0

```

The remainder operator, sometimes called *modulo*, returns the number that remains after the right-hand number divides into the left-hand number as many times as it evenly can: `11 % 3` equals 2 because 3 fits into 11 three times, leaving 2 as the remainder.

## Instructions

1. Inside of a `console.log()`, add `3.5` to your age.<br><br>This is the age you’ll be when we start sending people to live on Mars.
2. On a new line write another `console.log()`. Inside the parentheses, take the current year and subtract `1969`.<br><br>The answer is how many years it’s been since the 1969 moon landing.
3. Create another `console.log()`. Inside the parentheses divide `65` by `240`.
4. Create one last `console.log()`. Inside the parentheses, multiply `0.2708` by `100`.<br><br>That’s the percent of the sun that is made up of helium. Assuming we could stand on the sun, we’d all sound like chipmunks!
