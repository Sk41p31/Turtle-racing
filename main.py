from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "yellow", "orange", "green", "blue", "purple"]

turtles = []

for color in colors:
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    turtles.append(new_turtle)

for i in range(len(turtles)):
    turtles[i].penup()
    turtles[i].goto(-230, 120 - 40 * i)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Ether the color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winner = turtle.color()[0]
            is_race_on = False
            break

if user_bet == winner:
    print("You won!")
else:
    print("You lost!")


screen.exitonclick()