import turtle
import time

class Segment:
    def __init__(self, t, color, dt):
        self.t = t
        self.t.color(color)
        self.t.penup()
        self.t.setheading(0)
        self.t.goto(0, 0)
        self.t.pensize(10)
        self.dt = dt

    def draw(self, digit):
        if digit == 0:
            self.t.goto(-50, 100)
            self.t.pendown()
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.forward(100)
            self.t.right(90)
            self.t.penup()

        if digit == 1:
            self.t.goto(50, 100)
            self.t.pendown()
            self.t.right(90)
            self.t.forward(100)
            self.t.forward(100)
            self.t.left(90)
            self.t.penup()

        if digit == 2:
            self.t.goto(-50, 100)
            self.t.pendown()
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.forward(100)
            self.t.penup()

        if digit == 3:
            self.t.goto(-50, 100)
            self.t.pendown()
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.forward(-100)
            self.t.left(90)
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.left(90)
            self.t.penup()

        if digit == 4:
            self.t.goto(-50, 100)
            self.t.pendown()
            self.t.right(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.forward(100)
            self.t.forward(-100)
            self.t.forward(-100)
            self.t.right(90)
            self.t.penup()

        if digit == 5:
            self.t.goto(-50, 100)
            self.t.pendown()
            self.t.forward(100)
            self.t.forward(-100)
            self.t.right(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.left(90)
            self.t.penup()

        if digit == 6:
            self.draw(5)
            self.t.goto(-50, 0)
            self.t.pendown()
            self.t.right(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.penup()
        
        if digit == 7:
            self.t.goto(-50, 100)
            self.t.pendown()
            self.t.forward(100)
            self.t.forward(-100)
            self.draw(1)

        if digit == 8:
            self.draw(0)
            self.t.goto(-50, 0)
            self.t.pendown()
            self.t.forward(100)
            self.t.penup()

        if digit == 9:
            self.draw(5)
            self.t.goto(50, 100)
            self.t.pendown()
            self.t.right(90)
            self.t.forward(100)
            self.t.left(90)
            self.t.penup()

    def clear(self):
        self.t.clear()

    def my_delay(self):
        start =  time.time()
        while time.time() - start < self.dt:
            pass
