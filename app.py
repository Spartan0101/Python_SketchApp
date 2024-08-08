import turtle
from turtle import Turtle, Screen
import random

# Object State and Instances (turtle Race Bet)
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yloc = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=yloc[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

# Higher order functions & Event Listeners

# tib = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tib.forward(10)
#
#
# def move_backwards():
#     tib.backward(10)
#
#
# def draw_circle():
#     tib.circle(100)
#
#
# def draw_circle_cc():
#     tib.circle(-100)
#
#
# def clear():
#     tib.penup()
#     tib.clear()
#     tib.home()
#     tib.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=draw_circle)
# screen.onkey(key="d", fun=draw_circle_cc)
# screen.onkey(key="c", fun=clear)
#
# screen.exitonclick()