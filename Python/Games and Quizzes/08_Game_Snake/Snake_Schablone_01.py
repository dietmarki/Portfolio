from tkinter import *
import random
import logging

logging.basicConfig(level='DEBUG', format='%(levelname)s - %(message)s')

GAME_WIDTH  = 1200
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
SNAKE_COLOR = "#00FF00"

BG_COLOR    = "#000000"

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


# funktion für neues spiel mit leertaste
def new_game():
    
    global end_screen
    
    if end_screen:
        logging.info("Neues Spiel gestartet!")
        
        end_screen = False
        
        canvas.delete(ALL)

        snake = Snake()
        food = Food(canvas)
        
        # schlüssel für 4 richtungen:
        window.bind('<w>', lambda event: change_direction(snake,UP))
        window.bind('<a>', lambda event: change_direction(snake,LEFT))
        window.bind('<s>', lambda event: change_direction(snake,DOWN))
        window.bind('<d>', lambda event: change_direction(snake,RIGHT))        
        
        next_turn(snake, food)
        
# schlange --> klasse definieren
class Snake:  
    
    def __init__(self):
        self.coordinates = [(0,0),(0,0),(0,0)]       #schlangenkörper (3 Glieder)
        self.squares = []
        self.direction = DOWN
        
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)

# food bauen:
class Food:
    FOOD_COLOR = "#FFFF00"
    
    def __init__(self,canvas):
        
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        
        self.coordinates = (x,y)
        
        self.draw(canvas)
        
    def draw(self,canvas):
        x = self.coordinates[0]
        y = self.coordinates[1]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = Food.FOOD_COLOR, tag = "food")
    

# funktion richtung:
def change_direction(snake,new_direction):
    
    if new_direction == LEFT:
        if snake.direction != RIGHT:
            snake.direction = new_direction
    elif new_direction == RIGHT:
        if snake.direction != LEFT:
            snake.direction = new_direction
    elif new_direction == UP:
        if snake.direction != DOWN:
            snake.direction = new_direction
    elif new_direction == DOWN:
        if snake.direction != UP:
            snake.direction = new_direction
            
# bewegung der schlange
def next_turn(snake, food):
    
    # koordinaten - kopf der schlange
    x,y = snake.coordinates[0]
    
    if snake.direction == DOWN:
        y += SPACE_SIZE
    elif snake.direction == UP:
        y -= SPACE_SIZE
    elif snake.direction == LEFT:
        x -= SPACE_SIZE
    elif snake.direction == RIGHT:
        x += SPACE_SIZE
        
        
    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
    snake.squares.insert(0, square)
    
    # schlange frißt:
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score = len(snake.coordinates) - 3
        label.config(text="Score:{}".format(score), font=('consolas', 40))
        canvas.delete("food")
        food = Food(canvas)
        
    else:            
        # löschen des letzten schlangengliedes:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    # bei schlangenkopf außerhalb spielfeld --> game over
    if check_collision(snake):
        game_over()
    else:
        # schlangenkopf wieder aufrufen --> bewegung (neue quadrate)
        window.after(SPEED, next_turn, snake, food)
        
# funktion kollision mit wand:
def check_collision(snake):
    
    # koordinaten von schlangenkopf:
    x,y = snake.coordinates[0]
    if x < 0 or y < 0 or x > GAME_WIDTH or y > GAME_HEIGHT:
        return True
    
    # trifft schlange sich selbst? (schlange ausser kopf mit index [0])
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False

# spiel beendet funktion:
def game_over():
    global end_screen
    end_screen = True
    canvas.delete(ALL)
    
    # text in einer fläche:
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, text = "Gegen die Wand gefahren!!!", fill = "red",font =("consolas",50),tag = "gameover")
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2 + 100, text = "Für neues Spiel bitte Leertaste drücken!", fill = "cyan",font =("consolas",20),tag = "gameover")

    
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

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# neues spiel starten mit leertaste:
window.bind('<space>', lambda event: new_game()) 
   

window.mainloop()