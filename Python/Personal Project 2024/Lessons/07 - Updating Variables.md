# Updating Variables
## Learn
Changing the contents of a variable is one of the essential operations. As the flow of a program progresses, data should be updated to reflect changes that have happened.
```
fish_in_clarks_pond = 50

print "Catching fish"

number_of_fish_caught = 10
fish_in_clarks_pond = fish_in_clarks_pond - number_of_fish_caught

```
n the above example, we start with 50 fish in a local pond. After catching 10 fish, we update the number of fish in the pond to be the original number of fish in the pond minus the number of fish caught. At the end of this code block, the variable ```fish_in_clarks_pond``` is equal to 40.

Updating a variable by adding or subtracting a number to its original value is such a common task that it has its own shorthand to make it faster and easier to read.
```
money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price

sandwich_price += sales_tax
money_in_wallet -= sandwich_price
```
In the above example, we use the price of a sandwich to calculate sales tax. After calculating the tax we add it to the total price of the sandwich. Finally, we complete the transaction by reducing our ```money_in_wallet``` by the cost of the sandwich (with tax).
## Instructions
1. We’re trying to figure out how much it rained in the past year! Update the ```annual_rainfall``` variable to include the values from September to December.