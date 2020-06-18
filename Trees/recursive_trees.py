import turtle


def draw_tree(b_length, t):
    if b_length > 2:
        t.forward(b_length)
        t.right(20)
        draw_tree(b_length-12, t)
        t.left(40)
        draw_tree(b_length-12, t)
        t.right(20)
        t.backward(b_length)


def main(branch_length):
    '''
    Function to draw recursively draw fractal trees using turtle! The module makes it so you
    can visualise the process and see how the tree evolves.
    '''
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_turtle.speed(30)
    my_win.bgcolor("black")
    my_win.title("Fractal Tree")
    my_turtle.color("white")
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(200)
    my_turtle.down()
    draw_tree(branch_length, my_turtle)
    my_win.exitonclick()


main(100)
