//-//-// Program Written by Zena Comerford //-//-//
//-//-// Kelvin Weather //-//-//
//-//-// Completed as a part of the Javascript Codeacademy cirriculum //-//-//

//--// Task 1 & Task 2
// Sets the temperture forecast in Kelvin to 293, stored in the `kelvin` variable
const kelvin = 293;

//--// Task 1 Test
// Code is commented out when finished testing
//code// console.log(kelvin);

//--// Task 3 & Task 4
// Since Temperture in Celsius is 273 less than temperature in Kelvin, sets the temperture forecast in celsius to 273 less than kelvin, store in the `celsius`
const celsius = kelvin - 273;

//--// Task 3 Test 
// Code is commented out when finished testing
//code// console.log(kelvin);
//code// console.log(celsius);

//--// Task 5 & Task 6
// Follows the equation for the conversion of Celsius to Fahrenheit and then saves it to the variable `fahrenheit` (modifiable variable)
let fahrenheit = celsius * (9/5) + 32;

//--// Task 5 Test
// Code is commented out when finished testing
//code// console.log(fahrenheit);

//--// Task 7 & Task 8
// Rounds the value in fahrenheit down because it it often a decimal value
fahrenheit = Math.floor(fahrenheit);

//--// Task 7 Test
// Code is commented out when finished testing
//code// console.log(fahrenheit);

//--// Task 9
// Prints the value in fahrenheit using the given structure
console.log(`The temperture is ${fahrenheit} degrees Fahrenheit`);

//--// Bonus Task 1
// Follows the equation for the conversion of Celsius to Newtons and saves it to the variable `newton` (modifiable variable)
let newton = celsius * (30/100);

//--// Bonus Task 2
// Rounds the newton value down
newton = Math.floor(newton);

//--// Bonus Task 3
// Prints all the values out neatly :3
console.log(`Temperatures in Different Formats \n--------------------------\nKelvin: ${kelvin}\nCelsius: ${celsius}\nFahrenheit: ${fahrenheit}\nNewton: ${newton}`)