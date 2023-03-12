#Haciendo un Juego de Ping Pong basico con pygame en # pasos

#1- importar e Iniciar las librerias
import pygame
pygame.init()
import sys


#2- Creo constantes con el alto y ancho de la pantalla
ANCHO = 800
ALTO = 600


#3- Establezco Varios colores por si los llego a necesitar
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


#4- Establezco el tamaño de las paletas/jugadores
heigth = 90
width = 15


#5- Establezco la ubicación del Jugador 1, 2 y la pelota
coordXP1 = 50
coordYP1 = 300-45
speedYP1 = 0

coordXP2 = 750
coordYP2 = 300-45
speedYP2 = 0

coordBallX = 400
coordBallY = 300
speedBallY = 3
speedBallx = 3


#6- Inicio la ventana del juego, tambien añado un clock
#**El clock servira más tarde 
screen = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()


#7- Una variable para Terminar/Cerrar el programa
gameOver = False


#8- Empieza a correr el juego
while not gameOver:

    #9- Propiedad para cerrar la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True


        #10- Controles de movimiento
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_w:
            speedYP1 = -3 
           if event.key == pygame.K_s:
            speedYP1 = 3

           if event.key == pygame.K_UP:
            speedYP2 = -3  
           if event.key == pygame.K_DOWN:
            speedYP2 = 3

        if event.type == pygame.KEYUP:
           if event.key == pygame.K_w:
            speedYP1 = 0 
           if event.key == pygame.K_s:
            speedYP1 = 0

           if event.key == pygame.K_UP:
            speedYP2 = 0  
           if event.key == pygame.K_DOWN:
            speedYP2 = 0

    #11- Movimiento de la pelota
    if coordBallY > 590 or coordBallY < 10 :
        speedBallY *= -1

    if coordBallX > 800 or coordBallX < 0:
        coordBallX = 400
        coordBallY = 300
        speedBallx *= -1


    #12- Aplicamos los movimientos en relación al controls
    coordYP1 += speedYP1
    coordYP2 += speedYP2
    coordBallY += speedBallY
    coordBallX += speedBallx


    #13- Coloreamos el fondo de la pantalla
    screen.fill(BLACK)


    #14- Implementamos a el Jugador 1, 2, y la pelota
    p1 = pygame.draw.rect(screen, BLUE, (coordXP1,coordYP1 , width, heigth))
    p2 = pygame.draw.rect(screen, RED, (coordXP2,coordYP2, width, heigth))
    ball = pygame.draw.circle(screen, WHITE,(coordBallX, coordBallY), 10)


    #15- Hacemos que la pelota rebote
    if ball.colliderect(p1) or ball.colliderect(p2):
        speedBallx *= -1


    #16- Una regla para que nada salga de las pantallas
    if coordYP1 < 0 :
        coordYP1 = 0
    if coordYP1 > 510 :
        coordYP1 = 510


    if coordYP2 < 0 :
        coordYP2 = 0
    if coordYP2 > 510 :
        coordYP2 = 510
        

    #17- Aplicamos los cambios y ponemos los fotogramas por segundo/FPS
    pygame.display.flip()
    clock.tick(120)


#16- Finalizamos el programa
pygame.quit()