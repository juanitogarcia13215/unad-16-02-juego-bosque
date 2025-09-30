from objeto import objeto
import time 


derecho = "encontre una criatura deberia negiciar si/no ?"
negociar = "encuentro  el objeto magico"

#--------------------------------------------------bosque----------------------------------------

def bosque():
    print("en este momento estas en un bosque lleno de criaturas magicas")
    time.sleep(4)
    print("!vaya¡\n" \
    "¿tengo dos caminos que elegir, cual sera el mas conveniente?\n" \
    "derecho(1): camino obscuro lo que implica luchar con criaturas\n" \
    "hizquierdo(2): camino iluminado hay un mnesaje!\n")
    bosque1 = input ("toma tu desición guerrero = hizquierdo:(1)\n derecho:(2)\n")

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
        print()