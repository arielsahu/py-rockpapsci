# Permainan Batu Gunting Kertas
# Created By Ariel R V S / 2022-08-13

import random
import os

#GLOBAL 
userWinPoint = 0
userLossPoint = 0 
userDrawPoint = 0 


def GetName(a):
    if a == 1:
      nama = "Batu"
    elif a== 2:
      nama = "Gunting"
    else:
      nama = "Kertas"
    return nama

def Compare(x,y):
    global userWinPoint 
    global userLossPoint 
    global userDrawPoint 
    if x == 1 and y == 1:
        print('\x1b[6;30;43m' + 'Seri!' + '\x1b[0m')
        userDrawPoint += 1
    elif x == 1 and y == 2:
        print('\x1b[6;30;42m' + 'Anda Menang!' + '\x1b[0m')
        userWinPoint += 1
    elif x == 1 and y == 3:
        print('\x1b[6;30;41m' + 'Anda Kalah!' + '\x1b[0m')
        userLossPoint += 1
    elif x == 2 and y == 2:
        print('\x1b[6;30;43m' + 'Seri!' + '\x1b[0m')
        userDrawPoint += 1
    elif x == 2 and y == 1:
        print('\x1b[6;30;41m' + 'Anda Kalah!' + '\x1b[0m')
        userLossPoint += 1
    elif x == 2 and y == 3:
        print('\x1b[6;30;42m' + 'Anda Menang!' + '\x1b[0m')
        userWinPoint += 1
    elif x == 3 and y == 3:
        print('\x1b[6;30;43m' + 'Seri!' + '\x1b[0m')
        userDrawPoint += 1
    elif x == 3 and y == 1:
        print('\x1b[6;30;42m' + 'Anda Menang!' + '\x1b[0m')
        userWinPoint  += 1
    elif x == 3 and y == 2:
        print('\x1b[6;30;41m' + 'Anda Kalah!' + '\x1b[0m')
        userLossPoint  += 1
    else:
        print("Not Defined")

def main():
    varloop = 1
    while  varloop == 1: 
        os.system("CLS")
        print ("PAPAN SCORE")
        print ("------------------------------")
        print("WIN  : ",userWinPoint)
        print("DRAW : ",userDrawPoint)
        print("LOSS : ",userLossPoint)
        print ("------------------------------")
        print("Masukan Pilihan Anda")
        print("1. Batu"+u'\u270A')
        print("2. Gunting"+u'\u270C')
        print("3. Kertas"+u'\u270B')
        try:
            x = int(input("? "))
            isint = 1
        except:
             isint = 0
        if isint==1:
            x = int(x)
            if  x in range(1,4):
                y = random.randint(1, 3)
                print ("Anda Memilih "+GetName(x)+", Komputer Memilih "+GetName(y))
                Compare(x,y)
                z = input("Ingin Melanjutkan Permainan (Y/N)? ")
                if z == "N" or z == "n":
                    varloop = 0
                    os.system("CLS")
                else:
                    os.system("CLS")
            else:
                os.system("CLS")
        else:
             os.system("CLS")
    #after while
    print ("TOTAL SCORE")
    print ("------------------------------")
    print("WIN  : ",userWinPoint)
    print("DRAW : ",userDrawPoint)
    print("LOSS : ",userLossPoint)
    print ("------------------------------")
    print("Terima Kasih telah bermain bersama saya..")
    if(userWinPoint > userLossPoint):
        print("Tampaknya anda Cukup Tangguh")
        print("Selamat Anda Menang")
    elif (userWinPoint < userLossPoint):
        print("Sayang sekali Hari ini anda belum beruntung")
    else:
        print("Ayo main lagi belum ada pemenangnya")

#call main function 

main()