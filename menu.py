import os
from Funciones import *
from data import *

seguir = True

while seguir:
    os.system("cls")

    print("   ***Menu de Opciones***   ")
    print("Punto 0.2")
    print("Punto 0.3")
    print("Punto 0.4")
    print("Punto 0.5")
    print("Punto 0.6")
    print("Punto 0.7")
    print("Punto 0.8")
    print("Punto 1.1")
    print("Punto 1.12")
    print("Punto 1.13")
    print("Punto 1.14")
    print("Punto 1.15") 
    print("cerrar menu / 2")


    opcion = input("Ingrese opcion: ")

    match opcion:

        case "0.2":
            nombres_Super(lista_heroes)

        case "0.3":
            nombre_y_altura(lista_heroes)
        
        case "0.4":
            super_mas_alto(lista_heroes)

        case "0.5":
            super_mas_bajo(lista_heroes)

        case "0.6":
            promedio_altura(lista_heroes)

        case "0.7":
            maximos_y_minimos_altura(lista_heroes)

        case "0.8":
            maximos_y_minimos_peso(lista_heroes)

        case "1.1":
            nombres_masculino(lista_heroes)
        
        case "1.2":
            nombres_femenino(lista_heroes)

        case "1.3":
            super_mas_alto_masculino(lista_heroes)

        case "1.4":
            super_mas_alto_femenino(lista_heroes)
        
        case "1.5":
            super_mas_bajo_M(lista_heroes)

        case "1.6":
            super_mas_bajo_F(lista_heroes)

        case "1.7":
            promedio_altura_M(lista_heroes)

        case "1.8":
            promedio_altura_F(lista_heroes)
        
        case "1.9":
            nombres_3_al_6(lista_heroes)

        case "1.10":
            contar_colores_ojos(lista_heroes)
        
        case "1.11":
            contar_colores_pelo(lista_heroes)
        
        case "1.12":
            contar_inteligencia(lista_heroes)

        case "1.13":
            listar_nombres_ojos(lista_heroes)
        
        case "1.14":
            listar_nombres_pelo(lista_heroes)
        
        case "1.15":
            listar_nombres_inteligencia(lista_heroes)

        


        case "2":
            seguir = False
    
    os.system("pause")