# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:15:24 2023

@author: 22948
"""
def Pascal_triangle(k):
    List=[]
    for i in range(0,k):
        tempList=[]
        for j in range(0,i+1):
            if j==0 or j==i:
                tempList.append(1)
            else:
                tempList.append(List[i-1][j-1]+List[i-1][j])
        List.append(tempList)
    return List[-1]
        

print("line 100:{}".format(Pascal_triangle(100)))
print("line 200:{}".format(Pascal_triangle(200)))