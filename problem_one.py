"""
Write a program which will find and display all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
"""
index=2000
while (index>=2000 and 3200>=index):
    if(index%7==0 and index%5!=0):
        print(index)
    index+=1
