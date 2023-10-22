import data

#0.2
def nombres_Super(lista):
    for heroes in lista:
        nombres = heroes["nombre"]
        print(nombres)


#0.3
def nombre_y_altura(lista):
    for heroes in lista:
        nombres = heroes["nombre"]
        alturas = float(heroes["altura"])
        print("Superhéroe: {}, Altura: {:.2f}".format(nombres, alturas))

#0.4 
def super_mas_alto(lista):
    mas_alto = 0
    nombre_mas_alto = None
    for heroes in lista:
        altura = heroes["altura"]
        altura = float(altura)
        nombre = heroes["nombre"]

        if altura > mas_alto:
            mas_alto = altura
            nombre_mas_alto = nombre

    print(f"El super mas alto es {nombre_mas_alto} y mide {mas_alto}")

#0.5
def super_mas_bajo(lista):
    mas_bajo = float("inf")
    nombre_mas_bajo = None
    for heroes in lista:
        altura = heroes["altura"]
        altura = float(altura)
        nombre = heroes["nombre"]

        if altura < mas_bajo:
            mas_bajo = altura
            nombre_mas_bajo = nombre
    print(f"El super mas bajo es {nombre_mas_bajo} y mide {mas_bajo}")
    
#0.6
def promedio_altura(lista):
    alturas = []
    for heroes in lista:
        altura = heroes["altura"]
        altura = float(altura)
        alturas.append(altura)
        
        promedio = sum(alturas) / len(alturas)
    print(f"El promedio de altura es de {promedio}")

#0.7
def maximos_y_minimos_altura(lista):
    super_mas_alto(lista)
    super_mas_bajo(lista)

#0.8
def maximos_y_minimos_peso(lista):
    menos_pesado = float("inf")
    nombre_menos_pesado = None
    for heroes in lista:
        peso = heroes["peso"]
        peso = float(peso)
        nombre = heroes["nombre"]

        if peso < menos_pesado:
            menos_pesado = peso
            nombre_menos_pesado = nombre  
    
    mas_pesado = 0
    nombre_mas_pesado = None
    for heroes in lista:
        peso = heroes["peso"]
        peso = float(peso)
        nombre = heroes["nombre"]

        if peso > mas_pesado:
            mas_pesado = peso
            nombre_mas_pesado = nombre  

    print(f"El mas pesado es {nombre_mas_pesado}, mientras que el menos es {nombre_menos_pesado}")

#1.1
def nombres_masculino(lista):
    for heroes in lista:
        genero = heroes["genero"]
        nombres = heroes["nombre"]
        if genero == "M":
            print(nombres)
        
#1.2
def nombres_femenino(lista):
    for heroes in lista:
        genero = heroes["genero"]
        nombres = heroes["nombre"]
        if genero == "F":
            print(nombres)

#1.3
def super_mas_alto_masculino(lista):
    mas_alto = 0
    nombre_mas_alto = None
    for heroes in lista:
        altura = heroes["altura"]
        altura = float(altura)
        nombre = heroes["nombre"]
        genero = heroes["genero"]

        if genero == "M" and altura > mas_alto:
            mas_alto = altura
            nombre_mas_alto = nombre

    print(f"El super mas alto masculino es {nombre_mas_alto} y mide {mas_alto}")

#1.4
def super_mas_alto_femenino(lista):
    mas_alto = 0
    nombre_mas_alto = None
    for heroes in lista:
        altura = heroes["altura"]
        altura = float(altura)
        nombre = heroes["nombre"]
        generos = heroes["genero"]

        if generos == "F" and altura > mas_alto:
            mas_alto = altura
            nombre_mas_alto = nombre

    print(f"El super mas alto femenino es {nombre_mas_alto} y mide {mas_alto}")
      
#1.5
def super_mas_bajo_M(lista):
    mas_bajo = float("inf")
    nombre_mas_bajo = None
    for heroes in lista:
        generos = heroes["genero"]
        altura = heroes["altura"]
        altura = float(altura)
        nombre = heroes["nombre"]

        if generos == "M" and altura < mas_bajo:
            mas_bajo = altura
            nombre_mas_bajo = nombre
    print(f"El super mas bajo masculino es {nombre_mas_bajo} y mide {mas_bajo}")
    
#1.6
def super_mas_bajo_F(lista):
    mas_bajo = float("inf")
    nombre_mas_bajo = None
    for heroes in lista:
        generos = heroes["genero"]
        altura = heroes["altura"]
        altura = float(altura)
        nombre = heroes["nombre"]

        if generos == "F" and altura < mas_bajo:
            mas_bajo = altura
            nombre_mas_bajo = nombre
    print(f"El super mas bajo femenino es {nombre_mas_bajo} y mide {mas_bajo}")
    
#1.7
def promedio_altura_M(lista):
    alturas = []
    for heroes in lista:
        altura = heroes["altura"]
        altura = float(altura)
        generos = heroes["genero"]
        
        if generos == "M":
            alturas.append(altura)

    promedio = sum(alturas) / len(alturas)
    print(f"El promedio de altura masculina es de {promedio}")

#1.8
def promedio_altura_F(lista):
    alturas = []
    for heroes in lista:
        altura = heroes["altura"]
        altura = float(altura)
        generos = heroes["genero"]
        
        if generos == "F":
            alturas.append(altura)

    promedio = sum(alturas) / len(alturas)
    print(f"El promedio de altura femenina es de {promedio}")

#1.9
def nombres_3_al_6 (lista):
    print(super_mas_alto_masculino(lista))
    print(super_mas_alto_femenino(lista))
    print(super_mas_bajo_M(lista))
    print(super_mas_bajo_F(lista))

#1.10
def contar_colores_ojos(lista):
    colores_ojos = {}
    
    for heroe in lista:
        ojos = heroe["color_ojos"].lower() 
        if ojos in colores_ojos:
            colores_ojos[ojos] += 1
        else:
            colores_ojos[ojos] = 1
    print(colores_ojos)

#1.11
def contar_colores_pelo(lista):
    colores_pelo = {}
    
    for heroe in lista:
        pelo = heroe["color_pelo"].lower() 
        if pelo in colores_pelo:
            colores_pelo[pelo] += 1
        else:
            colores_pelo[pelo] = 1
    print(colores_pelo)

#1.12
def contar_inteligencia(lista):
    lista_inteligencia = {}
    
    for heroe in lista:
        inteligencia = heroe["inteligencia"].lower()
        
        if not inteligencia:
            inteligencia = "No Tiene"
        
        if inteligencia in lista_inteligencia:
            lista_inteligencia[inteligencia] += 1
        else:
            lista_inteligencia[inteligencia] = 1
    print(lista_inteligencia)

#1.13
def listar_nombres_ojos(lista):
    lista_ojos = {}
    
    for heroe in lista:
        ojos = heroe["color_ojos"].lower()
        
        if ojos in lista_ojos:
            lista_ojos[ojos].append(heroe["nombre"])
        else:
            lista_ojos[ojos] = [heroe["nombre"]]

    print(lista_ojos)

#1.14
def listar_nombres_pelo(lista):
    lista_pelo = {}
    
    for heroe in lista:
        pelo = heroe["color_pelo"].lower()
        
        if pelo in lista_pelo:
            lista_pelo[pelo].append(heroe["nombre"])
        else:
            lista_pelo[pelo] = [heroe["nombre"]]

    print(lista_pelo)

#1.15
def listar_nombres_inteligencia(lista):
    lista_inteligencia = {}
    
    for heroe in lista:
        inteligencia = heroe["inteligencia"].lower()
        
        if not inteligencia:
            inteligencia = "No Tiene"
        
        if inteligencia in lista_inteligencia:
            lista_inteligencia[inteligencia].append(heroe["nombre"])
        else:
            lista_inteligencia[inteligencia] = [heroe["nombre"]]

    print(lista_inteligencia)
