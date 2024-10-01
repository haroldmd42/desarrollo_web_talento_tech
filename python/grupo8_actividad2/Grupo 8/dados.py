#Integrantes
#Alexander Arroyo Ceballos
#Juan Felipe Córdoba 
#Kevin Carrillo
#Yan Harold Muñoz Dominguez


import random

class Dado:
    # Valores permitidos para el número de caras
    CARAS_PERMITIDAS = {4, 6, 8, 12, 20}

    def __init__(self, caras=6):
        """Inicializa un dado con el número de caras especificado."""
        if caras in self.CARAS_PERMITIDAS:
            self.caras = caras
        else:
            raise ValueError(f"El dado debe tener una de las siguientes caras: {self.CARAS_PERMITIDAS}")

    def lanzar(self):
        """Genera un valor aleatorio entre 1 y el número de caras del dado."""
        resultado = random.randint(1, self.caras)
        print(f"Se lanzó un dado de {self.caras} caras y salió: {resultado}")
        return resultado

    @staticmethod
    def iniciar_juego():
        """Inicializa el menú principal del juego de dados."""
        print("=== ¡Bienvenido al Juego de los Dados! ===")
        while True:
            print("\nOpciones:")
            print("1. Dos jugadores (1 vs 1)")
            print("2. Jugar contra la máquina (1 vs COM)")
            print("3. Salir")

            try:
                opcion = int(input("Selecciona una opción: "))
                if opcion == 1:
                    Dado.juego_1vs1()
                elif opcion == 2:
                    Dado.juego_1vsCOM()
                elif opcion == 3:
                    print("¡Gracias por jugar! Hasta luego.")
                    break
                else:
                    print("Opción inválida. Por favor, elige 1, 2 o 3.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")

    @staticmethod
    def elegir_caras_jugador(numero_jugador):
        """Permite al jugador elegir el número de caras de su dado."""
        while True:
            try:
                entrada = input(f"Jugador {numero_jugador}, elige el número de caras de tu dado {Dado.CARAS_PERMITIDAS}: ")
                caras = int(entrada)
                if caras in Dado.CARAS_PERMITIDAS:
                    return Dado(caras)
                else:
                    print(f"El número de caras debe ser uno de los siguientes: {Dado.CARAS_PERMITIDAS}")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")

    @staticmethod
    def juego_1vs1():
        """Permite jugar una partida entre dos jugadores."""
        print("\n=== Juego: Dos Jugadores ===")
        nom_jug1 = input("Nombre del Jugador 1: ")
        nom_jug2 = input("Nombre del Jugador 2: ")

        # Elegir dados para cada jugador
        dado_jug1 = Dado.elegir_caras_jugador(1)
        dado_jug2 = Dado.elegir_caras_jugador(2)

        cont_jug1 = 0
        cont_jug2 = 0

        while True:
            print("\n-- Nuevo Lanzamiento --")
            valor1 = dado_jug1.lanzar()
            print(f"{nom_jug1} obtuvo: {valor1}")
            valor2 = dado_jug2.lanzar()
            print(f"{nom_jug2} obtuvo: {valor2}")

            if valor1 > valor2:
                print(f"¡{nom_jug1} gana este lanzamiento!")
                cont_jug1 += 1
            elif valor2 > valor1:
                print(f"¡{nom_jug2} gana este lanzamiento!")
                cont_jug2 += 1
            else:
                print("¡Empate en este lanzamiento!")

            # Preguntar si desean continuar lanzando
            if not Dado.preguntar_repetir_lanzamiento():
                break

        # Determinar el ganador final
        Dado.determinar_ganador(nom_jug1, cont_jug1, nom_jug2, cont_jug2)

    @staticmethod
    def juego_1vsCOM():
        """Permite jugar una partida contra la máquina (COM)."""
        print("\n=== Juego: Jugador vs COM ===")
        nom_jug1 = input("Nombre del Jugador: ")
        nom_jug2 = "COM"

        # Elegir dado para el jugador
        dado_jug1 = Dado.elegir_caras_jugador(1)

        # La máquina elige un dado aleatorio
        caras_com = random.choice(list(Dado.CARAS_PERMITIDAS))
        dado_com = Dado(caras_com)
        print(f"COM ha elegido un dado de {caras_com} caras.")

        cont_jug1 = 0
        cont_com = 0

        while True:
            print("\n-- Nuevo Lanzamiento --")
            valor1 = dado_jug1.lanzar()
            print(f"{nom_jug1} obtuvo: {valor1}")
            valor2 = dado_com.lanzar()
            print(f"{nom_jug2} obtuvo: {valor2}")

            if valor1 > valor2:
                print(f"¡{nom_jug1} gana este lanzamiento!")
                cont_jug1 += 1
            elif valor2 > valor1:
                print(f"¡{nom_jug2} gana este lanzamiento!")
                cont_com += 1
            else:
                print("¡Empate en este lanzamiento!")

            # Preguntar si desean continuar lanzando
            if not Dado.preguntar_repetir_lanzamiento():
                break

        # Determinar el ganador final
        Dado.determinar_ganador(nom_jug1, cont_jug1, nom_jug2, cont_com)

    @staticmethod
    def preguntar_repetir_lanzamiento():
        """Pregunta al usuario si desea realizar otro lanzamiento."""
        while True:
            respuesta = input("¿Deseas realizar otro lanzamiento? (Y/N): ").strip().upper()
            if respuesta == 'Y':
                return True
            elif respuesta == 'N':
                return False
            else:
                print("Opción inválida. Por favor, responde con 'Y' o 'N'.")

    @staticmethod
    def determinar_ganador(nombre1, puntos1, nombre2, puntos2):
        """Determina y muestra el ganador final de la partida."""
        print("\n=== Resultado Final ===")
        print(f"{nombre1}: {puntos1} puntos")
        print(f"{nombre2}: {puntos2} puntos")

        if puntos1 > puntos2:
            print(f"¡{nombre1} es el ganador de la partida!")
        elif puntos2 > puntos1:
            print(f"¡{nombre2} es el ganador de la partida!")
        else:
            print("¡La partida termina en empate!")

        # Preguntar si desean jugar de nuevo
        while True:
            jugar_de_nuevo = input("¿Desean jugar de nuevo? (Y/N): ").strip().upper()
            if jugar_de_nuevo == 'Y':
                return
            elif jugar_de_nuevo == 'N':
                print("¡Gracias por jugar! Hasta luego.")
                exit()
            else:
                print("Opción inválida. Por favor, responde con 'Y' o 'N'.")

# Ejecutar el juego
if __name__ == "__main__":
    Dado.iniciar_juego()
