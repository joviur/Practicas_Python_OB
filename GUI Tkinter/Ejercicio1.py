# Ejercicio 1 GUI - Lista Desplegable
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Lista desplegable")
window.geometry('300x300')

def etiqueta():
    etiq = tkinter.Label(window, text='Selecciona tu S.O: ')
    etiq.grid(column=0, row=0)

def lista_desplegable():
    lista_desplegable = ttk.Combobox(window,width=17, values=['Windows','Linux','MacOS','Android','Otros...'], state='readonly' )
    lista_desplegable.grid(column=1, row=0)
    
etiqueta()
lista_desplegable()

window.mainloop()

