import tkinter
from tkinter import ttk


def main():

    window = tkinter.Tk()

    window.columnconfigure(1, weight=3)

    frameTitulo = ttk.Frame(window)
    frameTitulo.grid(column=1, row=0, sticky=tkinter.W, pady=10, padx=10)

    titulo = tkinter.Label(frameTitulo, text='Elija una interfaz:', bg='grey',fg='white')
    titulo.grid(sticky=tkinter.W)

    frameLista = ttk.Frame(window)
    frameLista.grid(column=1, row=1, pady=0, padx=10)

    lista = ["PyFTK","PyQT","wxPython","Tkinter"]
    listaSeleccionable = tkinter.StringVar(value=lista)
    listBox = tkinter.Listbox(frameLista, height=10,width=25,listvariable=listaSeleccionable)
    listBox.grid(column=1, row=3, sticky=tkinter.W)


    window.mainloop()



if __name__ == "__main__":
    main()