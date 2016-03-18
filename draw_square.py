import turtle

def draw_square(turtle_name) :
    i = 1
    while(i<5) :
        turtle_name.forward(100)
        turtle_name.right(90)
        i+=1

def draw_circle(turtle_name) :
    turtle_name.circle(100)

def draw_triangle(turtle_name) :
    turtle_name.left(180)
    turtle_name.forward(100)
    turtle_name.right(240)
    turtle_name.forward(100)
    turtle_name.right(240)
    turtle_name.forward(100)

window = turtle.Screen()
window.bgcolor("yellow")

brad = turtle.Turtle()
brad.color("green")
brad.shape("turtle")
draw_square(brad)

pit = turtle.Turtle()
pit.color("red")
pit.shape("circle")
draw_circle(pit)

trip = turtle.Turtle()
trip.color("blue")
trip.shape("triangle")
draw_triangle(trip)

window.exitonclick()
