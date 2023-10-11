import random
import csv

def crear_tablero() -> dict:
    # tablero = {}
    # for i in range(1,10):
    #     tablero[f"{i}"] = " "
    # return tablero
    return {f"{i}": " " for i in range(1,10)}

def imprimir_tablero(tablero : dict) -> None:
    print(f""" {tablero['1']} | {tablero['2']} | {tablero['3']}
 ---------
 {tablero['4']} | {tablero['5']} | {tablero['6']}
 ---------
 {tablero['7']} | {tablero['8']} | {tablero['9']}""")
    
def casillas_disponibles(tablero : dict) -> list:
    # disponibles = []
    # for casilla in tablero:
    #     if tablero[casilla] == " ":
    #         disponibles.append(casilla)
    # return disponibles
    return [casilla for casilla in tablero if tablero[casilla] == " "]
    
def juego_terminado(tablero : dict) -> tuple: # (bool, string)
    casos = [[f"{i}",f"{i+1}",f"{i+2}"] for i in [1,4,7]] + \
             [[f"{i}",f"{i+3}",f"{i+6}"] for i in [1,2,3]] +\
             [["1","5", "9"], ["3","5","7"]]
    for caso in casos:
        if tablero[caso[0]] != " " and tablero[caso[0]] == tablero[caso[1]] == tablero[caso[2]]:
            return True, tablero[caso[0]]
    if not casillas_disponibles(tablero):
        return True, None
    return False, None

# def obtener_ganadas(partida : dict) -> int:
#     return partida["ganadas"]

def guardar_marcador(nombre : str, ganadas : int, perdidas : int, empatadas : int) -> None:
    marcadores = []
    with open("leaderboard.csv", "r", encoding="utf8") as archivo:
        lector = csv.DictReader(archivo)
        marcadores = [fila for fila in lector]
    marcadores.append({
        "nombre": nombre,
        "ganadas": ganadas,
        "perdidas": perdidas,
        "empatadas": empatadas
    })
    # marcadores.sort(key=obtener_ganadas)
    marcadores.sort(key=lambda x: int(x["ganadas"]), reverse=True)
    with open("leaderboard.csv", "w", encoding="utf8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "ganadas", "perdidas", "empatadas"])
        escritor.writeheader()
        escritor.writerows(marcadores)

def mostrar_leaderboard():
    with open("leaderboard.csv", "r", encoding="utf8") as archivo:
        lector = csv.DictReader(archivo)
        for linea in lector:
            print(f"Nombre: {linea["nombre"]} - Ganadas: {linea["ganadas"]} - Perdidas: {linea["perdidas"]} - Empatadas: {linea["empatadas"]}")
    
def jugar():
    partidas_ganadas = 0
    partidas_perdidas = 0
    partidas_empatadas = 0
    seguir_jugando = "1"
    while seguir_jugando == "1":
        while (figura_jugador := input("Elige tu figura (x,o): ").strip().lower()) not in ["x", "o"]:
            print("Debes elegir entre: (x,o).")
        # if figura_jugador == "x":
        #     figura_maquina = "o"
        # else:
        #     figura_maquina = "x"
        figura_maquina = "o" if figura_jugador == "x" else "x"
        
        # 1 -> jugador, 2 -> máquina
        turno = random.randint(1,2)
        tablero = crear_tablero()
        terminado, ganador = juego_terminado(tablero)
        while not terminado:
            imprimir_tablero(tablero)
            disponibles = casillas_disponibles(tablero)
            if turno == 1:
                print(f"Las casillas disponibles son: {', '.join(disponibles)}")
                while (tirada := input("Ingresa la casilla en la que deseas tirar: ").strip()) not in disponibles:
                    print("Debes elegir una casilla disponible.")
                    print(f"Las casillas disponibles son: {', '.join(disponibles)}")
                tablero[tirada] = figura_jugador
                turno = 2
            else:
                print("Turno de la máquina.")
                tirada = random.choice(disponibles)
                tablero[tirada] = figura_maquina
                turno = 1
            terminado, ganador = juego_terminado(tablero)
        print("Tablero final:")
        imprimir_tablero(tablero)
        if ganador == figura_jugador:
            print("Has ganado.")
            partidas_ganadas += 1
        elif ganador == figura_maquina:
            print("Has sido derrotado.")
            partidas_perdidas += 1
        else:
            print("Ha sido un empate.")
            partidas_empatadas += 1
        
        while (seguir_jugando := input("¿Desea seguir jugando? 1)Sí, 2)No: ").strip()) not in ["1", "2"]:
            print("Debe elegir 1 para sí o 2 para no.")
    nombre = input("Introduce tu nombre: ")
    print(f"Ganaste {partidas_ganadas} veces.")
    print(f"Perdiste {partidas_perdidas} veces.")
    print(f"Empataste {partidas_empatadas} veces.")
    guardar_marcador(nombre, partidas_ganadas, partidas_perdidas, partidas_empatadas)
    
    
def menu_principal() -> None:
    while (opcion := input("""Menú principal:
1) Jugar
2) Ver leaderboard
3) Salir
Ingrese la opción deseada: """).strip()) != "3":
        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_leaderboard()
        elif opcion == "3":
            print("Hasta pronto.")
        else:
            print("Debe ingresar una opción válida.")

if __name__ == "__main__":
    menu_principal()