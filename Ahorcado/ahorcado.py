import random
import csv

def obtener_palabra(nombre_archivo : str) -> str:
    with open(nombre_archivo, 'r', encoding='utf8') as archivo:
        palabra =  random.choice(archivo.readlines()).strip().lower()
        return palabra

def desplegar_tablero(palabra : str, correctas : list, incorrectas : list) -> None:
    impr_cuerpo = ''
    contador1 = 0
    contador2 = 0    
    print ("""
----
    l
    l    """    )

    cuerpo = ['    O ', '\n', '  /', '-', 'I', '-', '\\', '\n', '    I' , '\n' ,'   l', ' ', 'l', '\n', '   o', ' ', 'o']
    while contador2 != len(incorrectas):
        impr_cuerpo += cuerpo[contador1]

        if cuerpo[contador1] != ' ' and cuerpo[contador1] != '\n':
            contador2 += 1
        contador1 += 1


    print(impr_cuerpo)

    print(f'Palabra: ')
    res = ''
    for letra in palabra:
        if letra in correctas:
            res += letra
        elif not letra.isalpha():
            res +=  letra
        else:
            res += '_'

    print(f'Palabra Actual: {res}')

def tirada(palabra : str, letra : str, correctas : list, incorrectas : list) -> bool:
    if len(letra) != 1 or not letra.isalpha():
        return False
    if letra in correctas + incorrectas:
        return False
    else:
        if letra in palabra:
            correctas.append(letra)
            print(f"La letra {letra} esta en la palabra")
        else:
            incorrectas.append(letra)
            print (f"La letra {letra} no esta en la palabra")
        return True

def juego_terminado(palabra : str, correctas : list, incorrectas : list) -> tuple:
    if len(incorrectas) == 11:
        return True, "perdiste"
    for letra in palabra:
        if letra.isalpha() and letra not in correctas:
            return False, ""
    return True, "ganaste"

def registrar_marcador(nombre : str, puntaje : int) -> None:
    with open ("Leaderboard.csv", "a", newline='', encoding="utf8") as leaderboard:
        writer = csv.writer(leaderboard)
        writer.writerow([nombre, puntaje])
        return

def registro_top5(orden: str) -> list:
        
        with open ("Leaderboard.csv" , "a", encoding="utf8") as leaderboard:
            reader = csv.reader(leaderboard)
            for i in reader:
                nombre, puntaje = i[0], int(i[1])
                scores.append((nombre, puntaje))
                
                if orden == "ascendente":
                    scores = sorted(scores, key=lambda x: x[1])  # Ordenar de menor a mayor
                elif orden == "descendente":
                    scores = sorted(scores, key=lambda x: x[1], reverse=True)  # Ordenar de mayor a menor

            # Obtener el top 5
            top5 = scores[:5]  # Tomar los primeros 5 registros

            return top5
        
def juego():
    palabra = obtener_palabra("palabras.txt") 
    correctas = []
    incorrectas = []
    
    terminado = juego_terminado(palabra, correctas, incorrectas)
    while not terminado[0]:
        desplegar_tablero(palabra, correctas, incorrectas)
        letra = input("letra: ").lower().strip()
        while not tirada(palabra, letra, correctas, incorrectas):
            print("Letra incorrecta.")
            letra = input("letra: ").lower().strip()

def menu():
    while (opcion := input("""Ahorcado
1) Jugar
2) Mostrar leaderboard
3) Salir
Seleccione una opción: """).strip()) != "3":
        if opcion == "1":
            juego()          
            
if __name__ == "__main__":
    menu()
