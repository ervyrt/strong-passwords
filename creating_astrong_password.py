# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:16:07 2021

@author: yurtb
"""
# LET'S CREATE A STRONG PASSWORD
import random
import time
word= input("please write a sentence that you can remember easily:")
x= word.split()
list=[]
for i in x:  
    a=random.choice([0,1]) 
    if a ==0:
        i=i.lower()
        list.append(i[0])
    else:
        i=i.upper()
        list.append(i[0])
year=input("please input an important date for yourself:")
puncuation=[".",":",",",";","-","_","?"]
print("we are creating a strong password for you...")
time.sleep(1)
p=random.choice((0,6))
pun=puncuation[p]
your_password=str()
for i in list:
    your_password=your_password+i
your_password=your_password+pun
your_password=your_password+year
print(your_password)
