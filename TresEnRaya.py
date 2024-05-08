import random

def comenzar_juego():
   jugadores = [[input("Nombre del Jugador 1: "), "X"], [input("Nombre del Jugador 2: "), "O"]]
   jugador_inicial = random.randint(0, 1)
   tablero = [["-" for _ in range(3)] for _ in range(3)]
   return True, jugadores, jugador_inicial, tablero

def actualizar_tablero(jugador, fila, columna, tablero):
   while True:
       if 1 <= fila <= 3 and 1 <= columna <= 3:
           if tablero[fila - 1][columna - 1] == "-":
               tablero[fila - 1][columna - 1] = jugador[1]
               break
           else:
               print("Casilla ocupada. Por favor, elige otra coordenada.")
       else:
           print("Coordenadas inválidas. Por favor, elige otras coordenadas.")
       fila, columna = list(map(int, input("Indica las coordenadas: Fila y Columna (Dos dígitos): ")))

   return tablero

def tablero_completo(tablero):
   return all(c != "-" for fila in tablero for c in fila)

def comprobar_ganador(jugador, tablero):
   for i in range(3):
       if all(tablero[i][j] == jugador[1] for j in range(3)):
           return True

   for i in range(3):
       if all(tablero[j][i] == jugador[1] for j in range(3)):
           return True

   if all(tablero[i][i] == jugador[1] for i in range(3)):
       return True

   if all(tablero[i][2 - i] == jugador[1] for i in range(3)):
       return True

   return False

juego_en_curso, jugadores, jugador_inicial, tablero = comenzar_juego()

print("\nCOMIENZA EL JUEGO:\n")
print("\t-", jugadores[0][0], "juega con la letra", jugadores[0][1])
print("\t-", jugadores[1][0], "juega con la letra", jugadores[1][1])
print()

while juego_en_curso:
   if tablero_completo(tablero):
       juego_en_curso = False
       print("FIN DEL JUEGO. NO HAY GANADOR")
       break

   print("\nTURNO DE JUEGO DE:", jugadores[jugador_inicial][0])

   print("  0 1 2")
   for i, fila in enumerate(tablero):
       print(i, " ".join(fila))

   fila, columna = list(map(int, input("INDICA LAS COORDENADAS: FILA Y COLUMNA (Dos dígitos): ")))

   tablero = actualizar_tablero(jugadores[jugador_inicial], fila, columna, tablero)
   print()

   if comprobar_ganador(jugadores[jugador_inicial], tablero):
       juego_en_curso = False
       print("  0 1 2")
       for i, fila in enumerate(tablero):
           print(i, " ".join(fila))
       print("EL GANADOR ES:", jugadores[jugador_inicial][0], "CON LA LETRA", jugadores[jugador_inicial][1])

   jugador_inicial ^= 1