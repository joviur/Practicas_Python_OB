import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window,text='¡Hola!', background='yellow',)
label_saludo.pack(ipadx=50, ipady=50, fill='both')
label_adios = tkinter.Label(window, text='¡Adios!', background='red')
label_adios.pack(ipadx=50, ipady=100, fill='both')

window.mainloop()

