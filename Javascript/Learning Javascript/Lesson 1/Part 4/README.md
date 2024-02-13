# Lesson 1 - Part 4 - Data Types

## Files
('starterfile's are what codecademy gave me in the file to start with)

- [app.starterfile.js](./app.starterfile.js)
- [app.step1.js](./app.step1.js)
- [app.step2.js](./app.step2.js)
- [app.step3.js](./app.step3.js)
- [app.step4.js](./app.step4.js)

## Learn

### Data Types

[Data types](https://www.codecademy.com/resources/docs/javascript/data-types?page_ref=catalog) are the classifications we give to the different kinds of data that we use in programming. In JavaScript, there are eight fundamental data types:

* *Number*: Any number, including numbers with decimals: `4`, `8`, `1516`, `23.42`.
* *BigInt*: Any number, greater than 2<sup>53</sup>-1 or less than -(2<sup>53</sup>-1), with n appended to the number: `1234567890123456n`.
* *String*: Any grouping of characters on your keyboard (letters, numbers, spaces, symbols, etc.) surrounded by single quotes: `' ... '` or double quotes `" ... "`, though we prefer single quotes. Some people like to think of string as a fancy word for text.
* *Boolean*: This data type only has two possible values— either `true` or `false` (without quotes). It’s helpful to think of booleans as on and off switches or as the answers to a “yes” or “no” question.
* *Null*: This data type represents the intentional absence of a value, and is represented by the keyword `null` (without quotes).
* *Undefined*: This data type is denoted by the keyword `undefined` (without quotes). It also represents the absence of a value though it has a different use than `null`. `undefined` means that a given value does not exist.
* *Symbol*: A newer feature to the language, symbols are unique identifiers, useful in more complex coding. No need to worry about these for now.
* *Object*: Collections of related data.

The first 7 of those types are considered *primitive data types*. They are the most basic data types in the language. *Objects* are more complex, and you’ll learn much more about them as you progress through JavaScript. At first, eight types may not seem like that many, but soon you’ll observe the world opens with possibilities once you start leveraging each one. As you learn
more about objects, you’ll be able to create complex collections of data.

But before we do that, let’s get comfortable with strings and numbers!

```js
console.log('Location of Codecademy headquarters: 575 Broadway, New York City');
console.log(40);

```

In the example above, we first printed a string. Our string isn’t just a single word; it includes both capital and lowercase letters, spaces, and punctuation.

Next, we printed the number 40, notice we did not use quotes. 

## Instructions

1. On line 1, log the string `'JavaScript'` to the console.
2. On line 2, log the number `2011` to the console.
3. On line 3, print `'Woohoo! I love to code! #codecademy'` to the console.
4. On line 4, print the number `20.49` to the console.