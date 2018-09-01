# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:43:42 2018

@author: kyleh
"""
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses = 0
if abs(guess**3 - cube) >= epsilon:
    print('failed cube root of', cube)
else:
    print(guess, 'is close to cube root of', cube)
    zzzz
    zzzz
    zzzz
    zzz
    yyyy
    yyyy
    xxxx
    xxxx
    