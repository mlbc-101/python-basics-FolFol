"""Write a program that solves second degree equation of the form ax^2 +bx + c = 0."""

import math
a=2
b=3
c=1

if (a==0):
    x=-c/b
    print(" This is a one degree equation, the solution is:")
    print("X = ",x)
else:
    Delta=b*b-4*a*c
    if (Delta > 0):
        x1=(-b-math.sqrt(Delta))/(2*a)
        x2=(-b+math.sqrt(Delta))/(2*a)
        print("This equation has two solutions:") 
        print("X1 = ",x1)
        print("X2 = ",x2)
    elif (Delta == 0):
        x=-b/(2*a)
        print("This equation has only one solution:")
        print("X = ",x)
    else:
        print("This equation has no solution.")
