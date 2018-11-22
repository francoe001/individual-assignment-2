#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:54:43 2018

@author: efrancois
"""
#%%
#Exercise 2
 #  You want to give more features to the user, so you decide that you will 
  # allow them to purchase an insurance package on their purchase and also priority mail.  
  # Consider that these two new services can only be purchase once per order.
   # 1. Insurance: $5
   # 2. Priority mail: $10
   # Modify your checkout function so it handles these cases correctly, and add 
   # more tests that check your functionality.
   
inventory = {"Guitar": 1000, "Pick box": 5, "Guitar Strings": 10}
add_ons = {"Insurance": 5, "Priority mail": 10}
total_price = list()
added = list()
    
def checkout(shopping_cart, added_services):

    
    if shopping_cart == []:
        return "Your shopping cart is Empty!"
    else:
        for price in shopping_cart:
            total_price.append(inventory[price])
            
            for items in added_services:
                if items not in added:
                    total_price.append(add_ons[items])
                    added.append(items)
                    
        return "Your Total price is $" + str(sum(total_price))

added_services = ["Insurance", "Insurance", "Insurance", "Priority mail", "Priority mail"]
shopping_cart = []
print(checkout(shopping_cart, added_services))

