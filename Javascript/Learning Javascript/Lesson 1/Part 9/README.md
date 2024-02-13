# Lesson 1 - Part 9 - Built-in Objects

## Files
('starterfile's are what codecademy gave me in the file to start with)

- [app.starterfile.js](./app.starterfile.js)
- [app.step1.js](./app.step1.js)
- [app.step2.js](./app.step2.js)
- [app.step3.js](./app.step3.js)
- [app.step4.js](./app.step4.js)

## Learn

### Built-in Objects

In addition to `console`, there are other [objects built into JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects). Down the line, you’ll build your own [objects](https://www.codecademy.com/resources/docs/javascript/objects), but for now these “built-in” objects are full of useful functionality. 

For example, if you wanted to perform more complex mathematical operations than arithmetic, JavaScript has the built-in `Math` object. 

The great thing about objects is that they have methods! Let’s call the `.random()` method from the built-in `Math` object:

```js
console.log(Math.random()); // Prints a random number between 0 and 1

```

In the example above, we called the `.random()` method by appending the object name with the dot operator, the name of the method, and opening and closing parentheses. This method returns a random number between 0 (inclusive) and 1 (exclusive). 

To generate a random number between 0 and 50, we could multiply this result by 50, like so: 

```js
Math.random() * 50;

```

The example above will likely evaluate to a decimal. To ensure the answer is a whole number, we can take advantage of another useful `Math` method called `Math.floor()`. 

`Math.floor()` takes a decimal number, and rounds down to the nearest whole number. You can use `Math.floor()` to round down a random number like this:

```js
Math.floor(Math.random() * 50);

```

In this case:

1. `Math.random()` generates a random number between 0 and 1.
2. We then multiply that number by `50`, so now we have a number between 0 and 50.
3. Then, `Math.floor()` rounds the number down to the nearest whole number.

If you wanted to see the number printed to the terminal, you would still need to use a `console.log()` statement:

```js
console.log(Math.floor(Math.random() * 50)); // Prints a random whole number between 0 and 50

```

To see all of the properties and [methods](https://www.codecademy.com/resources/docs/javascript/methods) on the `Math` object, take a look at [the documentation here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math).

## Instructions

1. Inside of a `console.log()`, create a random number with `Math.random()`, then multiply it by `100`.
2. Now, use `Math.floor()` to make the output a whole number.<br><br>Inside the `console.log()` you wrote in the last step, put the existing `Math.random() * 100` code inside the parentheses of `Math.floor()`.
3. Find a method on the [JavaScript `Math` object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math) that returns the smallest integer greater than or equal to a decimal number.<br><br>Use this method with the number `43.8`. Log the answer to the console.
4. Use the JavaScript documentation to find a method on the built-in `Number` object that checks if a number is an integer.<br><br>Put the number `2017` in the parentheses of the method and use `console.log()` to print the result.