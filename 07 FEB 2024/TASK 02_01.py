'''Write a Python program to calculate the
area of a circle given its radius using
the formula area=π×r^2 ( Take pie as 3.14)'''
from math import pi

radius=float(input("Enter the radius:- "))
area= float(pi *radius **2)
print(area)
