from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("The Turtle Race! 3..2..1..Let's GO!")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

t = Turtle(shape="turtle")
t.penup()
t.hideturtle()
t.clear()
while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False

            winning_colors = [turtle.pencolor() for turtle in all_turtles if turtle.xcor() >= 230]

            t = Turtle(shape="turtle")
            t.speed("fastest")
            t.penup()
            t.hideturtle()
            t.goto(-230, 0)

            if user_bet in winning_colors:
                t.write(f"You've won!🏆😀\n\nThe {', '.join(winning_colors)} \nturtle is the winner!",
                        font=("Arial", 12, "normal"))
            else:
                t.write(f"You've lost!😭\n\nThe {', '.join(winning_colors)} \nturtle is the winner!",
                        font=("Arial", 12, "normal"))
screen.exitonclick()
