import turtle

depth = 100
length = 20
height = turtle.window_height()
width = turtle.window_width()
margin = 200

turtle.tracer(0)
turtle.speed(0)
turtle.Screen().bgcolor("black")
turtle.Screen().setup(width=width, height=height)
turtle.color("white")
turtle.penup()
turtle.goto(0, (-height/2))
turtle.pendown()

turtle.left(90)

def recurstion(n, l):
    if(n == 0):
        return 0
    base_angle = 20
    turtle.forward(l)
    p = turtle.pos()
    turtle.left(base_angle)
    recurstion(n-1, l*0.9)
    turtle.penup()
    turtle.goto(p)
    turtle.right(2*base_angle)
    turtle.pendown()
    recurstion(n-1, l*0.9)
    turtle.left(base_angle)
    

recurstion(9, 50) 
turtle.done()
