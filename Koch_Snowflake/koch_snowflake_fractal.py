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
    Function to draw snowflakes based on the following L-System notation for the Koch Curve:
    F ? F+F--F+F -> where F means draw forward, + is turn left(60), - is turn right(60).
    The function recurses based on the depth which dictates the detail of the curve and thus the snowflake.
    It is called thrice in order to draw the 3 sides of a equilateral triangle.
    '''
    l = 360
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
    for i in range(3):
        draw_curve(l, my_turtle, 4)
        my_turtle.right(120)
    turtle.mainloop()


if __name__ == '__main__':
    main()
