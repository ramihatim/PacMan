import os.path
import time
import turtle
import random

# variables
speed = 10
lives = 3
score = 0

# window/screen settings
window = turtle.Screen()
window.addshape(os.path.expanduser("/Users/mac/Documents/pacman/pacman1.gif"))  # adding pacman shape from files
window.addshape(os.path.expanduser("/Users/mac/Documents/pacman/ghost2.gif"))  # adding ghost shape from files
window.tracer(7)
window.title("Pacman By Rami & Mark")
window.bgcolor("Black")
window.setup(800, 800)

pacman = turtle.Turtle()  # creating a pacman turtle
pacman.shape(
    os.path.expanduser("/Users/mac/Documents/pacman/pacman1.gif"))  # connecting the gif with the shape of the turtle
pacman.speed()
pacman.penup()  # turning of pen mode
pacman.direction = 'stop'

# ghosts
ghosts = []  # making ghosts list
for x in range(10):  # for loop to create 10 ghosts turtles
    ghost = turtle.Turtle()
    ghost.shape(os.path.expanduser("/Users/mac/Documents/pacman/ghost2.gif"))  # connecting the gif with the shape of the turtle
    ghost.penup()
    ghost.speed = 4
    x = random.randint(-380, 380)
    y = random.randint(-380, 380)
    ghost.setposition(x, y)
    ghosts.append(ghost)

#text score
pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.penup()
pen.goto(0, 320) #setting the text on top of the screen
pen.pendown()
pen.write('Score: {}   Lives: {}'.format(score, lives), align='center', font=('ArcadeClassic', 36))
pen.hideturtle()

# food
foods = []
for _ in range(40):
    food = turtle.Turtle()
    food.penup()
    food.shape('circle')
    food.color('white')
    food.shapesize(0.5, 0.5)
    x = random.randint(-380, 380)
    y = random.randint(-380, 380)
    food.setposition(x, y)
    foods.append(food)


# creating movement function
def movement():
    if pacman.direction == 'up':
        y = pacman.ycor()
        y += speed
        pacman.sety(y)

    if pacman.direction == 'down':
        y = pacman.ycor()
        y -= speed
        pacman.sety(y)

    if pacman.direction == 'left':
        x = pacman.xcor()
        x -= speed
        pacman.setx(x)

    if pacman.direction == 'right':
        x = pacman.xcor()
        x += speed
        pacman.setx(x)


# windows binding functions
def moveUp():
    pacman.direction = 'up'


def moveDown():
    pacman.direction = 'down'


def moveLeft():
    pacman.direction = 'left'


def moveRight():
    pacman.direction = 'right'


# ghosts movement
def ghostMovement():
    for ghost in ghosts:
        y = ghost.ycor()
        x = ghost.xcor()

        y += ghost.speed
        x += ghost.speed
        ghost.sety(y)
        ghost.setx(x)


# set window binding

window.listen()
window.onkeypress(moveUp, 'Up')
window.onkeypress(moveDown, 'Down')
window.onkeypress(moveLeft, 'Left')
window.onkeypress(moveRight, 'Right')

# main game loop
while True:
    window.update()

    # border collision
    if pacman.xcor() > 400 or pacman.xcor() < -400 or pacman.ycor() > 400 or pacman.ycor() < -400:
        lives -= 1
        pen.clear()
        pen.write('Score: {}   Lives: {}'.format(score, lives), align='center', font=('ArcadeClassic', 36))
        time.sleep(1)
        pacman.goto(0, 0)

    # food and pacman collision
    for food in foods:
        if pacman.distance(food) < 10:
            score += 1
            pen.clear()
            pen.write('Score: {}   Lives: {}'.format(score, lives), align='center', font=('ArcadeClassic', 36))
            x = random.randint(-380, 380)
            y = random.randint(-380, 380)
            food.goto(x, y)

    # game over
    if lives == 0:
        window.resetscreen
        window.setup(800, 800)
        pen.clear()
        pen.goto(0, 0)
        pen.color('red')
        pen.penup()
        pen.write(' Game Over \nyour score: {}'.format(score), align='center', font=('ArcadeClassic', 50))
    else:
        ghostMovement()
        movement()

    # ghosts and border
    for ghost in ghosts:
        if ghost.xcor() > 400 or ghost.xcor() < -400 or ghost.ycor() > 400 or ghost.ycor() < -400:
            x = random.randint(-380, 380)
            y = random.randint(-380, 380)
            ghost.goto(x, y)
            ghostMovement()

    # ghosts and pacman
    for ghost in ghosts:
        if pacman.distance(ghost) < 15:  # checks if the distance between a ghost and pacman less than 15 pixels
            lives -= 1  # loses one life
            pen.clear()
            pen.write('Score: {}   Lives: {}'.format(score, lives), align='center', font=('ArcadeClassic', 36))
            x = random.randint(-380, 380)
            y = random.randint(-380, 380)
            pacman.goto(x, y)  # random respawn


