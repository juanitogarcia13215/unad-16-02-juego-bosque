import time
from objeto import objeto

derecho = "encontre una criatura deberia negiciar si/no ?"
negociar = "encuentro  el objeto magico"
#--------------------------------------------------bosque----------------------------------------
def bosque():
    print("en este momento estas en un bosque lleno de criaturas magicas")
    time.sleep(4)
    print("!vaya¡\n" \
    "¿tengo dos caminos que elegir, cual sera el mas conveniente?\n" \
    "derecho(1): camino obscuro lo que implica negociar o luchar con criaturas\n" \
    "hizquierdo(2): camino iluminado donde hay un mnesaje!\n")

    bosque1 = input ("toma tu desición guerrero = hizquierdo:(1)-----derecho:(2)----negociar(3)\n")
#-----------------------------------------------desición luchar o negosear--------------------------------
    if bosque1 == "1":
        print("decidiste luchar contra las criaturas de este inospito bosque\n")
        time.sleep(2)
        print("!LUCHAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        time.sleep(10)
        print("............\n.....................\n...................\n...............\n")
        time.sleep(3)
        print("pierdes 10 puntos de vida pero tienes la oportunidad de elegir un objeto magico:\n")
        objeto()

    elif  bosque1 == "2":
        print("haz llegado  a un pozo, por o cual si desansas obtienes vida\n ¿que desición tomaras guerreto?")
        descansar = input ("descansar si---/---No\n")
        if  descansar == "si":
            print("recuperaste puntos de vida guerrero continua tu viaje")
            bosque1()

        elif descansar == "no":
            print("¡contunuaste tu camino guerrero!")
            bosque1()

        else:
            print("opción invalida selecciona una correcta")

    elif bosque1 == "3":
        print("decides negociar con la criatura por lo cual encuentras un objeto magito pero................\n")
        print("debes elegir una de las  3 cosas")
        objeto()

    else:
        print("opción incorrecta intenta de nuevo")
        bosque1()
    