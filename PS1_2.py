# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 23:51:17 2023

@author: 22948
"""
import numpy as np
M1=np.random.randint(0,51,(5,10))
M2=np.random.randint(0,51,(10,5))
print("M1:{}".format(M1))
print("M2:{}".format(M2))

def Matrix_multip(M1,M2):
    if M1.shape[1]!=M2.shape[0]:
        return "error"
    else:
        row=M1.shape[0]
        col=M2.shape[1]
        middle=M1.shape[1]
        M3=np.zeros((row,col))
        for i in range(0,row):
            for j in range(0,col):
                for k in range(0,middle):
                    M3[i,j]+=M1[i,k]*M2[k,j]
    return M3
    
print("M1*M2:{}".format(Matrix_multip(M1,M2)))