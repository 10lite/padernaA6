# Write a program that asks the user to input two positive integers (m, n) 
# and determine the greatest common factor (gcf) of these two numbers.  
# Write a user-defined function (UDF) for gcf.  
# Your gcf should have two parameters and return the greatest common factor or divisor to the main program.  
# You should not use a built-in function in this assignment.  

def gcf(a, b):
    while(b):
        a, b = b, a % b
    return a

m = int(input("Input first positive integer:"))
n = int(input("Input second positive integer:"))

print("their gcf =",gcf(m, n))



