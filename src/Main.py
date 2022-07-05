from imp import reload
import numpy
import re
import pygame
import sys
import math

#Definition der Farben für GUI
BLUE = (0,0,255)
BLACK = (0,0,0)    
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)


def Spielzug(spielfeld,spieler,spalte):

    if spielfeld[0][spalte] != 0: #falls Spalte bereits gefüllt ist
        print("zug nicht möglich")

    for i in range(0, len(spielfeld)):
        if i == len(spielfeld) - 1: #Überprüfung, ob unterste Zeile
            spielfeld[i][spalte] = spieler
            print(spielfeld)
            if CheckGewinnervert(spieler, spielfeld, spalte) or CheckGewinnerhorizontal(spieler,spielfeld,i) or CheckGewinnerDiagonal(spieler,spielfeld,i,spalte): #Überprüfung, ob Gewinnbedingung erfüllt
                return True
            break
        elif spielfeld[i+1][spalte] != 0: #Spalte wird nach unten durchiteriert, Überprüfung ob nächstes Feld besetzt 
            spielfeld[i][spalte] = spieler
            print(spielfeld)
            if CheckGewinnervert(spieler, spielfeld, spalte) or CheckGewinnerhorizontal(spieler,spielfeld,i) or CheckGewinnerDiagonal(spieler,spielfeld,i,spalte):
                return True
            break


def CheckGewinnervert(spieler, spielfeld, spalte):

    zaehler = 0

    for s in range(0,len(spielfeld)): #Spalte wird nach unten durchiteriert, Überprüfung, ob 4 mal nacheinander selber Spieler
        if spielfeld[s][spalte] == spieler: 
            zaehler += 1
        else:
            zaehler = 0
        if zaehler == 4:
            return True
    return False


def CheckGewinnerhorizontal(spieler, spielfeld, zeile):

    zaehler = 0

    for s in range(0, len(spielfeld[zeile])): #Zeile wird nach rechts durchiteriert, Überprüfung, ob 4 mal nacheinander selber Spieler

        if spielfeld[zeile][s] == spieler:
            zaehler += 1
        else:
            zaehler = 0
        if zaehler == 4:
            return True
    return False


def CheckGewinnerDiagonal(spieler,spielfeld,zeile,spalte):

     zaehler = 0
     startZ = zeile
     startS = spalte

     while(startS > 0 and startZ > 0): #Zeilen und/oder Spaltenwert werden an Rand des Speielfelds gesetzt, um ganze Diagonale zu überprüfen -> Verschiebung nach oben links
         startZ -= 1
         startS -= 1

     while(startS < len(spielfeld[zeile]) and startZ < len(spielfeld)): #Durchiterieren der jeweiligen Diagonale von oben links nach unten rechts. Überprüfung, ob 4 mal nacheinander selber Spieler
         if spielfeld[startZ][startS] == spieler:
             zaehler += 1
         else:
             zaehler = 0
         if zaehler == 4:
            return True
         startZ += 1
         startS += 1

     zaehler = 0
     startZ = zeile
     startS = spalte

     while (startS > 0 and startZ < len(spielfeld) - 1 ): #Zeilen und/oder Spaltenwert werden an Rand des Speielfelds gesetzt, um ganze Diagonale zu überprüfen -> Verschiebung nach unten links
         startZ += 1
         startS -= 1

     while (startS < len(spielfeld[zeile]) and startZ  > 0 ): #Durchiterieren der jeweiligen Diagonale von unten links nach oben rechts. Überprüfung, ob 4 mal nacheinander selber Spieler
         if spielfeld[startZ][startS] == spieler:
             zaehler += 1
         else:
             zaehler = 0
         if zaehler == 4:
             return True
         startZ -= 1
         startS += 1

     return False

def draw_spielfeld(spielfeld): #Aufbau des Spielfelds
	for s in range(len(spielfeld)):
		for z in range(len(spielfeld[0])):
			pygame.draw.rect(screen, BLUE, (s*quadrat, z*quadrat+quadrat, quadrat, quadrat)) #Rechtecke, oben eine Zeile frei
			pygame.draw.circle(screen, BLACK, (int(s*quadrat+quadrat/2), int(z*quadrat+quadrat+quadrat/2)), radius) #Kreise in den Rechtecken
	
	for s in range(len(spielfeld)): #Chips der 2 Spieler
		for z in range(len(spielfeld[0])):		
			if spielfeld[z][s] == 1:
				pygame.draw.circle(screen, RED, (int(s*quadrat+quadrat/2), int(z*quadrat+quadrat/2)), radius) #Spieler 1: Roter Chip
			elif spielfeld[z][s] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(s*quadrat+quadrat/2), int(z*quadrat+quadrat/2)), radius) #Spieler 2: Gelber Chip
	pygame.display.update()


spielfeld = numpy.zeros((8,8))  #Spielfeld[zeile][spalte]

pygame.init()

print(spielfeld)

#Definition der Maße für GUI
quadrat = 100
radius = int(quadrat/2 - 4)

breite = len(spielfeld) * quadrat
hoehe = len(spielfeld[0] + 1) * quadrat
size = (breite, hoehe)

fonttype = pygame.font.SysFont("Bauhaus 93", 40) #Schriftart der Texte

currspieler = 1
ende = False

#Anzeigen des Spielfelds
screen = pygame.display.set_mode(size)
draw_spielfeld(spielfeld)
pygame.display.update()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Zum Schließen des Programms
            sys.exit()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #Neustart des Spiels bei Taste SPACE
                    spielfeld = numpy.zeros((8,8))

        if event.type == pygame.MOUSEMOTION: #Wenn Maus sich bewegt
            pygame.draw.rect(screen, BLACK, (0,0, breite, quadrat)) #Schwarzer Block in oberster Zeile, damit Spur nicht bleibt
            xpos = event.pos[0] #Scannen der X-Achsen-Position des Mauszeigers (Zwischen 0 und 799)
            if currspieler == 1:
                pygame.draw.circle(screen, RED, (xpos, int(quadrat/2)), radius) #Anzeige des Chips in oberster Spalte
            else:
                pygame.draw.circle(screen, YELLOW, (xpos, int(quadrat/2)), radius)
            pygame.display.update()
            
        if event.type == pygame.MOUSEBUTTONDOWN: #Wenn Maus geklickt
            pygame.draw.rect(screen, BLACK, (0,0, breite, quadrat))
            
            if currspieler == 1:
                print("Rot ist an der Reihe") 
                #eingabe = input("Spalte: ")   
                #spalte = int(eingabe)-1
                xpos = event.pos[0]
                spalte = int(math.floor(xpos/quadrat)) #Teilen der X-Achsen-Position durch die Breite eines Quadrats (x/100) -> Erkennen welche Spalte

            if currspieler == 2:
                print(" Gelb ist an der Reihe")
                #eingabe = input("Spalte: ")  
                #spalte = int(eingabe)-1   
                xpos = event.pos[0]
                spalte = int(math.floor(xpos/quadrat))       

            #if re.findall(r'[1-8]',eingabe): #RegEx Überprüfung, ob Eingabe zwischen 1 und 8. Wenn nicht, erneute Abfrage
            #    pass
            #else:
            #    print('Bitte gültige Spalte eingeben)
            #    continue

            if Spielzug(spielfeld,currspieler,spalte): #Wenn Spielzug = True, steht ein Gewinner fest, sonst läuft Spielzug Methode durch
                
                if currspieler == 1:
                    print("Rot hat gewonnen")
                    draw_spielfeld(spielfeld)
                    label = fonttype.render("SPIELER 1 HAT GEWONNEN!!!", 1, RED) #Ausgabe der Gewinn-Message
                    screen.blit(label, (170,25))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    
                elif currspieler == 2:
                    print("Gelb hat gewonnen")
                    draw_spielfeld(spielfeld)
                    label = fonttype.render("SPIELER 2 HAT GEWONNEN!!!", 1, YELLOW)
                    screen.blit(label, (170,25))
                    pygame.display.update()
                    pygame.time.wait(3000)
 
                ende = True

            else: #Wechsel der Spieler
                if currspieler == 1:
                    currspieler = 2
                else:
                    currspieler = 1

        draw_spielfeld(spielfeld)

        if ende == True:
            pygame.draw.rect(screen, BLACK, (0,0, breite, quadrat))
            label = fonttype.render("NOCHMAL? -> SPACE   ENDE? -> BACKSPACE", 1, WHITE)
            screen.blit(label, (20,25))
            pygame.display.update()
            pygame.event.wait()

            if event.type == pygame.KEYDOWN: #Neustart bei Taste SPACE
                if event.key == pygame.K_SPACE:
                    spielfeld = numpy.zeros((8,8))
                    ende = False

                if event.key == pygame.K_BACKSPACE: #Schließen bei Taste BACKSPACE                    
                    sys.exit()  
                         
                

        
 
 