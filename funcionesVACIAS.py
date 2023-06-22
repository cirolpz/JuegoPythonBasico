from email.headerregistry import ParameterizedMIMEHeader
from fileinput import close
from principal import *
from configuracion import *

import random
import math

#Agrega, elimina, pone color, y mueve los paises en pantalla
def actualizar(paisesEnPantalla,posiciones,listaPaises,color,totaltime):
    eliminar(posiciones,paisesEnPantalla,color)#llamamos a la funcion que elimina a los paises que se pasen de la pantalla
    for indice in range (0,len(posiciones)-1):#se calcula cuantos paises hay en la pantalla
        if indice==7: #Eliminamos el primer valor de cada lista cuando hay muchos paises en pantalla
            paisesEnPantalla.pop(0)
            posiciones.pop(0)
            color.pop(0)
        else:
            pass
    #Creamos dos valores randoms entre un rango permitido por la pantalla:
    ranx=random.randrange(100,650)
    rany=random.randrange(100,470)
    elem=(ranx,rany)
    mover(posiciones,totaltime)#se llama a la funcion que realiza el movimiento de los paises
    if estaCerca(elem,posiciones) and (ranx,rany) not in posiciones:#Si los rangos no son iguales o estan cercas de una posicion
        porColor(color)        
        posiciones.append((ranx,rany))#agregamos los valores en forma de tupla a la lista posiciones
        paisesEnPantalla.append(nuevoPais(listaPaises))#agregamos un pais aleatorio en la lsita paisesEnPantalla

#Elimina cuando una pais se pasa de la pantalla
def eliminar(posiciones,paisesEnPantalla,color):
    indice=0
    for i in posiciones:
        if i[0]>660 or i[1]>500:#i es una tupla, seleccionamos el valor 0 y valor 1 de i, indicamos q si es mayor al tamaño de la pantalla sea eliminado
            paisesEnPantalla.pop(indice)
            posiciones.pop(indice)
            color.pop(indice)
        indice+=1

#Mueve a los paises a una velocidad dependiendo del tiempo
def mover(posiciones,totaltime):
    indice=0
    primera=61
    segunda=25
    tercera=15
    for i in posiciones:
        if totaltime<=primera and totaltime>segunda:
            respuesta=(i[0]+3,i[1]+3)#guardamos en la variable respuesta la tupla modeificada para hacer q la palabra se mueva
            posiciones.pop(indice)#eliminamos la tupla recibida para despues agregarle otro valor
#utilizamos la funcion insert de python, permite cambiar el valor de una lista indicando el indice y luego el valor nuevo            
            posiciones.insert(indice,respuesta)
        elif totaltime<=segunda and totaltime>tercera:
            respuesta=(i[0]+6,i[1]+6)
            posiciones.pop(indice)
            posiciones.insert(indice,respuesta)
        elif totaltime<=tercera:
            respuesta=(i[0]+10,i[1]+10)
            posiciones.pop(indice)
            posiciones.insert(indice,respuesta)
        indice+=1

#detecta si una posicion random esta cerca de una posicion ya creada para no generarla y evitar sobreposicion
def estaCerca(elem, lista):
    for i in lista:
#En la variable espacio guardamos la suma de los valores originales de la tupla con un valor minimo para crear un espacio entre palabras
#en la otra vairable es lo mismo pero restamos para marcar el lado izquierdo y abajo       
        espacio=(i[0]+80,i[1]+20)
        espacio2=(i[0]-80,i[1]-20)
        if elem > espacio2  and elem < espacio :#Si el valor random está cerca de algun pais devolvera falso
            espacio=0#ponemos los valores en 0 para que la funcion sea reutilizable
            espacio2=0
            return False#devuelve False si es que el elemento random está a una distancia cercana de otro
        espacio=0
        espacio2=0
    return True#Si llego hasta aquí es por que es una posicion segura

#Controla que se genere en pantalla un pais random
def nuevoPais(paises):
        nuevosPaises=longitudMinima(paises)
        numAlea=random.randrange(0,len(nuevosPaises))
        return nuevosPaises[numAlea]#Retorna un país aleatorio que esté en la lista paises

#añadimos longitud minima de caracteres de un pais y eliminamos la ñ
def longitudMinima(listaPaises):
    nuevosPaises=[]#creamos una nueva lista con los paises adecuados
    for pais in listaPaises:
        if pais in 'ñ' or len(pais)<=5:#si el pais contiene ñ o tiene menos de 5 letas no será agregado
            pass
        else:
            nuevosPaises.append(pais)
    return nuevosPaises

#añadimos color random por pais
def porColor(color):
    r=random.randint(0,200)
    g=random.randint(0,200)
    b=random.randint(0,200)
    colores=(r,g,b)
    color.append(colores)
    
#Eliminamos los paises en pantalla con su posicion y color si coincide con la palabra candidata
def quitar(candidata, paisesEnPantalla, posiciones,color):
    cont=0
    for i in paisesEnPantalla:
        if candidata.upper() == i:#hacemos a candidata mayuscula para que pueda ser comparada con la lista que están en mayuscula
            paisesEnPantalla.pop(cont)
            posiciones.pop(cont)
            color.pop(cont)
        cont+=1

#Si la palabra candidata está en pantalla devolverá True
def esValida(candidata, listaPaises, paisesEnPantalla):
    if candidata.upper() in paisesEnPantalla and candidata.upper() in listaPaises:
        return True
    efectosDeSonido(0)
    return False#La palabra candidata no forma parte de paisesEnPantalla o no se encuentra en la lista de paises que se utilizaron

#Agregamos sonido si la palabra es incorrecta, correcta y si es correcta y complicada
def efectosDeSonido(puntos):
    sonidoCorrecto=pygame.mixer.Sound("sonido correcto.mp3")#creamos un objeto de sonido para ser usada posteriormente
    sonidoSuperCorrecto=pygame.mixer.Sound("sonido supercorrecto.mp3")
    sonidoIncorrecto=pygame.mixer.Sound("sonido incorrecto.mp3")
    if puntos == 0:
        sonidoIncorrecto.play()#ejecuta la variable sonidoIncorrecto
    elif puntos == 1:
        sonidoCorrecto.play()#ejecuta la variable sonidoCorrecto
    elif puntos == 3:
        sonidoSuperCorrecto.play()#ejecuta la variable sonidoSuperCorrecto
    else:
        pass

#calcula los puntos correspondientes a cada palabra
def Puntos(candidata):
    vocal="aeiou"#guardamos en las variables los valores correspondientes guiandonos con el pdf
    consonanteDificil="jkqwxyz"
    consonante="bcdfghklmnprstuv"
    puntajeTotal=0
    candidataMin=candidata.lower()#Hacemos minuscula a candidata para compararla con  las variables que están en minuscula
    for puntosLetra in candidataMin:#recorremos el pais para comprar la letra con las variables
        if puntosLetra in consonanteDificil:# si puntosLetra está en la variable consonanteDificil
            puntajeTotal=puntajeTotal+5
        elif puntosLetra in consonante:
            puntajeTotal=puntajeTotal+2
        elif  puntosLetra in vocal:
            puntajeTotal=puntajeTotal+1
    if puntajeTotal>10:
        efectosDeSonido(3)
    else:
        efectosDeSonido(1)
    return puntajeTotal#DEVOLVEMOS LA PUNTUACION TOTAL DE LA PALABRA

#Procesamos la informacion recibida de principal.py para ver si candidata es correcta, cuantos puntos recibe, ejecutar sonido y eliminarla
def procesar(candidata, listaPaises, paisesEnPantalla,posiciones,color):
    if esValida(candidata,listaPaises,paisesEnPantalla):#Si esValida es True
        quitar(candidata, paisesEnPantalla, posiciones,color)#Se elimina la palabra de la pantalla
        return Puntos(candidata)#Devuelve los puntos que se suman en total
    else:
#Si contesta mal retorna 0 puntos, sabemos q no entro en el if porque el if retorna un valor lo que hace que no se lea esta parte del codigo
        return 0