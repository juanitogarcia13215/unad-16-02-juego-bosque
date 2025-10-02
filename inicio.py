import time
from bosque import bosque
from objeto import objeto

#-------------------------juan david espitia garcia------------------------------------
#-----------------------ingenieria de sistemas------------------------------------

#---------------------------------inicio del juego----------------------------------- "

def inicio():
    print("¡bienvenido guerrero....!")
    time.sleep(3)
    print("¿estas listo para esta gran aventura?")
    time.sleep(4)
    print("eres el guerrero mas valiente de GLORADIAN, tierra de increibles guerreros")
    time.sleep(4)
    print("pero para convertirte en uno de estos guerreros tendras que pasar varias pruebas:")
    time.sleep(4)
    print("""!Aqui emieza tu aventura y tu decides tu camino:\n" \
    "1: entras al bosque\n" \
    "2: ¿buscar un objeto magico?\n" \
    "3: salir del juego """)
    
    #--------------------------------------------desiciones------------------------------------"
    opcion = input ("elige 1/2/3:\n")

    if opcion == "1":
        bosque()

    elif opcion == "2":
        objeto()

    else:
        print("no te rindas guerrero confio en que lo vas a lograr")
        time.sleep(3)
        print("¿quieres continuar, si/no?")

        opcion2 = input ("elige si o no\n")

        if opcion2 == "si":
            return inicio()

        elif opcion2 == "no":
            print("hasta la proximaaa GUERRERO")
 
if __name__ == "__main__":
    inicio()
   

        


    




    

        
    
    



