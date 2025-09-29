import time 

derecho = "encontre una criatura deberia negiciar si/no ?"
negociar = "encuentro  el objeto magico"

"--------------------------------------------------bosque----------------------------------------"

def bosque():
    print("en este momento estas en un bosque lleno de criaturas magicas")
    time.sleep(4)
    print("!vaya¡" \
    "¿tengo dos caminos que elegir, cual sera el mas conveniente?" \
    "derecho(1): camino obscuro lo que implica luchar con criaturas" \
    "hizquierdo(2): camino iluminado hay un mnesaje!")
    bosque1 = input ("elige = 1/2")
    negocio = input ("elige si/no")

    if bosque1 == "1":
        derecho()
        if negocio == "si":
            negociar()




        

