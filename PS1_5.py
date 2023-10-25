# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:59:45 2023

@author: 22948
"""

def Find_expression(i,sum,index):
    global total_num
    if i==index+1:
        if sum==target_sum:
            result=""
            total_num+=1
            for j in range(0,index+1):
                result+=str(num[j])
                if j!=index:
                    if flag[j]:
                        result+="-"
                    else:
                        result+="+"
                else:
                    result+="={}".format(sum)
                    print(result)
        return
    elif i==0:
        Find_expression(i+1,num[i],index)
        return
    flag[i-1]=0
    Find_expression(i+1,sum+num[i],index)
    flag[i-1]=1
    Find_expression(i+1,sum-num[i],index)
    return
        
    
#n 分成几个数 r剩几个数
def generate_num(n,r,index,now_num):
    if n==1:
        for i in range(-r,0):
            num[index]=num[index]*10+now_num
            now_num+=1
        Find_expression(0,0,index)
        num[index]=0
        now_num=r-n+1
        return
    else:
        #至多可以与后面 r-n 个数字结合
        for i in range(0,r-n+1):
            for j in range(0,i+1):
                num[index]=num[index]*10+now_num
                now_num+=1
            index+=1
            generate_num(n-1,r-i-1,index,now_num)
            index-=1
            num[index]=0
            now_num-=i+1
            
num=[0,0,0,0,0,0,0,0,0]
now_num=1
index=0 #分成的第几个数
flag=[0,0,0,0,0,0,0,0]
target_sum=50
total_num=0
#5.1
#for n in range(9,1,-1):
#    generate_num(n,9,index,now_num)
   
#5.2
Total_solutions=[]
for target_sum in range(1,101):
    total_num=0
    for n in range(9,1,-1):
        generate_num(n,9,index,now_num)
    Total_solutions.append(total_num)
Max=max(Total_solutions)
Min=min(Total_solutions)
def  searchIndex(List,num):
    resultList=[]
    for i in range(len(List)):
        if List[i]==num:
            resultList.append(i+1)
    return resultList
print("Total_solutions:")
print(Total_solutions)
print("{} yields the maximum of Total_solutions".format(searchIndex(Total_solutions,Max)))
print("{} yields the minimum of Total_solutions".format(searchIndex(Total_solutions,Min)))
    