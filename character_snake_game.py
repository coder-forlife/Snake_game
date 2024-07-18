import turtle
import time
import random
import os
import sys
turtle.register_shape("F_Down.gif")
turtle.register_shape("F_Left.gif")
turtle.register_shape("F_Right.gif")
turtle.register_shape("F_Up.gif")
turtle.register_shape("Body.gif")
food=turtle.Turtle()
food.shape("circle")
food.color("green")
food.penup()
food.setpos(200,150)
head=turtle.Turtle()
head.shape("F_Up.gif")
turtle.bgcolor("black")
head.color("white")
head.direction="stop"
screen=turtle.Screen()
score=turtle.Turtle()
score.color("white")
score.penup()
score.setpos(300,300)
score.pendown()
head.penup()
segments=[]
score.write("Score = " + str(len(segments)), font=("Arial",10,"bold"))
turtle.screensize(canvwidth=220,canvheight=220)
def down():
  if head.direction!="up":
    head.direction="down"
    head.shape("F_Down.gif")
def up():
  if head.direction!="down":
    head.direction="up"
    head.shape("F_Up.gif")
def left():
  if head.direction!="right":
    head.direction="left"
    head.shape("F_Left.gif")
def right():
  if head.direction!="left":
    head.direction="right"
    head.shape("F_Right.gif")
def move():
  if head.direction=="up":
    y=head.ycor()
    head.sety(y+20)
  if head.direction=="down":
    y=head.ycor()
    head.sety(y-20)
  if head.direction=="left":
    x=head.xcor()
    head.setx(x-20)
  if head.direction=="right":
    x=head.xcor()
    head.setx(x+20)
  


screen.listen()
screen.onkey(up,"Up")
screen.onkey(right,"Right")
screen.onkey(left,"Left")
screen.onkey(down,"Down")


while(True):
  screen.update()
  
  if (head.xcor()<=-220 or head.xcor()>=220 or head.ycor()>=220 or head.ycor()<=-220):
    screen.clear()
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-180,0)
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.write("game over", font=("Calibri",60,"bold"))
    time.sleep(1)
    screen.bye()
    os.system('python "C://Users//priya//OneDrive//Desktop//Python Neha//Class thirty five//character_snake_game.py')
    head.hideturtle()
    time.sleep(1)
    head.goto(0,0)
    head.showturtle()
  if (head.distance(food)<20):    
    x2=random.randint(-220,220)
    y2=random.randint(-220,220)
    shape=random.choice(["square",
                         "circle","triangle"])
    colors=random.choice(["red","green",
                          "yellow"])
    food.shape(shape)
    food.color(colors)
    food.setpos(x2,y2)
    new_segment=turtle.Turtle()
    new_segment.speed(0)
    new_segment.penup()
    new_segment.shape("Body.gif")
    new_segment.color("orange")
    segments.append(new_segment)
    score.clear()
    score.write("Score = " + str(len(segments)), font=("Arial",10,"bold"))
  for index in range(len(segments)-1,0,-1):
    x=segments[index-1].xcor()
    y=segments[index-1].ycor()
    segments[index].goto(x,y)
  if len(segments)>0:
    x=head.xcor()
    y=head.ycor()
    segments[0].goto(x,y)
  move()
  time.sleep(0.1) 
screen.mainloop()

