import turtle

def draw_koch_curve(koch_turtle, size, level):
    
    if level == 0:
        koch_turtle.forward(size)
        return

    draw_koch_curve(koch_turtle, size / 3, level - 1)
    koch_turtle.left(60)
    draw_koch_curve(koch_turtle, size / 3, level - 1)
    koch_turtle.right(120)
    draw_koch_curve(koch_turtle, size / 3, level - 1)
    koch_turtle.left(60)
    draw_koch_curve(koch_turtle, size / 3, level - 1)

def main():

    koch_turtle = turtle.Turtle()
    koch_turtle.speed(0)
    koch_turtle.pensize(2)
    koch_turtle.penup()

    while True:
        level = int(input("Введіть рівень рекурсії (0-7): "))
        if 0 <= level <= 7:
            break
        else:
            print("Неправильне значення рівня рекурсії. Введіть значення від 0 до 7.")

    koch_turtle.setposition(-0.8, 0.6)
    koch_turtle.pendown()

    draw_koch_curve(koch_turtle, 160, level)

    koch_turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()