import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    level = int(input("Рівень рекурсії: "))
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    koch_snowflake(t, 400, level)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
