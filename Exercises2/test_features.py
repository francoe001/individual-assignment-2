#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:40:31 2018

@author: efrancois
"""

from features import checkout

def checkout_features_empty():
    
    shopping_cart = []
    
    assert checkout_features_empty(shopping_cart) == "Your shopping cart is Empty!"
    

def test_checkout_features_five_random_items():
    added_services = ["Insurance", "Insurance", "Insurance", "Priority mail", "Priority mail"]
    shopping_cart = ["Guitar", "Guitar", "Guitar"]
    
    assert checkout(shopping_cart, added_services) == "Your Total price is $3015"
