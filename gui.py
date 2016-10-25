from tkinter import *

from wallpaperactual import *

master = Tk()


def command1():
    print("HI")


def quit():
    master.quit()


okay = Button(master, anchor=W, text="Fix Wallpaper!", command=testmain)
okay.pack()
quit = Button(master, command=quit, text="Quit!", fg="red", bg="black")
quit.pack_propagate(0)
quit.pack()

mainloop()
