import math
import turtle

colors = [
    "#3B1A08",  # 1 — темна кора (стовбур)
    "#6B3318",  # 2 — темно-коричневий (великі гілки)
    "#8B5A2B",  # 3 — середній коричневий (гілки)
    "#A07840",  # 4 — теплий коричневий (дрібні гілки)
    "#6B6B20",  # 5 — оливковий (перехід)
    "#4A6B25",  # 6 — дубово-зелений (молоде листя)
    "#2D5C1A",  # 7 — глибокий зелений (крона дуба)
]

def get_color(order, max_order):
    index = max_order - order
    if index > len(colors) - 1:
        index = len(colors) - 1
    return colors[index]

def set_color_and_size(t, order, max_order):
    t.pencolor(get_color(order, max_order))
    t.pensize(order*2)

def reset_pen(t, x, y, angle):
    t.penup()
    t.goto(x,y)
    t.setheading(angle)
    t.pendown()

def draw_leaf(t, size, color="#2D5C1A"):
    t.fillcolor(color)
    t.pencolor("#1A3D0A")
    t.pensize(1)
    t.begin_fill()
    t.left(-15)
    t.circle(size, 90)
    t.left(90)
    t.circle(size, 90)
    t.right(45)
    t.end_fill()

def pythagoras_curve(t, order, max_order, size):
    if order == 0:
        draw_leaf(t, size)
    else:
        x = t.xcor()
        y = t.ycor()
        origin_angle = t.heading()
        for angle in [-45, 45]:
            reset_pen(t, x, y, origin_angle)
            t.right(angle)
            set_color_and_size(t, order, max_order)
            t.forward(size)
            pythagoras_curve(t, order - 1, max_order, size/5*4)


def draw_pythagoras(size=100):
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    order = window.numinput(
        "Дерево Піфагора",
        "Введіть рівень рекурсії (1-10):",
        default=5,
        minval=3,
        maxval=10
    )

    if order is None:   # користувач натиснув Cancel
        turtle.bye()
        return
    else:
        order = int(order)

    t.penup()
    t.goto(0, -size*2)
    t.pendown()

    t.left(90)
    set_color_and_size(t, order, order)
    t.forward(size)
    pythagoras_curve(t, order, order, size/5*4)

    t.end_fill()

    t.setheading(0)

    window.mainloop()

if __name__ == "__main__":
    draw_pythagoras()

