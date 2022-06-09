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


def CheckGewinnervert(spieler,spielfeld,spalte,reihe):
    activeRow = True
    rowcount = 0
    while(activeRow):   #vertikale Überprüfung
        if(reihe == len(spielfeld) ):    #reihe außerhalb des Spielfelds
            return False
        if spielfeld[reihe][spalte] == spieler:
            rowcount += 1
        else:
            activeRow = False

        if rowcount >= 4:
            return True
        reihe += 1

#horizontale Überprüfung klappt noch nicht
"""
def CheckGewinnerhorizontal(spieler,spielfeld,reihe):
    zaehler = 0
    for s in range(0,len(spielfeld[reihe])):

        if spielfeld[reihe][s] == spieler:
            zaehler += 1
        else:
            zaehler = 0
        if zaehler == 4:
            return True

        return False

def CheckGewinnerhor(spieler,spielfeld,reihe,spalte):
    activeRow = True
    links = True
    constSpalte = spalte
    rowcount = 0

    while(activeRow):

        if spalte == len(spielfeld[reihe]) and links == False:
            return False
        if spalte == -1:
            links = False
            spalte = constSpalte + 1

        if links:
            if spielfeld[reihe][spalte] == spieler:
                rowcount += 1
                spalte -= 1
            else:
                links = False
                spalte = constSpalte + 1
        else:

            if spielfeld[reihe][spalte] == spieler:
                rowcount += 1
                spalte += 1
            else:
                activeRow = False

        if rowcount >= 4:
            return True
    print("hor rowcount")
    print(rowcount)
    return False


"""


spielfeld = numpy.zeros((8,8))  #spieldfeld[reihe][spalte]
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





