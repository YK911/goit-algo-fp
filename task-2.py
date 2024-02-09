"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""

import turtle


def draw_pifagor_tree(branch_len, level):
    if level == 0:
        return
    turtle.forward(branch_len)
    turtle.right(45)
    draw_pifagor_tree(0.7 * branch_len, level - 1)
    turtle.left(90)
    draw_pifagor_tree(0.7 * branch_len, level - 1)
    turtle.right(45)
    turtle.backward(branch_len)


def main():
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("blue")
    turtle.left(90)
    draw_pifagor_tree(branch_len=80, level=8)  # set branch length and recursion level
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
