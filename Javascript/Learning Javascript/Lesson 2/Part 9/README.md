# Lesson 2 - Part 9 - typeof operator

## Files
- Starter File - [main.starterfile.js](./main.starterfile.js)
- Step 1 - [main.step1.js](./main.step1.js)
- Step 2 - [main.step2.js](./main.step2.js)
- Step 3 - [main.step3.js](./main.step3.js)

## Learn

### typeof operator

While writing code, it can be useful to keep track of the [data types](https://www.codecademy.com/resources/docs/javascript/data-types) of the [variables](https://www.codecademy.com/resources/docs/javascript/variables) in your program. If you need to check the data type of a variable’s value, you can use the `typeof` operator.

The `typeof` operator checks the value to its right and *returns*, or passes back, a string of the data type.

```js
const unknown1 = 'foo';
console.log(typeof unknown1); // Output: string

const unknown2 = 10;
console.log(typeof unknown2); // Output: number

const unknown3 = true; 
console.log(typeof unknown3); // Output: boolean
```

Let’s break down the first example. Since the value `unknown1` is `'foo'`, a string, `typeof unknown1` will return `'string'`.

## Instructions

1. Use `console.log()` to print the typeof `newVariable`.
2. Great, now let’s check what happens if we reassign the variable. Below the `console.log()` statement, reassign `newVariable` to `1`.
3. Since you assigned this new value to `newVariable`, it has a new type! On the line below your reassignment, use `console.log()` to print typeof `newVariable` again.