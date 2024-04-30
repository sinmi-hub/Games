from turtle import Turtle, Screen
from random import randint, choice

turtle_obj = Turtle("turtle")
screen = Screen()
screen.colormode(255) # RGB mode

directions = [9, 99, 189, 279]

# function to draw shapes
def draw_shapes(num_sides:int):
    angle = 360 // num_sides
    turtle_obj.color(randint(0, 255), randint(0, 255),randint(0, 255))
    for _ in range(num_sides):
        turtle_obj.forward(randint(15, 30))
        turtle_obj.right(angle)

#random walk
def rand_walk():
    turtle_obj.pensize(15)
    turtle_obj.forward(randint(15, 30))
    turtle_obj.setheading(choice(directions))

def spirograph(rad):
    turtle_obj.circle(rad)
    turtle_obj.setheading(turtle_obj.heading() + 10)
  

def main():
    turtle_obj.speed("fastest")
   
    # spirograph
    for _ in range(100):
        turtle_obj.color(randint(0, 255), randint(0, 255),randint(0, 255))
        spirograph(80)
    
    turtle_obj.setheading(0.0)

     # random walk
    for _ in range(100):
        turtle_obj.color(randint(0, 255), randint(0, 255),randint(0, 255))
        rand_walk()

if __name__ == "__main__":
    main()

screen.exitonclick()