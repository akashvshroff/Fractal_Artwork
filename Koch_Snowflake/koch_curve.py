import turtle


def draw_curve(length, t, depth):
    if depth == 0:
        t.forward(length)
        return
    length //= 3
    draw_curve(length, t, depth-1)
    t.left(60)
    draw_curve(length, t, depth-1)
    t.right(120)
    draw_curve(length, t, depth-1)
    t.left(60)
    draw_curve(length, t, depth - 1)


def main():
    '''
    A function that draws a simple koch curve based on the following L-System notation:
    F ? F+F--F+F -> where F means draw forward, + is turn left(60), - is turn right(60).
    The function recurses based on the depth which dictates the detail of the curve and thus the snowflake.
    '''
    my_turtle = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.title('Koch Curve')
    my_turtle.up()
    my_turtle.backward(180)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.down()
    my_turtle.color('white')
    my_turtle.speed(30)
    draw_curve(360, my_turtle, 4)
    turtle.mainloop()


if __name__ == '__main__':
    main()
