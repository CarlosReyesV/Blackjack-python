import random

Cartas_Mesero = []
Cartas_Jugador = []

# A = 1
# J,Q,K = 10,10,10

Ae, Ac, Ad, At = 1,1,1,1
e2, c2, d2, t2 = 2,2,2,2
e3, c3, d3, t3 = 3,3,3,3
e4, c4, d4, t4 = 4,4,4,4
e5, c5, d5, t5 = 5,5,5,5
e6, c6, d6, t6 = 6,6,6,6
e7, c7, d7, t7 = 7,7,7,7
e8, c8, d8, t8 = 8,8,8,8
e9, c9, d9, t9 = 9,9,9,9
e10, c10, d10, t10 = 10,10,10,10
Je, Jc, Jd, Jt = 10,10,10,10
Qe, Qc, Qd, Qt = 10,10,10,10
Ke, Kc, Kd, Kt = 10,10,10,10

# BARAJA = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K,
#           A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K,
#           A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K,
#           A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]

BARAJA = [Ae ,e2, e3, e4, e5, e6, e7, e8, e9, e10, Je, Qe, Ke,
          Ac ,c2, c3, c4, c5, c6, c7, c8, c9, c10, Jc, Qc, Kc,
          Ad ,d2, d3, d4, d5, d6, d7, d8, d9, d10, Jd, Qd, Kd,
          At ,t2, t3, t4, t5, t6, t7, t8, t9, t10, Jt, Qt, Kt]
        
def REVELAR_C_M():
    for x in range(len(Cartas_Mesero)):
        carta_N =""
        carta = dict(globals())
        for nombre in carta:
            if carta[nombre] is Cartas_Mesero[1]:
                carta_N = nombre
                break
        print(carta_N)
        break
    
def REVELAR_C_J():
    for x in range(len(Cartas_Jugador)):
        carta_N =""
        carta = dict(globals())
        for nombre in carta:
            if carta[nombre] is Cartas_Jugador[x]:
                carta_N = nombre
        print(carta_N)


def TOMAR_CARTA_MESERO():
    Carta_M = random.choice(BARAJA)
    Cartas_Mesero.append(Carta_M)
    BARAJA.remove(Carta_M)

def TOMAR_CARTA_JUGADOR():
    Carta_J = random.choice(BARAJA)
    Cartas_Jugador.append(Carta_J)
    BARAJA.remove(Carta_J)

def BLACK():
    #BARAJAS
    while len(Cartas_Mesero) <2:
        TOMAR_CARTA_MESERO()
        if len(Cartas_Mesero) ==2:
            print("El Mesero tiene ? y:", Cartas_Mesero[1])
            # Imprimir la baraja del mesero
            REVELAR_C_M()

    while len(Cartas_Jugador) <2:
        TOMAR_CARTA_JUGADOR()
        if len(Cartas_Jugador) ==2:
            print("El Jugador tiene:", sum(Cartas_Jugador), Cartas_Jugador)
            # Imprimir la baraja del jugador
            REVELAR_C_J()

    #SUMA de las cartas
    if sum(Cartas_Mesero) ==21:
        print("Gana la casa, sacó 21, sus cartas fueron: ")
        # Imprimir la baraja del mesero
        REVELAR_C_M()
        quit()
    elif sum(Cartas_Mesero) >21:
        print("Gana el jugador, sacó 21 :)")
        # Imprimir la baraja del jugador
        print("Tus cartas fueron: ")
        REVELAR_C_J()
        quit()

#JUEGO
    while sum(Cartas_Jugador) < 21:
        accion = str(input("¿Juegas o Pasas? " ))
        if (accion == "Juego") or (accion == "juego") or (accion == "Si") or (accion == "si"):
            TOMAR_CARTA_JUGADOR()
            print("Tienes: " + str(sum(Cartas_Jugador)) +" "," De:", Cartas_Jugador)
            REVELAR_C_J()
        else:
            if(sum(Cartas_Mesero) <16):
                TOMAR_CARTA_MESERO()
            print("El Mesero tiene: " + str(sum(Cartas_Mesero)) + " De:", Cartas_Mesero)
            print("Tienes: " + str(sum(Cartas_Jugador)) + " De:", Cartas_Jugador)
            if sum(Cartas_Mesero) > sum(Cartas_Jugador) and sum(Cartas_Mesero) <= 21:
                # Imprimir la baraja del mesero
                print("El Mesero GANA!, sus cartas fueron: ")
                REVELAR_C_M()
                print("Tus cartas fueron: ")
                REVELAR_C_J()
                break
            elif sum(Cartas_Mesero) == sum(Cartas_Jugador):
                print("Empate")
                break
            else:
                # Imprimir la baraja del jugador
                print("TU GANAS!")
                print("Tus cartas fueron: ")
                REVELAR_C_J()
                break

    if sum(Cartas_Jugador) > 21:
        # Imprimir la baraja del jugador
        print("Perdiste, El Mesero GANA con "+ str(sum(Cartas_Mesero)))
        print("Tus cartas fueron: ")
        REVELAR_C_J()
    elif sum(Cartas_Jugador) == 21:
        # Imprimir la baraja del jugador
        print("Tienes 21! GANASTE")
        print("Tus cartas fueron: ")
        REVELAR_C_J()

BLACK()