import turtle
import random
import sys
import time 

# This creates the window
window = turtle.Screen()
window.bgcolor('aquamarine')
window.tracer(0)
player = turtle.Turtle()
player.shape('circle')
player.color('black')
player.shapesize(2)
player.penup()
player.speed(0)
player.goto(0, -250)
window.update()

def right_arrow_key():
    current_position = player.xcor()
    new_position = current_position + 20
    player.setx(new_position)
    window.update()

def left_arrow_key():
    current_position = player.xcor()
    new_position = current_position - 20
    player.setx(new_position)
    window.update()

window.listen()
window.onkeypress(right_arrow_key, "Right")
window.onkeypress(left_arrow_key, "Left")

enemy = turtle.Turtle()
enemy.shape('square')
enemy.color('red')
enemy.shapesize(3)
enemy.penup()
enemy.speed(0)
secret_position = random.randint(-300, 300)
enemy.goto(secret_position, 270)
window.update()

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()

score = 0 

pen.goto(0, 0)
pen.write("DODGE YOUR ENEMY - THE RED SQUARE", align="center", font=("Calibri", 20, "bold"))
window.update()
time.sleep(1.8)
window.tracer(0)

while True: 
    enemy_position = enemy.ycor()
    new_position = enemy_position - 1   
    enemy.sety(new_position)
    window.update()
    time.sleep(0.001)
    
    if enemy.distance(player) < 40:
        pen.goto(0, 0)
        pen.write("YOU LOST TO THE ENEMY!", align="center", font=("Calibri", 30, "bold"))
        window.update()
        time.sleep(2.5)
        sys.exit()
    elif enemy_position < -300:
        enemy.sety(270)
        secret_position = random.randint(-300, 300)
        enemy.setx(secret_position)
        score = score + 1
        pen.clear()
        pen.goto(200, 260)
        pen.write(score, align="right", font=("Calibri", 18, "bold"))


# This keeps the window open
window.mainloop()