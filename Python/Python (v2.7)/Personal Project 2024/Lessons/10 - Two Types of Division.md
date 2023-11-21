# Two Types of Division
## Learn
In Python 2, when we divide two integers, we get an integer as a result. When the quotient is a whole number, this works fine:
```
quotient = 6/2
# the value of quotient is now 3, which makes sense
```
However, if the numbers do not divide evenly, the result of the division is truncated into an integer. In other words, the quotient is rounded down to a whole number. This can be surprising when you expect to receive a decimal and you receive a rounded-down integer:
```
quotient = 7/2
# the value of quotient is 3, even though the result of the division here is 3.5
```
To yield a float as the result instead, programmers often change either the numerator or the denominator (or both) to be a float:
```
quotient1 = 7./2
# the value of quotient1 is 3.5
quotient2 = 7/2.
# the value of quotient2 is 3.5
quotient3 = 7./2.
# the value of quotient3 is 3.5
```
An alternative way is to use the ```float()``` method:
```
quotient1 = float(7)/2 
# the value of quotient1 is 3.5
```
## Instructions
1. You have come home from the grocery store with 100 cucumbers to split amongst yourself and your 5 roommates (6 people total). Create a variable ```cucumbers``` that holds ```100``` and ```num_people``` that holds ```6```.
2. Create a variable called ```whole_cucumbers_per_person``` that is the integer result of dividing cucumbers by ```num_people```. Print ```whole_cucumbers_per_person``` to the console.
3. You realize that the numbers don’t divide evenly and you don’t want to throw out the remaining cucumbers. Create a variable called ```float_cucumbers_per_person``` that holds the float result of dividing cucumbers by ```num_people```. Print ```float_cucumbers_per_person``` to the console.