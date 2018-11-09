#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:50:55 2018

@author: efrancois
"""

#Bubblesort = O(n^2) 
input_list = [1,4,2,7,92,68,32,15]

def bubble(lst):
    
    y = 0
    
    while y < len(lst):
        
        x= 0 
        while x < len(lst) - 1:
            print("comparing " +str(lst[x]) + " with " + str(lst[x+1]))
            
            if lst[x] > lst[x +1]:
                temp = lst[x]
                lst[x] = lst[x + 1]
                lst[x + 1] =temp
            
            x = x + 1
        
        y += 1
        print(lst)

#%%

#Mergesort = O(nlog(n))
#Recursion

def sum_list(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
                
#slicing
#lst[x:y:z] where x is the first element to start the slice, y is the last element to end the slice, z is the interval          

