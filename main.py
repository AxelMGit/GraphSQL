import mysql.connector
from mysql.connector import Error

import tkinter
from tkinter import *
from tkinter import simpledialog
from tkinter.simpledialog import askinteger


window = Tk()

#window.withdraw()

#user = simpledialog.askstring("Connection", "Veuillez entrer l'utilisateur :", parent=window, show='*')
#password = simpledialog.askstring("Connection", "Veuillez entrer le mot de passe :", parent=window, show='*')
user = "user"
password = "password"
cb = ""

#window.deiconify()

window.geometry("300x300")
label = Label(window, text="SQL Actions")
label.pack()


Button(window, text='SELECT * FROM NSI.Film',command=lambda *args: sqlexec(1)).pack()

Button(window, text='SELECT * FROM NSI.Pays',command=lambda *args: sqlexec(2)).pack()

Button(window, text='SELECT * FROM NSI.PaysFilm',command=lambda *args: sqlexec(3)).pack()



def sqlexec(exec_action):
    if exec_action == 1:
        global sql_action
        sql_action = 'SELECT * FROM NSI.Film'
        window.destroy()
    elif exec_action == 2:
        global sql_action
        sql_action = 'SELECT * FROM NSI.Film'
        window.destroy()
    elif exec_action == 3:
        global sql_action
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
print(sql_action)
result = cursor.execute(sql_action)
cb = cursor.fetchall()
print(cb)


















