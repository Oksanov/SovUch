import turtle as t
# t = t.Turtle()
# t.shape("turtle")
# t.speed(1)
def triangle():
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.right(135)
def square():
    for i in range(8):
        t.forward(100)
        t.left(90)
def reset():
    t.home()
    t.clear()
square()
# reset()
# triangle()

# t.screen.exitonclick()
# t.screen.mainloop()
