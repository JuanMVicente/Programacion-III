
import tkinter
from tkinter import ttk


def main():
    window = tkinter.Tk()

    window.columnconfigure(1, weight=3)

    selected = tkinter.StringVar()
    r1 = ttk.Radiobutton(window, text="Victoria", value='victoria', variable=selected)
    r2 = ttk.Radiobutton(window, text="Empate", value='empate', variable=selected)
    r3 = ttk.Radiobutton(window, text="Derrota", value='derrota', variable=selected)
    clean = tkinter.Button(window, text="Limpiar")  
    
    # Me gustaría dejarlo como una funcion global, pero por la variable selected se me complicaba
    def reiniciar(event):
        selected.set(None)
    clean.bind('<Button-1>', reiniciar)

    r1.grid(column=0, row=1, pady=10, padx=10)
    r2.grid(column=0, row=2, pady=10, padx=10)
    r3.grid(column=0, row=3, pady=10, padx=10)
    clean.grid(column=1, row=2, pady=10, padx=10)


    window.mainloop()
    


if __name__ == "__main__":
    main()