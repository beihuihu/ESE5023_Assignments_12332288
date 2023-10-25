# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:11:33 2023

@author: 22948
"""
import random as random
def Print_values(a,b,c):
    if a>b:
        if b>c:
            if a>c:
                print("output:{} {} {}".format(a,c,b))
            else:
                print("output:{} {} {}".format(c,a,b))
        else:
            print("output:{} {} {}".format(a,b,c))
    else:
        if not b>c:
            print("output:{} {} {}".format(c,b,a))
        
a=random.random()
print("a:{}".format(a))
b=random.random()
print("b:{}".format(b))
c=random.random()
print("c{}".format(c))
Print_values(a,b,c)