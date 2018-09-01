# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:22:27 2018

@author: kyleh
"""
#vEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# 75Is your secret number 75?
x= input('Please think of a number between 0 and 100!')
high = 100
low = 0
ans = int((high + low)//2)
y = 'a'
while y != 'c':
    ans = int((high + low)//2)
    print('Is your secret number ', ans, '?')
    y = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if y == 'l':
        low = ((high + low)//2)
    elif y == 'h':
        high = ((high + low)//2)
    elif y == 'c':
        print('Game over. Your secret number was:', ans)
        break
    while y != 'l' or y != 'h' or y != 'c':
        if y == 'l' or y == 'h' or y == 'c':
            break
        print('Sorry, I did not understand your input.')
        print('Is your secret number ', ans, '?')
        y = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        if y == 'l':
            low = ((high + low)//2)
            break
        elif y == 'h':
            high = ((high + low)//2)
            break
        elif y == 'c':
            print('Game over. Your secret number was:', ans)
            break
    else:


        zzzzz
        zzzzz
        zzzzz
        yyyy
        yyyy
        xxxxx
        xxxxx