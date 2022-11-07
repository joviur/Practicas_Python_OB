import tkinter
import random
from tkinter import ttk

window = tkinter.Tk()

def geometria_grid():
    ### Login de usuario y contraseña:
    window.columnconfigure(0,weight=2)
    window.rowconfigure(1,weight=3)
    # Usuario
    username_label = ttk.Label(window, text='Username:')
    username_label.grid(column=0, row=0,sticky=tkinter.W,padx=5, pady=5)

    username_entry = ttk.Entry(window)
    username_entry.grid(column=1,row=0,sticky=tkinter.E)
    # Contraseña
    password_label = ttk.Label(window, text='Password:')
    password_label.grid(column=0, row=1,sticky=tkinter.W, padx=5, pady=5)

    password_entry = ttk.Entry(window,show='*')
    password_entry.grid(column=1,row=1,sticky=tkinter.E)
    
    #Boton    
    login_button = ttk.Button(window, text='Login')
    login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

def geometria_pack():
    label1 = tkinter.Label(window,text='Label1', background='yellow',foreground='blue')
    label1.pack(ipadx=45, ipady=15)

    label2 = tkinter.Label(window, text='Label2', background='purple',fg='white')
    label2.pack(ipadx=45, ipady=15)

    label3 = tkinter.Label(window, text='Label3', background='blue',fg='white')
    label3.pack(ipadx=45, ipady=15)

    label4 = tkinter.Label(window, text='Label4', background='red',fg='white')
    label4.pack(ipadx=15, ipady=15,side='left')

    label5 = tkinter.Label(window, text='Label5', background='yellow',fg='black')
    label5.pack(ipadx=15, ipady=15,side='left')

    label6 = tkinter.Label(window, text='Label6', background='green',fg='white')
    label6.pack(ipadx=15, ipady=15,side='right')

def geometria_place():
    #Probando he acabado haciendo un generador de arte abstracto:
    colors = ['blue', 'red','yellow','purple', 'green', 'black']
    
    for x in range(0,10):
        color = colors[random.randint(0, len(colors)-1)]
        color2 = colors[random.randint(0, len(colors)-1)]
        ancho = random.randint(0,100)
        alto = random.randint(0,100)
        label = tkinter.Label(window, background=color,foreground=color2, padx=ancho, pady=alto)
        label.place(x=random.randint(0,100), y=random.randint(0,100),)

def componentes():
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=3)
    
    lista = ['Windows', 'MacOS', 'Linux', 'MS-DOS']
    
    listbox = tkinter.Listbox(window, height=50, listvariable=lista)
    listbox.grid(column=0, row=0, sticky=tkinter.W)
    
    frame = ttk.Frame(window,width=800, height=600, relief='sunken')
    label = ttk.Label(frame, text='Hola')
    label.grid(column=0, row=0,sticky=tkinter.W, padx=50, pady=50)
    frame.grid(column=0, row=0, sticky=tkinter.W)
componentes()
window.mainloop()

