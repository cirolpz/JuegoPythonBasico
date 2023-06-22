#! /usr/bin/env python
import os, random, sys, math
#importa la libreria pygame y los archivos que vamos a usar
import pygame
from pygame.locals import *
from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"#Es un objeto de mapeo que representa las variables ambientales del usuario. Objeto de mapeo: convierte tipos de datos oorientados a objetos a sistema de base de datos relacional 
        pygame.init()#pantalla inicial
        #pygame.mixer.init()


        #Preparar la ventana
        pygame.display.set_caption("Lopez Ciro")#nombre del programa
        screen = pygame.display.set_mode((ANCHO, ALTO))#Se crea la superficie de visualizacion

        #tiempo total del juego
        gameClock = pygame.time.Clock()#crear un objeto para ayudar a controlar el tiempo
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial

        color= []
        puntos = 0
        candidata = ""
        listaPaises = []
        posiciones = []
        paisesEnPantalla=[]

        archivo= open("paises.txt","r")#Abrimos el archivo de paises en modo lectura, lo recorremos y guardamos sus valores en listaPaiese
        for linea in archivo.readlines():
            listaPaises.append(linea[0:-1])#Sacamos el \n

        dibujar(screen, candidata, paisesEnPantalla, posiciones, puntos,segundos,color)
        
        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
            	fps = 2

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(candidata, listaPaises, paisesEnPantalla,posiciones,color)
                        candidata = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)
            #Dibujar de nuevo todo
            dibujar(screen, candidata, paisesEnPantalla, posiciones, puntos, segundos,color)

            pygame.display.flip()#actualiza pantalla
            actualizar(paisesEnPantalla, posiciones, listaPaises,color,segundos)


        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Pirncipal ejecuta Main
if __name__ == "__main__":
    main()
