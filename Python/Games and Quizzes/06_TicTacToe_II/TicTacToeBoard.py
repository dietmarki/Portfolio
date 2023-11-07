# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 18:27:28 2023

@author: dietm
"""

def draw_board(position):

    print(f"  {position[0]}  |  {position[1]}  |  {position[2]}  \n-----|-----|-----\n  {position[3]}  |  {position[4]}  |  {position[5]}  \n-----|-----|-----\n  {position[6]}  |  {position[7]}  |  {position[8]}  ")

def clear_board():

    return [" "] * 9
        
def check_if_valid(position,move):
    for i in range(len(position)):
        if position[i] == " " and i == move:
            return True
    return False

def check_if_draw(position):
    if not " " in position:
        return False
    return True

def check_win_condition(position):
    
    if position[0] == position[1] == position[2] and position[0] != " ":
        return True
    if position[3] == position[4] == position[5] and position[3] != " ":
        return True
    if position[6] == position[7] == position[8] and position[6] != " ":
        return True
    if position[0] == position[3] == position[6] and position[0] != " ":
        return True
    if position[1] == position[4] == position[7] and position[1] != " ":
        return True
    if position[2] == position[5] == position[8] and position[2] != " ":
        return True
    if position[0] == position[4] == position[8] and position[0] != " ":
        return True
    if position[6] == position[4] == position[2] and position[6] != " ":
        return True
    else:
        return False
