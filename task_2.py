import turtle

def draw_koch_curve(turtle, size, level):

  if level == 0:
    turtle.forward(size)
    return

  draw_koch_curve(turtle, size / 3, level - 1)
  turtle.left(60)
  draw_koch_curve(turtle, size / 3, level - 1)
  turtle.right(120)
  draw_koch_curve(turtle, size / 3, level - 1)
  turtle.left(60)
  draw_koch_curve(turtle, size / 3, level - 1)

turtle = turtle.Turtle()

def main():
  turtle.speed(0)
  turtle.pensize(1)
  turtle.penup()

  while True:
    try:
      level = int(input("Введіть рівень рекурсії (0-7): "))
      if 0 <= level <= 7:
        break
      else:
        print("Неправильне значення рівня рекурсії. Введіть значення від 0 до 7.")
    except ValueError:
      print("Неправильне значення. Введіть ціле число.")

  turtle.setposition(-0.8, 0.6)
  turtle.pendown()

  for _ in range(3):
    draw_koch_curve(turtle, 160, level) 
    turtle.right(120)
    turtle.hideturtle()
    turtle.clone()

if __name__ == "__main__":
  main()