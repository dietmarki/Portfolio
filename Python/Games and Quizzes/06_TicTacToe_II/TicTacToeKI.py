# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:49:32 2023

@author: dietm
"""

from random import randint 

def make_random_move():
    computer = randint(0,8)
    return computer

def make_good_move(position):
    
    a = randint(0, 8)
    
    if position[2] == " " and position[0] == position[1] == "X" or position[4] == position[6] == "X" or position[5] == position[8] == "X" or position[0] == position[1] == "0" or position[4] == position[6] == "0" or position[5] == position[8] == "0":
        return 2
    if position[0] == " " and position[1] == position[2] == "X" or position[4] == position[8] == "X" or position[3] == position[6] == "X" or position[1] == position[2] == "0" or position[4] == position[8] == "0" or position[3] == position[6] == "0":
        return 0
    if position[6] == " " and position[0] == position[3] == "X" or position[2] == position[4] == "X" or position[7] == position[8] == "X" or position[0] == position[3] == "0" or position[2] == position[4] == "0" or position[7] == position[8] == "0":
        return 6
    if position[8] == " " and position[0] == position[4] == "X" or position[2] == position[5] == "X" or position[6] == position[7] == "X" or position[0] == position[4] == "0" or position[2] == position[5] == "0" or position[6] == position[7] == "0":
        return 8
    if position[3] == " " and position[0] == position[6] == "X" or position[4] == position[5] == "X" or position[0] == position[6] == "0" or position[4] == position[5] == "0":
        return 3
    if position[7] == " " and position[6] == position[8] == "X" or position[1] == position[4] == "X" or position[6] == position[8] == "0" or position[1] == position[4] == "0":
        return 7
    if position[5] == " " and position[3] == position[4] == "X" or position[2] == position[8] == "X" or position[3] == position[4] == "0" or position[2] == position[8] == "0":
        return 5
    if position[1] == " " and position[0] == position[2] == "X" or position[4] == position[7] == "X" or position[0] == position[2] == "0" or position[4] == position[7] == "0":
        return 1
    if position[4] == " " and position[0] == position[8] == "X" or position[2] == position[6] == "X" or position[3] == position[5] == "X" or position[1] == position[7] == "X" or position[0] == position[8] == "0" or position[2] == position[6] == "0" or position[3] == position[5] == "0" or position[1] == position[7] == "0":
        return 4
    else:
        return a
