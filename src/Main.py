import numpy

def Spielzug(spielfeld,spieler,spalte):

    if spielfeld[0][spalte] != 0:
        print("zug nicht möglich")
    for i in range(0, len(spielfeld)):
        if i == len(spielfeld) - 1:
            spielfeld[i][spalte] = spieler
            print(spielfeld)
            if CheckGewinnervert(spieler, spielfeld, spalte, i) or CheckGewinnerhorizontal(spieler,spielfeld,i) or CheckGewinnerDiagonal(spieler,spielfeld,i,spalte):
                return True
            break
        elif spielfeld[i+1][spalte] != 0:
            spielfeld[i][spalte] = spieler
            print(spielfeld)
            if CheckGewinnervert(spieler, spielfeld, spalte, i) or CheckGewinnerhorizontal(spieler,spielfeld,i) or CheckGewinnerDiagonal(spieler,spielfeld,i,spalte):
                return True
            break




def CheckGewinnervert(spieler, spielfeld, spalte, zeile):

    zaehler = 0

    for s in range(0,len(spielfeld)):
        if spielfeld[s][spalte] == spieler:
            zaehler += 1
        else:
            zaehler = 0
        if zaehler == 4:
            return True
    return False









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



def CheckGewinnerDiagonal(spieler,spielfeld,zeile,spalte):
     zaehler = 0
     startZ = zeile
     startS = spalte
     while(startS>0 and startZ>0):
         startZ -= 1
         startS -= 1

     while(startS<len(spielfeld[zeile]) and startZ<len(spielfeld)):
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
     while (startS > 0 and startZ < len(spielfeld) - 1 ):
         startZ += 1
         startS -= 1

     while (startS < len(spielfeld[zeile]) and startZ  > 0 ):
         if spielfeld[startZ][startS] == spieler:
             zaehler += 1
         else:
             zaehler = 0
         if zaehler == 4:
             return True
         startZ -= 1
         startS += 1


     return False





spielfeld = numpy.zeros((8,8))  #spieldfeld[zeile][spalte]
print(spielfeld)
spieler = 1
while(True):
    eingabe = input("Spalte: ")
    if eingabe == "stop":
        break
    if Spielzug(spielfeld,spieler,int(eingabe)-1):
        print("Spieler:" , spieler , "hat gewonnen")
        eingabe = input("wollt ihr nochmal spielen? (Y/N)")
        if eingabe == "Y":
            spielfeld = numpy.zeros((8,8))
        else:
            exit()


    else:

      if spieler == 1:
        spieler = 2
      else:
         spieler = 1





