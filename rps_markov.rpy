# Permainan Batu Gunting Kertas
# Created By Ariel R V S / 2022-08-13

import random
import os

# GLOBAL 
userWinPoint = 0
userLossPoint = 0 
userDrawPoint = 0 

# Track user moves
user_moves = []

# Transition matrix for Markov model
transition_matrix = {
    "Batu": {"Batu": 0, "Gunting": 0, "Kertas": 0},
    "Gunting": {"Batu": 0, "Gunting": 0, "Kertas": 0},
    "Kertas": {"Batu": 0, "Gunting": 0, "Kertas": 0}
}

def GetName(a):
    if a == 1:
        nama = "Batu"
    elif a == 2:
        nama = "Gunting"
    else:
        nama = "Kertas"
    return nama

def UpdateTransitionMatrix(prev_move, next_move):
    transition_matrix[prev_move][next_move] += 1

def PredictNextMove():
    if not user_moves:
        return random.choice(["Batu", "Gunting", "Kertas"])
    
    last_move = user_moves[-1]
    next_move_probs = transition_matrix[last_move]
    next_move = max(next_move_probs, key=next_move_probs.get)
    print( "My Last Move",last_move)
    print( "Computer Prediction Of My Next Move",next_move)
    print( "Computer Counter Next Move",GetCounterMove(next_move))
    counter_next_move = {"Batu": 1, "Gunting": 2, "Kertas": 3}[GetCounterMove(next_move)]
    return counter_next_move

def GetCounterMove(move):
    if move == "Batu":
        return "Kertas"
    elif move == "Gunting":
        return "Batu"
    else:
        return "Gunting"

def Compare(x, y):
    global userWinPoint 
    global userLossPoint 
    global userDrawPoint 
    user_move = GetName(x)
    comp_move = GetName(y)
    
    if user_moves:
        UpdateTransitionMatrix(user_moves[-1], user_move)
    user_moves.append(user_move)
    
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

def ClearScreen(): 
    if os.name == 'nt': # For Windows 
        os.system('cls')
    else: # For Linux and Mac 
        os.system('clear')

def main():
    varloop = 1
    while varloop == 1: 
        ClearScreen()
        print ("PAPAN SCORE")
        print ("------------------------------")
        print("WIN  : ", userWinPoint)
        print("DRAW : ", userDrawPoint)
        print("LOSS : ", userLossPoint)
        print ("------------------------------")
        print("Masukan Pilihan Anda")
        print("1. Batu" + u'\u270A')
        print("2. Gunting" + u'\u270C')
        print("3. Kertas" + u'\u270B')
        print ("-------MARKOV MODEL-----------")
        for transition_matrix in transition_matrix:
            print(transition_matrix, transition_matrix[transition_matrix])
        print ("------------------------------")
        try:
            x = int(input("? "))
            isint = 1
        except:
            isint = 0
        if isint == 1:
            x = int(x)
            if x in range(1, 4):
                user_move = GetName(x)
                #if user_moves:
                #    UpdateTransitionMatrix(user_moves[-1], user_move)
                #user_moves.append(user_move)
                y = GetName(PredictNextMove())
                print("Anda Memilih " + GetName(x) + ", Komputer Memilih " + y)
                Compare(x, {"Batu": 1, "Gunting": 2, "Kertas": 3}[y])
                z = input("Ingin Melanjutkan Permainan (Y/N)? ")
                if z == "N" or z == "n":
                    varloop = 0
                    ClearScreen()
                else:
                    ClearScreen()
            else:
                ClearScreen()
        else:
            os.system("CLS")
    # after while
    print ("TOTAL SCORE")
    print ("------------------------------")
    print("WIN  : ", userWinPoint)
    print("DRAW : ", userDrawPoint)
    print("LOSS : ", userLossPoint)
    print ("------------------------------")
    print("Terima Kasih telah bermain bersama saya..")
    if userWinPoint > userLossPoint:
        print("Tampaknya anda Cukup Tangguh")
        print("Selamat Anda Menang")
    elif userWinPoint < userLossPoint:
        print("Sayang sekali Hari ini anda belum beruntung")
    else:
        print("Ayo main lagi belum ada pemenangnya")

# call main function 
main()
