try:
    import tkinter
except ImportError:
    import tkinter as tkinter
import math


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, -y)

#  Modify the circle function so that it allows the color of the circle
#  to be specified and defaults to red if a color is not given.
#  You may want to review the previous lectures.


def circle(page, radius, g, h, color="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius,
                     outline=color, width=2)



def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin,
                                 x_origin, y_origin))
    page.create_line(-x_origin, 0,
                     x_origin, 0, fill="white")
    page.create_line(0, y_origin, 0,
                     -y_origin, fill="white")
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="purple")


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480, background="black")
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, "green")
circle(canvas, -100, -100, -100, "blue")
mainWindow.mainloop()
