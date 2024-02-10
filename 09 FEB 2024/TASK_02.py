#Write a program that classifies a triangle based on its side lengths.

side1=int(input("Enter the triangle first side is:- "))
side2=int(input("Enter the triangle second side is:- "))
side3=int(input("Enter the triangle third side is:- "))
if side1==side2==side3:
    print("This triangle is an equilateral triangle.")
elif side1==side2 or side2==side3 or side3==side1:
    print("This triangle is an isosceles triangle.")
else:
    print("This triangle is an scalene triangle.")