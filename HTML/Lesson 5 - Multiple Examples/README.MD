# Review
Awesome job adding client-side validation to "form"s!

Let’s quickly recap:

1. Client-side validations happen in the browser before information is sent to a server.
2. Adding the required attribute to an input related element will validate that the input field has information in it.
3. Assigning a value to the min attribute of a number input element will validate an acceptable minimum value.
4. Assigning a value to the max attribute of a number input element will validate an acceptable maximum value.
5. Assigning a value to the minlength attribute of a text input element will validate an acceptable minimum number of characters.
6. Assigning a value to the maxlength attribute of a text input element will validate an acceptable maximum number of characters.
7. Assigning a regex to pattern matches the input to the provided regex.
8. If validations on a "form" do not pass, the user gets a message explaining why and the "form" cannot be submitted.

These quick checks help ensure that input data is correct and safe for our servers. It also helps give users immediate feedback on what they need to fix instead of having to wait for a server to send back that information.