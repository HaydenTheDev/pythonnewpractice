try:
    import tkinter
except ImportError:
    import tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)


mainWindow = tkinter.Tk()

mainWindow.title("Hello how are you")
mainWindow.geometry("640x400")
mainWindow.mainloop()