from CPU_emulator import *
import os

userInputInstructions = []
userRawInstructions = []
#DATA FORMAT:
### [ 3-BIT OPCODE |  ADDRESS OR DATA BIT  |  4-BIT DATA/ADDRESS ]
resp = "1"
clear = lambda: os.system('cls')
while resp == "1":
    print("DATA FORMAT:\n[ 3-BIT OPCODE |  ADDRESS OR DATA BIT  |  4-BIT DATA/ADDRESS ]")
    print("OPERATIONS AVAILABLE:\nADD D|I\nSUB D|I\nAND D|I\nOR D|I\nLDA D|I\nMOVAR\nMOVAW\nNOP")
    print("-------------------Instructions written-----------------------")
    for i in userRawInstructions:
        print(i)
    print("-------------------New Instruction:-----------------------")
    userRawInstructions.append(input("--: "))
    clear()
    resp = input("ADD ANOTHER? [1]-YES")
#>>> a[:3]
#'012'
#>>> a[3]
#'3'
#>>> a[4:]
#'4567'

instructions = {
    "ADD"  : [False,False,False],
    "SUB"  : [False,False,True],
    "AND"  : [False,True,False],
    "OR"   : [False,True,True],
    "LDA"  : [True,False,False],
    "MOVAR": [True,False,True],
    "MOVAW": [True,True,False],
    "NOP"  : [True,True,True]
}

def binaryToDec_(dec):
    dec = int(dec)
    binary = [False for i in range(4)]
    i = 3
    while dec>0:
        binary[i]=  False if dec%2==0 else True
        dec = dec//2
        i-=1
    return binary

for i in userRawInstructions:
    thisInstrs = instructions
    index = int(i.find(" "))
    operation = i[:index]
    mode = i[index+1]
    data = i[index+2:]
    dataBinary = binaryToDec_(data if data.isnumeric() else 10 if data=="a" else 11 if data == "b" else 12 if data == "c" else 13 if data == "d" else 14 if data == "e" else 15)
    opcode = thisInstrs[operation]
    modeBinary = True if mode == "#" else False
    userInputInstructions.append(opcode + [modeBinary] + dataBinary)

#userInputInstructions.append([True, False, False, True, False, False, True, True])   #LDA #3
#userInputInstructions.append([False, False, False, True, True, False, True, True])   #ADD #11
#userInputInstructions.append([True, True, False, False, False, True, True, True])     #MOVAW h7
#userInputInstructions.append([False, False, True, True, False, True, False, True])    #SUB #5
#userInputInstructions.append([False, True, False, False, False, True, True, True])   #AND h7
#userInputInstructions.append([True, True, False, False, True, False, True, True])    #MOVAW hb->>>>>8
#userInputInstructions.append([True, False, True, False, False, True, True, True])     #MOVAR h7
#userInputInstructions.append([False, False, True, True, True, False, False, True])   #SUB #9
#userInputInstructions.append([True, True, False, False, False, False, False, False]) #MOVAW h0->>>>>5
#userInputInstructions.append([False, True, True, False, True, False, True, True])    #OR hb
#userInputInstructions.append([True, True, True, False, True, False, True, True])     #NOP

#print(userInputInstructions)
#clear()
#print(userInputInstructions)
cpu = CPU(userInputInstructions)

