#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:28:20 2018

@author: efrancois
"""

from Homework_Exercises_2 import checkout

def test_checkout_empty():
    shopping_cart = []
    
    assert checkout(shopping_cart) == "Your shopping cart is Empty!"


def test_checkout_five_random_items():
    shopping_cart = ["Guitar", "Pick box", "Guitar Strings", "Guitar", "Guitar"]
    
    assert checkout(shopping_cart) == "Your Total price is $3015"


