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
canvas.pack(side='left')

button1 = tkinter.Button(mainWindow, text="Button1")
button2 = tkinter.Button(mainWindow, text="Button2")
button3 = tkinter.Button(mainWindow, text="Button3")
button1.pack(side='left', anchor='n')
button2.pack(side='left', anchor='s')
button3.pack(side='left', anchor='e')
mainWindow.mainloop()