import numpy
import GUI
import re

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


eingabe = input("Spieler 1: ")
spieler1 = eingabe
eingabe = input("Spieler 2: ")
spieler2 = eingabe
spielfeld = numpy.zeros((8,8))  #Spielfeld[zeile][spalte]
print(spielfeld)
currspieler = 1

#GUI.grid()

while(True):
    
    if currspieler == 1:
        print(spieler1, "ist an der Reihe") 
        eingabe = input("Spalte: ")   
    if currspieler == 2:
        print(spieler2, "ist an der Reihe")
        eingabe = input("Spalte: ")            
    if eingabe == "stop":
        break

    if re.findall(r'[1-8]',eingabe): #RegEx Überprüfung, ob Eingabe zwischen 1 und 8. Wenn nicht, erneute Abfrage
        pass
    else:
        continue

    if Spielzug(spielfeld,currspieler,int(eingabe)-1): #Wenn Spielzug = True, steht ein Gewinner fest, sonst läuft Spielzug Methode durch
        if currspieler == 1:
            print(spieler1 , " hat gewonnen")
        elif currspieler == 2:
            print(spieler2 , " hat gewonnen")

        eingabe = input("wollt ihr nochmal spielen? (Y/N)")
        if eingabe == "Y" or "y":
            spielfeld = numpy.zeros((8,8))
        else:
            exit()

    else: #Wechsel der Spieler
      if currspieler == 1:
        currspieler = 2
      else:
         currspieler = 1





