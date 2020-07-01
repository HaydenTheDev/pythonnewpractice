try:
    import tkinter
except ImportError:
    import tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello how are you")
mainWindow.geometry("640x400")
label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button1.pack(side='top', anchor='n')
button2.pack(side='top', anchor='s')
button3.pack(side='top', anchor='e')
mainWindow.mainloop()