import turtle
import time


def s(n, m):
    if n == 0:
        turtle.color('black')
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(m)
            turtle.left(90)
        turtle.end_fill()

    else:
        for _ in range(4):
            s(n - 1, m / 3)
            turtle.forward(m / 3)

            s(n - 1, m / 3)
            turtle.forward(m / 3)

            turtle.forward(m / 3)
            turtle.left(90)


turtle.tracer(10)
depth=int(input("Введите глубину фрактала "))
t = time.perf_counter()
s(depth, 400)
print("Алгоритм Кнута-Морриса-Пратта: {0:.6f} сек".format ((time.perf_counter() - t)))
turtle.done()
