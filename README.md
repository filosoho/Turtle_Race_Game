# Turtle_Race_Game
This is a simple turtle race game where users can place bets on which turtle they think will win.

# How to Play
Run the script:
~~~
main.py
~~~

* Enter your bet by typing the color of the turtle you think will win.  
* The race will begin and the turtles will start moving forward at random distances.  
* Once a turtle reaches the finish line (the right side of the screen), the race ends.  
* If the turtle you bet on wins, a message saying "You've won!" and the winning turtle's color will be displayed. Otherwise, a message saying "You've lost!" and the winning turtle's color will be displayed.  

# Prerequisites
~~~
Python 3
~~~
~~~
Turtle module (included in Python Standard Library)
~~~

# Running the Script  
Simply run the script:
~~~
main.py
~~~

# Customization
Users can customize the number and color of turtles that participate in the race by modifying the colors list and y_positions list in the script.  
~~~
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
~~~
~~~
y_positions = [-70, -40, -10, 20, 50, 80]
~~~
~~~
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
~~~
Users can also modify the distance that the turtles move forward at each step of the race by modifying the rand_distance variable in the script.
~~~
rand_distance = random.randint(0, 10)
turtle.forward(rand_distance)
~~~

 # Contributing
If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

# License
Feel free to use and modify the code as per your requirements.
