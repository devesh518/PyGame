#Purpose: Create a pong game
#Author: Devesh Patel
#Date: 11th Nov 2021

import turtle
import winsound
from playsound import playsound

wn = turtle.Screen()  #Creating a window using turtle
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=1024, height=1280)
wn.tracer(0)

#Paddle 1
paddle_1 = turtle.Turtle() #Turtle is the name of the class here
paddle_1.speed(0)          #This is not the speed of the paddle, it is just the speed of animation
paddle_1.shape("square")   #square is one of the built-in shapes
paddle_1.shapesize(stretch_wid=5, stretch_len=1) #To change the size of the paddle
paddle_1.color("white")    #color of the paddle
paddle_1.penup()
paddle_1.goto(-480, 0)     #co-ordinates of the initial position of where i want the paddle to be


#Paddle 2
paddle_2 = turtle.Turtle() #Turtle is the name of the class here
paddle_2.speed(0)          #This is not the speed of the paddle, it is just the speed of animation
paddle_2.shape("square")   #square is one of the built-in shapes
paddle_2.shapesize(stretch_wid=5, stretch_len=1) #To change the size of the paddle
paddle_2.color("white")    #color of the paddle
paddle_2.penup()
paddle_2.goto(480, 0)


#Ball
ball = turtle.Turtle() #Turtle is the name of the class here and paddle_1, paddle_2 and ball are the objects
ball.speed(0)          #This is not the speed of the paddle, it is just the speed of animation
ball.shape("square")   #square is one of the built-in shapes
ball.shapesize(stretch_wid=1, stretch_len=1) #Here, we do not want to change the size of the ball
ball.color("sky blue")    #color of the paddle
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

#Variables for score
score_1 = 0
score_2 = 0



#Scoring system by making a pen
pen = turtle.Turtle()  #Creating a new object named as pen 
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))


#Functions for the game
def paddle_1_up():
    y = paddle_1.ycor()   #For finding the y-coordinate of paddle 1
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()   #For finding the y-coordinate of paddle 1 
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()   #For finding the y-coordinate of paddle 2
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()   #For finding the y-coordinate of paddle 2
    y -= 20
    paddle_2.sety(y)


#Binding the keyboard
wn.listen()   #To listen to the keyboard input
wn.onkeypress(paddle_1_up, "w")  #This line executes the function paddle_1_up() when w is pressed on the keyboard
wn.onkeypress(paddle_1_down, "s")  #This line executes the function paddle_1_down() when s is pressed on the keyboard
wn.onkeypress(paddle_2_up, "Up")  #This line executes the function paddle_2_up() when up arrow is pressed on the keyboard
wn.onkeypress(paddle_2_down, "Down")  #This line executes the function paddle_2_down() when down arrow is pressed on the keyboard

#Creating a Main game loop which is necessary for every game

while True:
    wn.update() #This updates the screen everytime the loop runs
    
    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Making boundaries/borders for the ball
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
        
    if ball.xcor() > 480: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)

    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
        
    if ball.xcor() < -480: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)

    #Paddle and ball collision

    if (ball.xcor() > 460 and ball.xcor() < 480) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(460)
        ball.dx *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() < -460 and ball.xcor() > -480) and (ball.ycor() > paddle_1.ycor() - 40 and ball.ycor() < paddle_1.ycor() + 40):
        ball.setx(-460)
        ball.dx *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)  