import mysql.connector
from mysql.connector import Error

import tkinter
from tkinter import *
from tkinter import simpledialog
from tkinter.simpledialog import askinteger


window = Tk()

user = simpledialog.askstring("Connection", "Veuillez entrer l'utilisateur :", parent=window, show='*')
password = simpledialog.askstring("Connection", "Veuillez entrer le mot de passe :", parent=window, show='*')
callback = ""

window.geometry("300x300")
label = Label(window, text="SQL Actions")
label.pack()

##

Button(window, text='SELECT * FROM NSI.Film',command=lambda *args: sqlexec(1)).pack()

Button(window, text='SELECT * FROM NSI.Pays',command=lambda *args: sqlexec(2)).pack()

Button(window, text='SELECT * FROM NSI.PaysFilm',command=lambda *args: sqlexec(3)).pack()

##

def sqlexec(exec_action):
    global sql_action
    if exec_action == 1:
        sql_action = 'SELECT * FROM NSI.Film'
        window.destroy()
    elif exec_action == 2:
        sql_action = 'SELECT * FROM NSI.Film'
        window.destroy()
    elif exec_action == 3:
        sql_action = 'SELECT * FROM NSI.Film'
        window.destroy()


window.mainloop()


connection = mysql.connector.connect(
                host="164.132.67.138",
                database="NSI",
                user=user,
                passwd=password
            )

cursor = connection.cursor()
result = cursor.execute(sql_action)

callback = cursor.fetchall()
print(callback)


















