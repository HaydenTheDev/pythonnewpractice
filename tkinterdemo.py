try:
    import tkinter
except ImportError:
    import tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello how are you")
mainWindow.geometry("640x400")
label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left', fill=tkinter.Y)
mainWindow.mainloop()