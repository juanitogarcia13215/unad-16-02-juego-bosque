import time
from bosque import bosque
def objeto ():
    print("""elige una opción\n" \
    "1: espada magica\n" \
    "2: escudo encantado\n" \
    "3: posión curativa\n"
    "4: salir""")

    objeto1 = input ("elije un objeto guerrero te lo haz ganado")
    time.sleep(3)

    if objeto1 == "1":
        print("espada de energia, eficaz siempre en el campo de batalla\n")  
        bosque()

    elif objeto1 == "2":
        print("un escudo encantado seria muy util para defenderme de estas criaturas\n")
        bosque()

    elif objeto1 == "3":
        print("!una posión curativa que maravilla¡\n")
        bosque()

    elif objeto1 == "4":
        print("guerrero valeroso nos veremos pronto\n")
    else:
        print("opción no valida elige bien guerrero")
        objeto1()
