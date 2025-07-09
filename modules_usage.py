#Program to calculate the square root, sine & natural log using 'math' module
from math import sqrt, sin, log #Importing functions 'sqrt', 'sin' & 'log' from 'math' module

num = int(input("Enter a Number: "))    #Takes the input of number whose square root, sine & natural log has to be calculated.

print(f"Square Root: {sqrt(num)}")  #Prints the square root of 'num' using 'sqrt' function
print(f"Logarithm: {log(num)}")  #Prints the natural log of 'num' using 'log' function
print(f"Sine: {sin(num)}")  #Prints the sine of 'num' using 'sin' function
