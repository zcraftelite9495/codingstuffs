# Lesson 2 - Part 7 - String Concatenation with Variables

## Files
- Starter File - [main.starterfile.js](./main.starterfile.js)

## Learn

### String Concatenation with Variables

In previous exercises, we assigned [strings](https://www.codecademy.com/resources/docs/javascript/strings) to [variables](https://www.codecademy.com/resources/docs/javascript/variables). Now, let’s go over how to connect, or concatenate, strings in variables.

The + operator can be used to combine two string values even if those values are being stored in variables:

```js
let myPet = 'armadillo';
console.log('I own a pet ' + myPet + '.'); 
// Output: 'I own a pet armadillo.'

```

In the example above, we assigned the value `'armadillo'` to the `myPet` variable. On the second line, the `+` operator is used to combine three strings: `'I own a pet'`, the value saved to `myPet`, and `'.'`. We log the result of this concatenation to the console as:

```output
I own a pet armadillo.
```

## Instructions

1. Create a variable named `favoriteAnimal` and set it equal to your favorite animal.
2. Use `console.log()` to print `'My favorite animal: ANIMAL'` to the console. Use string concatenation so that `ANIMAL` is replaced with the value in your `favoriteAnimal` variable.