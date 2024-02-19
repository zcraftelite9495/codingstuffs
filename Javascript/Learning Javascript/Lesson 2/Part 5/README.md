# Lesson 2 - Part 5 - Mathematical Assignment Operators

## Files
- Starter File - [main.starterfile.js](./main.starterfile.js)
- Step 1 - [main.step1.js](./main.step1.js)
- Step 1 - [main.step1.js](./main.step2.js)
- Step 1 - [main.step1.js](./main.step3.js)
- Step 1 - [main.step1.js](./main.step4.js)

## Learn

### Mathematical Assignment Operators

Let’s consider how we can use [variables](https://www.codecademy.com/resources/docs/javascript/variables) and math [operators](https://www.codecademy.com/resources/docs/javascript/operators) to calculate new values and assign them to a variable. Check out the example below:

```js
let w = 4;
w = w + 1;

console.log(w); // Output: 5

```

In the example above, we created the variable `w` with the number `4` assigned to it. The following line, `w = w + 1`, increases the value of `w` from `4` to `5`.

Another way we could have reassigned `w` after performing some mathematical operation on it is to use built-in *mathematical assignment operators*. We could re-write the code above to be:

```js
let w = 4;
w += 1;

console.log(w); // Output: 5

```

In the second example, we used the `+=` assignment operator to reassign `w`. We’re performing the mathematical operation of the first operator `+` using the number to the right, then reassigning `w` to the computed value.

```js
let x = 20;
x -= 5; // Can be written as x = x - 5
console.log(x); // Output: 15

let y = 50;
y *= 2; // Can be written as y = y * 2
console.log(y); // Output: 100

let z = 8;
z /= 2; // Can be written as z = z / 2
console.log(z); // Output: 4

```

Let’s practice using these mathematical assignment operators!

## Instructions
1. Use the `+=` mathematical assignment operator to increase the value stored in `levelUp` by `5`.
2. Use the `-=` mathematical assignment operator to decrease the value stored in `powerLevel` by `100`.
3. Use the `*=` mathematical assignment operator to multiply the value stored in `multiplyMe` by `11`.
4. Use the `/=` mathematical assignment operator to divide the value stored in `quarterMe` by `4`.
