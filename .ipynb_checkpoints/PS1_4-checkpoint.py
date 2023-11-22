# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:46:08 2023

@author: 22948
"""
import math
import random
x=random.randint(1,101)
def Least_moves(RMB):
    step=0
    while RMB!=1:
        if RMB%2==1:
            step+=1
            RMB-=1
        else:
            step+=1
            RMB/=2
    return step
print(x)
print("step numbers:{}".format(Least_moves(x)))