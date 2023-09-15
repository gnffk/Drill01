import turtle



def draw_w():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def draw_a():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def draw_s():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def draw_d():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)
def restart():
    turtle.reset()
    
turtle.onkey(draw_w,'w')
turtle.onkey(draw_s,'s')
turtle.onkey(draw_a,'a')
turtle.onkey(draw_d,'d')
turtle.onkey(restart, 'Escape')

turtle.shape("turtle")
turtle.listen()
