from bosque import bosque
from objeto import objeto
from fin import fin 
import time 


#---------------------------------inicio del juego----------------------------------- "

def inicio():
    print("¡bienvenido guerrero....!")
    time.sleep(3)
    print("¿estas listo para esta gran aventura?")
    time.sleep(4)
    print("selecciona una opción:" \
    "1: entras al bosque" \
    "2: ¿buscar un objeto magico?" \
    "3: salir del juego ")
    
    #--------------------------------------------desiciones------------------------------------"
    opcion = input ("elige 1/2/3")

    if opcion == "1":
        bosque()

    elif opcion == "2":
        objeto()

    else:
        print("no te rindas guerrero confio en que lo vas a lograr")
        time.sleep(3)
        print("¿quieres continuar, si/no?")

        opcion2 = input ("elige si o no ")

        if opcion2 == "si":
            inicio()

        elif opcion2 == "no":
            fin()
 


        


    




    

        
    
    



