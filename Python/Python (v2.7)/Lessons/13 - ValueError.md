# ValueError
## Learn
Python automatically assigns a variable the appropriate datatype based on the value it is given. A variable with the value ```7``` is an integer, ```7.``` is a float, and ```"7"``` is a string. Sometimes, we will want to convert variables to different datatypes. For example, if we wanted to print out an integer as part of a string, we would need to convert that integer to a string first. We can do that using ```str()```:
```
age = 13
print "I am " + str(age) + " years old!"
```
This would print:
```
>>> "I am 13 years old!"
```
Similarly, if we have the string ```"7"``` and we want to perform arithmetic operations on it, we must convert it to a numeric datatype. We can do this using ```int()```:
```
number1 = "100"
number2 = "10"

string_addition = number1 + number2 
# string_addition now has a value of "10010"

int_addition = int(number1) + int(number2)
# int_addition has a value of 110
```
If we have a string that is a floating point value, such as ```"7.5"```, we can convert it to a numeric datatype using ```float()``` instead:
```
string_num = "7.5"
print float(string_num)
```
```
>>> 7.5
```
Using ```float()``` on an integer value, whether string or numeric, will convert the value to a float:
```
string_int = "10"
numeric_int = 12

print float(string_int)
print float(numeric_int)
```
```
>>> 10.0
>>> 12.0
```
The result of using ```int()``` on a floating point value will depend on whether the value is a string or numeric datatype. If you use ```int()``` on a floating point string value, it will raise a ```ValueError```:
```
string_float = "7.5"
print int(string_float)
```
```
Traceback (most recent call last):
  File "script.py", line 2, in <module>
    print int(string_num)
ValueError: invalid literal for int() with base 10: '7.5'
```
Using ```int()``` on a floating point numeric value converts the number to an integer by removing the decimal portion and rounding the number closer towards 0:
```
numeric_float_positive = 7.5
numeric_float_negative = -9.5

print int(numeric_float_positive)
print int(numeric_float_negative)
```
```
>>> 7
>>> -9
```
**Note**: Use caution when converting a floating point number into an integer, as this may result in the loss of the decimal data.
## Instructions
1. Create a variable called ```product``` that contains the result of multiplying the float value of ```float_1``` and ```float_2```.