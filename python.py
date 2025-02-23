from tkinter import ttk
from tkinter import *
import sqlite3

class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Products application')
        
        # creating a frame container
        frame = LabelFrame(self.wind, text='Register A new Product')
        frame.grid(row=0, column=0, columnspan=3)

        # ID imput
        Label(frame, text='ID: '). grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

          # Name imput
        Label(frame, text='Name: '). grid(row=2, column=0)
        self.name = Entry(frame)
        self.name.grid(row=2, column=1)

         # City imput
        Label(frame, text='City: '). grid(row=3, column=0)
        self.name = Entry(frame)
        self.name.grid(row=3, column=1)


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
