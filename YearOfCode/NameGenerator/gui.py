#!/usr/bin/env python      1
import Tkinter as tk
import NameGenerator

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()
        self.generateButton = tk.Button(self, text='Generate!',
            command=NameGenerator.generate)
        self.generateButton.grid()


app = Application()
app.master.title('Name Generator')
app.mainloop()