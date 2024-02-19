# Lesson 2 - Part 3 - Create a Variable: let

## Files
- Starter File - [app.starterfile.js](./app.starterfile.js)
- Step 1 - [app.step1.js](./app.step1.js)
- Step 2 - [app.step2.js](./app.step2.js)
- Personal Extension Step 3 - [app.step3.js](./app.step3.js)


## Learn

### Create a Variable: let

As mentioned in the previous exercise, the `let` keyword was introduced in ES6. The `let` keyword signals that the variable can be reassigned a different value. Take a look at the example:

```js
let meal = 'Enchiladas';
console.log(meal); // Output: Enchiladas
meal = 'Burrito';
console.log(meal); // Output: Burrito

```

Another concept that we should be aware of when using `let` (and even `var`) is that we can declare a variable without assigning the variable a value. In such a case, the variable will be automatically initialized with a value of `undefined`:

```js
let price;
console.log(price); // Output: undefined
price = 350;
console.log(price); // Output: 350

```

Notice in the example above:
* If we don’t assign a value to a variable declared using the `let` keyword, it automatically has a value of `undefined`.
* We can reassign the value of the variable.

## Instructions

1. Create a `let` variable called `changeMe` and set it equal to the boolean `true`.
2. On the line after `changeMe` is declared, set the value of `changeMe` to be the boolean `false`.<br><br>To check if `changeMe` was reassigned, log the value saved to `changeMe` to the console.
3. **(Personal Extension)** Create a `let` variable called `thisIsUndefined` and don't set a value.<br><br>To check if `thisIsUndefined` is set correctly, log the value saved to `thisIsUndefined` to the console.

(A 'Personal Extension' is an additional step I made to challenge myself, and was not a instruction provided by Codecademy)