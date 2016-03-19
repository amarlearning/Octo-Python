import turtle

def draw_circle_square(t) :
    i = 0
    while(i < 370) :
        t.right(10)
        j = 1
        while(j < 5) :
            t.forward(100)
            t.right(90)
            j+=1
        i+=10
    brad.right(80)
    brad.forward(250)

window = turtle.Screen()
window.bgcolor("red")

brad = turtle.Turtle()
brad.color("yellow")
brad.shape("turtle")
brad.speed(2)
draw_circle_square(brad)

window.exitonclick()
