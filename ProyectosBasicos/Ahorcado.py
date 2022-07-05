import random
import string

# from palabras import palabras para importar de otras clase o archivos py

palabras = ["aire", "ojos", "piel", "anteojos", "joven", "viejo", "alto", "bajo", "pequeño", "gordo", "delgado", "bella", "azul", "verde", "negro", "sombrero", "guantes", "corbata", "gemelos", "paraguas", "plata", "oro", "perla", "diamante", "esmeralda", "anillo", "pulsera", "reloj", "elegante", "sencillo", "chaqueta", "traje", "camisa", "zapatos", "pelo", "maquillaje", "peine", "dedo", "hueso", "cara", "ojo", "calor", "ambulancia", "enfermera", "farmacia", "vitaminas", "pastillas", "dentista", "ciego", "correr", "caminar", "regresar", "saltar", "fin", "cerrar", "nombre", "mujer", "hombre", "soltero", "novio", "nacer", "vivir", "edad", "anciana","trabajar", "cobrar", "azafata", "artista", "panadero", "carpintero", "cocinero", "maestro", "bombero", "juez", "modelo", "monje", "pintor", "piloto", "secretaria", "taxista", "escritor", "jefe", "aprendiz", "jubilado", "empleo", "industria", "taller", "tienda", "vacaciones", "sueldo", "impuesto", "huelga", "obedecer", "locura", "humor", "inteligencia", "orgullo", "timidez", "valiente", "aburrido", "loco", "divertido", "bueno", "feliz", "amable", "pobre", "serio", "extraño", "gritar", "llorar", "suspirar", "preocupado", "risa", "amor", "suerte", "enamorado", "ver", "apagar", "luz", "color", "lupa", "microscopio", "claro", "cantar", "silbar", "voz", "eco", "trueno", "altavoz", "radio", "auricular", "liso", "comer", "dulce", "salado", "perfume", "despertarse", "vestirse", "desayunar", "leer", "dormirse", "toalla", "cobija", "almuerzo", "sopa", "agua", "leche", "jugo", "sal", "pimienta", "vinagre", "ajo", "perejil", "menta", "canela", "mayonesa", "pan", "mantequilla", "miel", "manzana", "pera", "durazno", "cereza", "papa", "lechuga", "arroz", "pollo", "pavo", "hamburguesa", "camarones", "tortilla", "espagueti", "sopa", "helado", "chocolate", "galletas", "bombones", "limpiar", "cortar", "hervir", "planchar", "aspiradora", "plancha", "horno", "abrelatas", "vajilla", "vaso", "cafetera", "azucarera", "comprar", "gastar", "vender", "barato", "caro", "gratis", "cliente", "bolsa", "precio", "recibo", "ascensor", "esquiar", "ciclismo", "golf", "pelota", "tenis", "bicicleta", "estadio", "gol", "torneo", "leer", "dibujar", "cantar", "bailar", "libro", "revista", "clavo", "cine", "pala", "cocina", "hielo", "coro", "piano", "cartas", "pesca", "radio", "noticias", "televisor", "documental", "anuncio", "aplaudir", "teatro", "circo", "mago", "disco", "portero", "propina", "regalo", "fiesta", "vela", "alfombra", "puerta", "ventana", "cortina", "escritorio", "cuadro", "juguete", "alquiler", "mudanza", "casa", "pared", "chimenea", "comedor", "plaza", "calle", "estacionamiento", "parque", "puente", "puerto", "edificio", "escuela", "museo", "estatua", "fuente", "turista", "mendigo", "manejar", "acelerar", "frenar", "cruzar", "reparar", "conductor", "multa", "atasco", "carretera", "peaje", "curva", "florecer", "campo", "bosque", "huerto", "selva", "tronco", "rama", "flor", "hoja", "musgo", "cedro", "roble", "pino", "nogal", "naranjo", "tallo", "clavel", "margarita", "amapola", "rosa", "girasol", "violeta", "gato", "perro", "vaca", "pato", "oveja", "conejo", "pez", "oso", "jirafa", "erizo", "mariposa", "foca", "tigre", "cobra", "almeja", "paloma", "cisne", "mosquito", "hormiga", "llover", "nevar", "nublado", "soleado", "clima", "rayo", "nieve", "sol", "viento", "padre", "madre", "hijo", "abuela", "estudioso", "aula", "tiza", "regla", "computadora", "diccionario"]


def obtenerPalabraValida(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()


vidasDiccionarioVisual = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }


def ahorcado():
    print("##################################")
    print("      Bienvenido(a) al Juego")
    print("##################################")

    palabra = obtenerPalabraValida(palabras)

    letrasPorAdivinar = set(palabra) # "palabra" = {'p','a','l','a','b','r','a'}
    letrasAdivinadas = set()
    letrasABCdario = set(string.ascii_uppercase) # sin ñ

    vidas = 7

    while len(letrasPorAdivinar) > 0 and vidas > 0:
        if vidas > 1:
            print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letrasAdivinadas)}")
        else:
            print(f"Te queda {vidas} vida y has usado estas letras: {' '.join(letrasAdivinadas)}")
        # Mostrar el estado actual de la plabra

        palabraLista = [letra if letra in letrasAdivinadas else '-' for letra in palabra]
        print(vidasDiccionarioVisual[vidas])
        print(f"Palabra : {' '.join(palabraLista)}")

        letraUsuario = input("Elija una letra: ").upper()

        if letraUsuario in letrasABCdario - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)

            if letraUsuario in letrasPorAdivinar:
                letrasPorAdivinar.remove(letraUsuario)
                print()
            else:
                vidas -= 1
                print(f"Tu letra {letraUsuario} no se encuentra en la palabra.")
        elif letraUsuario in letrasAdivinadas:
            print("\nLetra escogda anteriormente.")
        else:
            print("\nLetra o caracter no válido.")

    if vidas > 0:
        print(f"¡Ganaste! La palabra es {palabra}")
    else:
        print(vidasDiccionarioVisual[vidas])
        print(f"¡Ahoracado! Has perdido el juego, la palabra es {palabra}")


ahorcado()