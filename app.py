from turtle import Turtle, Screen

# Higher order functions & Event Listeners

tib = Turtle()
screen = Screen()


def move_forwards():
    tib.forward(10)


def move_backwards():
    tib.backward(10)


def draw_circle():
    tib.circle(100)


def draw_circle_cc():
    tib.circle(-100)


def clear():
    tib.penup()
    tib.clear()
    tib.home()
    tib.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=draw_circle)
screen.onkey(key="d", fun=draw_circle_cc)
screen.onkey(key="c", fun=clear)

screen.exitonclick()