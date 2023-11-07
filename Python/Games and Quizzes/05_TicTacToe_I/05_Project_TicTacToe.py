#!/usr/bin/env python
# coding: utf-8

# In[23]:


def draw_board(position):

    print(f"  {position[0]}  |  {position[1]}  |  {position[2]}  \n-----|-----|-----\n  {position[3]}  |  {position[4]}  |  {position[5]}  \n-----|-----|-----\n  {position[6]}  |  {position[7]}  |  {position[8]}  ")

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

position = [" "] * 9            # Erzeugt ein leeres Spielfeld
score_spieler_1 = 0             # Punkte Spieler 1
score_spieler_2 = 0             # Punkte Spieler 2

name_player_1 = input("Player 1\nYour name: ")
name_player_2 = input("Player 2\nYour name: ")

aktive = True

while aktive:
    
    print("Das Spiel beginnt:")
    draw_board(position)

    valid_move = False

    while not valid_move:
        # Zug von Spieler_1:
        player_1_zug = int(input(f"{name_player_1}, where do you want to play? [0-8]"))
        
        # Zug Spielbar?
        valid_move = check_if_valid(position,player_1_zug)
        
    position[player_1_zug] = "X"         # Spiel-Zug
            
    draw_board(position)
    
    if not check_if_draw(position):
        print("No one has won!")
        print(f"-------------------------------\n----------SCOREBOARD-----------\n-------------------------------\n{name_player_1:>5}          {score_spieler_1:<5}\n{name_player_2:>5}          {score_spieler_2:<5}\n-------------------------------")
        quit = input("If you want to quit, press [n]")
        if quit == "n":
            aktive = False
        position = [" "] * 9
        continue
    
    # Hat Spieler_1 gewonnen?
    if check_win_condition(position):
        score_spieler_1 += 1
        print(f"Player {name_player_1} has won!\n")
        print(f"-------------------------------\n----------SCOREBOARD-----------\n-------------------------------\n{name_player_1:>5}          {score_spieler_1:<5}\n{name_player_2:>5}          {score_spieler_2:<5}\n-------------------------------")
        quit = input("If you want to quit, press [n]")
        if quit == "n":
            aktive = False
        position = [" "] * 9
        continue
        
    valid_move = False
    
    while not valid_move:
        # Zug von Spieler_2:
        player_2_zug = int(input(f"{name_player_2}, where do you want to play? [0-8]"))

        # Zug Spielbar?
        valid_move = check_if_valid(position,player_2_zug)
        
    position[player_2_zug] = "O"         # Spiel-Zug

    draw_board(position)
    
    if not check_if_draw(position):
        print("No one has won!")
        print(f"-------------------------------\n----------SCOREBOARD-----------\n-------------------------------\n{name_player_1:>5}          {score_spieler_1:<5}\n{name_player_2:>5}          {score_spieler_2:<5}\n-------------------------------")
        quit = input("If you want to quit, press [n]")
        if quit == "n":
            aktive = False
        position = [" "] * 9
        continue
        
    # Hat Spieler_2 gewonnen?
    if check_win_condition(position):
        score_spieler_2 += 1
        print(f"Player {name_player_2} has won!\n")
        print(f"-------------------------------\n----------SCOREBOARD-----------\n-------------------------------\n{name_player_1:>5}          {score_spieler_1:<5}\n{name_player_2:>5}          {score_spieler_2:<5}\n-------------------------------")
        quit = input("If you want to quit, press [n]")
        if quit == "n":
            aktive = False
        position = [" "] * 9
        continue
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




