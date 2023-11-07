import TicTacToeBoard as board
import TicTacToeKI as ki

position = board.clear_board()         # Erzeugt ein leeres Spielfeld
score_spieler_1 = 0                    # Punkte Spieler 1
score_spieler_2 = 0                    # Punkte Spieler 2

name_player_1 = input("Player 1\nYour name: ")
name_player_2 = "Computer"
print(f"Player 2\nYour name: {name_player_2}")
print("Das Spiel beginnt:")
board.draw_board(position)

aktive = True

while aktive:
    
    board.clear_board()

    valid_move = False

    while not valid_move:
        # Zug von Spieler_1:
        player_1_zug = int(input(f"{name_player_1}, where do you want to play? [0-8]"))
        
        # Zug Spielbar?
        valid_move = board.check_if_valid(position,player_1_zug)
        
    position[player_1_zug] = "X"         # Spiel-Zug
            
    board.draw_board(position)
    
    if not board.check_if_draw(position):
        print("No one has won!")
        print(f"-------------------------------\n----------SCOREBOARD-----------\n-------------------------------\n{name_player_1:^5}          {score_spieler_1:<10}\n{name_player_2:<1}       {score_spieler_2:<1}\n-------------------------------")
        quit = input("If you want to quit, press [n]")
        if quit == "n":
            aktive = False
        position = board.clear_board()
        continue
    
    # Hat Spieler_1 gewonnen?
    if board.check_win_condition(position):
        score_spieler_1 += 1
        print(f"Player {name_player_1} has won!\n")
        print(f"-------------------------------\n----------SCOREBOARD-----------\n-------------------------------\n{name_player_1:^5}          {score_spieler_1:<10}\n{name_player_2:<1}       {score_spieler_2:<1}\n-------------------------------")
        quit = input("If you want to quit, press [n]")
        if quit == "n":
            aktive = False
        position = board.clear_board()
        continue
        
    valid_move = False
    
    while not valid_move:
        # Zug von Spieler_2:
        player_2_zug = ki.make_good_move(position)
        print(f"{name_player_2}, where do you want to play? [0-8] {player_2_zug}")

        # Zug Spielbar?
        valid_move = board.check_if_valid(position,player_2_zug)
        
    position[player_2_zug] = "O"         # Spiel-Zug

    board.draw_board(position)
    
    if not board.check_if_draw(position):
        print("No one has won!")
        print(f"-------------------------------\n----------SCOREBOARD-----------\n-------------------------------\n{name_player_1:^5}          {score_spieler_1:<10}\n{name_player_2:<1}       {score_spieler_2:<1}\n-------------------------------")
        quit = input("If you want to quit, press [n]")
        if quit == "n":
            aktive = False
        position = board.clear_board()
        continue
        
    # Hat Spieler_2 gewonnen?
    if board.check_win_condition(position):
        score_spieler_2 += 1
        print(f"Player {name_player_2} has won!\n")
        print(f"-------------------------------\n----------SCOREBOARD-----------\n-------------------------------\n{name_player_1:^5}          {score_spieler_1:<10}\n{name_player_2:<1}       {score_spieler_2:<1}\n-------------------------------")
        quit = input("If you want to quit, press [n]")
        if quit == "n":
            aktive = False
        position = board.clear_board()
        continue
        



