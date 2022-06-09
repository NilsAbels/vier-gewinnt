import numpy

def Spielzug(spielfeld,spieler,spalte):
    print(spielfeld)
    print(spieler)
    if spielfeld[0][spalte] != 0:
        print("zug nicht möglich")
    for i in range(0, len(spielfeld)):
        if i == len(spielfeld) - 1:
            spielfeld[i][spalte] = spieler
            if CheckGewinnervert(spieler, spielfeld, spalte, i) or CheckGewinnerhorizontal(spieler,spielfeld,i):
                print("gewonnen")
            break
        elif spielfeld[i+1][spalte] != 0:
            spielfeld[i][spalte] = spieler
            if CheckGewinnervert(spieler, spielfeld, spalte, i) or CheckGewinnerhorizontal(spieler,spielfeld,i):
                print("gewonnen")
            break

    print(spielfeld)


def CheckGewinnervert(spieler, spielfeld, spalte, zeile):
    activeRow = True
    rowcount = 0
    while(activeRow):   #vertikale Überprüfung
        if(zeile == len(spielfeld)):    #reihe außerhalb des Spielfelds
            return False
        if spielfeld[zeile][spalte] == spieler:
            rowcount += 1
        else:
            activeRow = False

        if rowcount >= 4:
            return True
        zeile += 1



def CheckGewinnerhorizontal(spieler, spielfeld, zeile):
    zaehler = 0
    for s in range(0, len(spielfeld[zeile])):

        if spielfeld[zeile][s] == spieler:
            zaehler += 1
        else:
            zaehler = 0
        if zaehler == 4:
            return True

    return False



def CheckGewinnerhorizontal(spieler,spielfeld,zeile,spalte):




spielfeld = numpy.zeros((8,8))  #spieldfeld[zeile][spalte]
spieler = 1
while(True):
    eingabe = input("Spalte: ")
    if eingabe == "stop":
        break
    Spielzug(spielfeld,spieler,int(eingabe)-1)
    if spieler == 1:
        spieler = 2
    else:
        spieler = 1





