#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:12:32 2018

@author: efrancois
"""
#%%
#Exercise 1
 #  Our e-shop sells the following products:

 #  1. Guitar: $1000
 #  2. Pick box: $5
 #  3. Guitar Strings: $10

  # Create a function named checkout that takes a list that represents a shopping 
  #cart and returns the total cost of it.  This function should check that the shopping 
  #cart must not be empty.

   #Create also some tests for the function.  Try to think of the corner cases.

   #Hint: you can represent a product as a dictionary with a name and a price.


   


inventory = {"Guitar": 1000, "Pick box": 5, "Guitar Strings": 10}
total_price = list()
    
def checkout(shopping_cart):

    
    if shopping_cart == []:
        return "Your shopping cart is Empty!"
    else:
        for price in shopping_cart:
            total_price.append(inventory[price])
        return "Your Total price is $" + str(sum(total_price))
shopping_cart = []
print(checkout(shopping_cart))












    
    