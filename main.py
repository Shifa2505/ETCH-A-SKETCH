# w = forwards
# S = backwards
# A = counter-clock
# D = clockwise
# c = clear screen

from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def move_forwards():
    return tim.forward(10)


def move_backwards():
    return tim.backward(10)


def move_counter_clock():
    return tim.left(10)


def move_clock():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()