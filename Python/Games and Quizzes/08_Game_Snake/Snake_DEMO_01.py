from tkinter import *
import random
import logging

logging.basicConfig(level='INFO', format='%(levelname)s - %(message)s')

# KONSTANTE VARIABLEN
GAME_WIDTH  = 1200
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
SNAKE_COLOR = "#00FF00"
BG_COLOR    = "#000000"
FOOD_COLOR  = "#FF0000"

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


class Snake:

    def __init__(self):
        self.coordinates = [(0,0), (0,0), (0,0)]
        self.squares     = []
        self.direction   = DOWN

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self,canvas):
        
        x = random.randint(0, (GAME_WIDTH  / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        
        self.coordinates = (x, y)
        
        self.draw(canvas)

    def draw(self, canvas):
        x = self.coordinates[0]
        y = self.coordinates[1]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake: Snake, food: Food):
    """
    Rechnet die nächste Bewegung der Schlange.

    Args:
        snake (Snake)
        food (Food)
    """
    logging.debug(f"Coordinates: {snake.coordinates}")
    logging.debug(f"Squares: {snake.squares}")

    # Die Koordinaten des Kopfes
    x, y = snake.coordinates[0]

    if snake.direction == UP:
        y -= SPACE_SIZE
        
    elif snake.direction == DOWN:
        y += SPACE_SIZE

    elif snake.direction == LEFT:
        x -= SPACE_SIZE

    elif snake.direction == RIGHT:
        x += SPACE_SIZE

    # Füge die neue Koordinate und das Quadrat in Position 0, wo sich der Kopf befindet.
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    
    # Sind die Koordinaten vom Kopf die gleichen mit dem Apfel?
    # Wenn ja, dann wächst der Körper um 1.
    if x == food.coordinates[0] and y == food.coordinates[1]: 
        
        # Update Score
        score = len(snake.coordinates) - 3
        label.config(text=f"Score:{score}")
        
        # Erstelle einen neuen Apfel.
        canvas.delete("food")
        food = Food(canvas)

    # Sonst, lösche die letzte Koordinate und Quadrat, wenn man nicht wächst.
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Sind wir auf etwas gestoßen?
    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(snake:Snake, new_direction:int):
    """
    Ändert die Richtung der Schlange und verhinder eine 180 Grad Drehung. 

    Args:
        snake (Snake)
        new_direction (str)
    """
    if new_direction == LEFT:
        if snake.direction != RIGHT:
            snake.direction = new_direction

    elif new_direction ==RIGHT:
        if snake.direction != LEFT:
            snake.direction = new_direction

    elif new_direction == UP:
        if snake.direction != DOWN:
            snake.direction = new_direction

    elif new_direction == DOWN:
        if snake.direction != UP:
            snake.direction = new_direction


def check_collisions(snake:Snake):
    """
    Checkt, ob die Schlange entweder die Wand oder sich selbst getroffen hat.

    Args:
        snake (Snake)

    Returns:
        bool
    """
    # Die Koordinaten des Kopfes
    x, y = snake.coordinates[0]
    
    # Trifft der Kopf der Schlange auf den Grenzen des Fensters?
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    
    # Trifft der Kopf der Schlange auf den restlichen Körper? 
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    """
    Entfernt alle Elemente aus der GUI und gibt den 'GAME OVER' Text wieder.
    """
    logging.info("Game over.")
    
    global end_screen

    end_screen = True
    
    logging.debug(f"end_screen: {end_screen}")
    
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")    
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 100,
                       font=('consolas', 20), text="Drücke das Leerzeichen, um nochmal zu spielen.", fill="red", tag="gameover")

def new_game():
    """
    Erstellt ein neues Spiel, wenn man auf dem 'Game Over' Schirm steht.
    """
    global end_screen
    
    if end_screen:    
    
        logging.info("New game started!")
    
        end_screen = False
    
        canvas.delete(ALL)
    
        snake = Snake()
        food  = Food(canvas)

        label.config(text="Score:{}".format(0))

        window.bind('<a>', lambda event: change_direction(snake, LEFT))
        window.bind('<d>', lambda event: change_direction(snake, RIGHT))
        window.bind('<w>', lambda event: change_direction(snake, UP))
        window.bind('<s>', lambda event: change_direction(snake, DOWN))

        next_turn(snake, food)
    
    else:
        logging.info("Game is already running!")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

end_screen = True

label = Label(window, text="Score:{}".format(0), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width /2) - (window_width /2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<space>', lambda event: new_game())    

window.mainloop()
