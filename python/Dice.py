import random


def foo(sides):
    print(random.randint(0,sides))

active = True

while active:
    print ('Choose number of sides, or to end type 0')
    i = int(input())

    if i > 0 :
        foo(i)
    else:
        print("End")
        active = False

    
    
    
    
