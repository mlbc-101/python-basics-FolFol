"""Write a program which can compute the factorial of a given numbers."""

Number=5
Factorial=1
index=1
while (index>=1 and Number>=index):
    Factorial *= index
    index+=1
print(Factorial)