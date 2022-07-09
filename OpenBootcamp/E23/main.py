

import sqlite3


def main():
    busqueda("Diego Armando")
    
    
    
def busqueda(nombre):
    conn = sqlite3.connect("E23/escuela.db")
    cursor = conn.cursor()

    query = f'SELECT * FROM Alumnos WHERE nombre="{nombre}"'
    rows = cursor.execute(query)
    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()


def main2():
    insertaAlumnos(1,"Lionel", "Messi")
    insertaAlumnos(2,"Sergio Leonel", "Aguero")
    insertaAlumnos(3,"Gabriel Omar", "Batistuta")
    insertaAlumnos(4,"Diego Armando", "Maradona")
    insertaAlumnos(5,"Claudio Paul", "Caniggia")
    insertaAlumnos(6,"Lucas", "Biglia")
    insertaAlumnos(7,"Daniel", "Garnero")
    insertaAlumnos(8,"Cristian Gabriel", "Romero")


def insertaAlumnos(id,nombre,apellido):
    conn = sqlite3.connect("E23/escuela.db")
    cursor = conn.cursor()

    query = 'INSERT INTO Alumnos(idAlumno, nombre, apellido) VALUES(?,?,?)'
    rows = cursor.execute(query, (id, nombre, apellido))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()