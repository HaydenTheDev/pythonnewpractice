try:
    import tkinter
except ImportError:
    import tkinter as tkinter


def parabola(x):
    y = x * x
    return y


mainWindow = tkinter.Tk()


mainWindow.title("Parabola")
mainWindow.geometry("640x400")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)


for x in range(-100, 100):
    y = parabola(x)
    print(y)

mainWindow.mainloop()