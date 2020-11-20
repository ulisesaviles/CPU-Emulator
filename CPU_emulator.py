from time import sleep
from os import system as sys

class CPU:
  def __init__(self, rom):
  # Set initial values

    self.clockSpeed = 1
    self.teamMembers = ["Aviles Ulises", "Cruz Elian", "Silva Abner"]
    self.clock = False
    self.colorPallete = {
      "yellow" : "\033[1;33;40m",
      "white" : "\033[1;37;40m",
      "green" : "\033[1;32;40m",
      "blue" : "\033[1;36;40m",
      "red" : "\033[1;31;40m",
    }
    self.componentColors = {
      "team-members" : "white",
      "border" : "yellow",
      "title" : "white",
      "counter": "white",
      "mar" : "white",
      "ram" : "white",
      "clock" : "red",
      "mir" : "white",
      "mdr" : "white",
      "alu" : "white",
      "control-unit" : "white",
      "outside-text" : "white",
      "acumulator" : "white",
    }
    self.acumulatorData = [False, False, False, False]
    self.acumulatorString = "00"
    self.romMemory = rom
    self.ramMemory = [[False for _ in range(8)] for _ in range(16)] #If the register doesn't contain an address in the data part, the fourth bit should be True.
                                                                    #e.g.: ramMemory[0][3]=True is data, ramMemory[0][3]=False is an address 
    self.ramString = ["00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"] 
    #Ignore the next few lines, are just for tests
    #self.ramMemory[0] = [True, False, False, True, False, False, True, True] #LDA #3
    #self.ramMemory[1] = [False, False, False, False, False, True, True, True] #ADD h7
    #self.ramMemory[2] = [True, True, True, True, False, True, True, False]  ##6
    #self.ramMemory[2] = [True, True, False, False, True, False, True, True] #MOVAW hb->>>>>6+3=9
    #self.ramMemory[3] = [False, False, True, True, False, False, True, False] #SUB A,#2
    #self.ramMemory[4] = [True, False, True, False, True, True, True, True] #MOVAR hf
    #self.ramMemory[7] = [True, True, True, True, False, True, True, False]  # #6
    #self.ramMemory[15] = [True, True, True, True, True, True, True, False]   #14
    #########################################################################
    self.counterCount = [False, False, False, False]
    self.counterCountStr = "00"
    self.marMemoryDirection = [False, False, False, False]
    self.marMemoryDirectionStr = "00"
    self.mdrData = [False, False, False, False, False, False, False, False] #This has the same format for the fourth bit as explained on lines 34 & 35
    self.mdrDataStr = ["00","00", "#"] #It's divided because of the separation needed between opcode and plain data an # tag represents a raw data, a blank space is an address.
    self.mirData = [False, False, False] #I've decreased the bus width of the MIR register because I needed to use an extra bit for determining wheter the fetched data contains
    self.mirDataStr = "00"               # ... an address or raw data
    self.run()
    
  def printCpu(self):
  # Print the CPU in the terminal with the right colors depending on the use of the components
  # >> IMPORTANT >> When you call self.printCpu() it makes a clockPulse before printing, so if you want to make a full clockPulse you should call this function twice
  # Sample Call:
  # self.componentColors["mdr"] = "blue" # if you want the mdr to be printed in color blue
  # self.printCpu()
  # self.componentColors["mdr"] = "white" # if you no longer want the mdr to be printed blue
  # >> IMPORTANT >> Every submodule (alu, ram, mdr, etc...) have their own printCpu() and recolor inside the function, so that you don't have to do it by yourself.
    self.clockPulse_()
    if (self.clock == False):
      self.componentColors["clock"] = "red"
      clockString = 0
    else:
      self.componentColors["clock"] = "green"
      clockString = 1
    sys("cls")
    print("                        {}{}              {}              {}\n{}##################################################################################################################\n#                                               >>{}CPU EMULATOR{}<<	                                         #\n#                                                                                                                #\n#                 {}_______________                {}_______________                {}_______________                  {}#\n#                {}|    COUNTER    |              {}|      MAR      |              {}|      RAM      |                 {}#\n#                {}|      {}       |              {}|      {}       |              {}|               |                 {}#\n#                {}|_______________|              {}|_______________|              {}| {}  {} {}  {} |                 {}#\n#                                                                              {}|               |                 {}#\n#                                                                              {}| {}  {} {}  {} |                 {}#\n#                                       {}_______________     {}_______________    {}|               |                 {}#\n#                     {}(Clock) {}        {}|      MIR      |   {}|      MDR      |   {}| {}  {} {}  {} |                 {}#\n#                                      {}|       {}      |   {}|     {}     |   {}|               |                 {}#\n#                                      {}|_______________|   {}|_______________|   {}| {}  {} {}  {} |                 {}#\n#               {}_______      _______                                           {}|               |                 {}#\n#               {}\      \    /      /             {}__________________            {}|_______________|                 {}#\n#                {}\      \  /      /             {}|                  |                                             {}#\n#                 {}\      \/      /              {}|                  |                                             {}#\n#                  {}\    ALU     /               {}|   CONTROL UNIT   |                                             {}#\n#                   {}\__________/                {}|                  |                                             {}#\n#                   {}____________                {}|__________________|                                             {}#\n#                  {}| Acumulator |                                                                                {}#\n#                  {}|     {}     |                                                                                {}#\n#                  {}|____________|                                                                                {}#\n#                                                                                                                #\n##################################################################################################################{}"
    .format(self.colorPallete[self.componentColors["team-members"]], self.teamMembers[0], self.teamMembers[1], self.teamMembers[2],
    self.colorPallete[self.componentColors["border"]], self.colorPallete[self.componentColors["title"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]],self.counterCountStr, self.colorPallete[self.componentColors["mar"]], self.marMemoryDirectionStr, self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.ramString[0], self.ramString[1], self.ramString[2], self.ramString[3], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["ram"]], self.ramString[4], self.ramString[5], self.ramString[6], self.ramString[7], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["clock"]], clockString, self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.ramString[8], self.ramString[9], self.ramString[10], self.ramString[11], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["mir"]], self.mirDataStr, self.colorPallete[self.componentColors["mdr"]], self.mdrDataStr[0]+self.mdrDataStr[2]+self.mdrDataStr[1] , self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.ramString[12], self.ramString[13], self.ramString[14], self.ramString[15], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["acumulator"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["acumulator"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["acumulator"]], self.acumulatorString, self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["acumulator"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["outside-text"]],
    )) # I've added two pointers to print the MIR and MDR data, their respective location its on line 85

  def fullAdder_(self, a, b, cin):
  # Pretty self explanatory
  # Sample call: self.fullAdder(True, False, True)
    return [a and b or a != b and cin, (a!=b) != cin] # returns [cout, sum]

  def adderSubstractor_(self, a, b, substraction):
  # 4 bit adder substractor
  # Sample call: self.fullAdder([True, False, True, False], [False, True, True, False], True) # where a and b are lists of booleans that represent a 4 bit binary number and 'substraction' decides weather a sum or a substraction is made
    firstFullAdder = self.fullAdder_(a[3], b[3]!=substraction, substraction)
    secondFullAdder = self.fullAdder_(a[2], b[2]!=substraction, firstFullAdder[0])
    thirdFullAdder = self.fullAdder_(a[1], b[1]!=substraction, secondFullAdder[0])
    fourthFullAdder = self.fullAdder_(a[0], b[0]!=substraction, thirdFullAdder[0])
    return [fourthFullAdder[1], thirdFullAdder[1], secondFullAdder[1], firstFullAdder[1]]

  def clockPulse_(self):
  # Make a clock pulse to indicate a new task
  # Sample call: clockPulse()
    self.clock = not self.clock
    sleep(self.clockSpeed)

  def run(self):
    self.printCpu()
    self.printCpu()
    # self.ram([False, False, False, True], True, [True, True, True, True])
    # print(self.ram([False, False, False, True], False))
    # self.printCpu()
    while int(self.counterCountStr)<len(self.romMemory):
      self.mar(self.counter(False), False, False, False)
      self.counter(True)
      #self.alu(False, False, [False, False, True, True]) # Sum 3 to the acumulator
      #self.ram(self.mar(self.counter(True)), True, self.acumulator(False, "Don't care")) # Store in the direction in the mar (wich takes the counter + 1) th data stores in the acumulator.
      self.printCpu()

  def alu(self, s1, s0, b):
  # Sample call: self.alu(True, False, True, False, [True, False, True, False]) # Where [True, False, True, False] is a list of booleans that represents the hexagesimal value of B in binary
  # The values of a are allways going to be the values stored in the acumulator because of the (retroalimentación en inlgés)
  # If you want to pass data stored in ram you must look for it first and then call alu() with the retrived data from ram
  # If you want to access the retived data from thr alu, it will be always stored in the acumulator, the method DOES NOT returns data directly
  # Sample return: [True, False, True, False] (a binary number represented with python booleans stored in a list)
  ########################################################   IMPORTANT   #######################################################################
  # I've changed the opcode of the selectors to match with the one we've been using through the semester. It works as follows: 
  # s1 && s0: bitwise or [True, True]            11
  # s1 && !s0: bitwise and [True, False]         10
  # !s1 && !s0: bitwise sum [False, False]       00
  # !s1 && s0: bitwise substraction [True, True] 01
    self.componentColors["alu"] = "blue"
    a = self.acumulator(False, "Don't care")
    self.printCpu()
    if (s1): #This selector chooses whether we'll use logic or arithmetic operations, if true, logic ops are chosen, otherwise arithmetic are chosen.
      if (not s0): #Bitwise and, selectors: 10
        self.acumulator(True, [a[0] and b[0], a[1] and b[1], a[2] and b[2], a[3] and b[3]])
      else: #Bitwise or, Selectors: 11
        self.acumulator(True, [a[0] or b[0], a[1] or b[1], a[2] or b[2], a[3] or b[3]])#True, [a[0] or b[0], a[1] or b[1], a[2] or b[2], a[3] or b[3]]
    else:
      self.acumulator(True, self.adderSubstractor_(a, b, s0)) # bitwise sum or substraction deppending on s0, 1->SUB, 0->ADD
    self.componentColors["alu"] = "white"
  
  def rom(self, memoryDirection):
      return self.romMemory[self.binaryToDec_(memoryDirection,4)]

  def ram(self, memoryDirection, write, data=[]):
  # Reads/Writes data depending in the boolean 'write'. True: write. False: read
  # It needs a memory direction to write/read the data as a list of booleans representing a 4-bit binary number
  # if you want to write data, you must send it as a list of booleans representing a 4-bit binary number
  # sample call: self.ram([True, False, True, False], True, )
  # If you need to write something, if it contains only data (not and address) then the fourth bit should be True
  # otherwise it will be interpreted as a reference to another address.
    self.componentColors["ram"] = "blue"
    self.printCpu()
    self.componentColors["ram"] = "white"
    if (not write):
      return self.ramMemory[self.binaryToDec_(memoryDirection,4)]
    else:
      self.ramMemory[self.binaryToDec_(memoryDirection,4)] = data
      dataStr = str(self.binaryToDec_(data[4:],4))
      if (len(dataStr) == 1):
        dataStr = "0" + dataStr
      self.ramString[self.binaryToDec_(memoryDirection,4)] = dataStr
      self.componentColors["ram"] = "blue"
      self.printCpu()
      self.componentColors["ram"] = "white"

  def binaryToDec_(self, boolBinary, busWidth):
  # Converts a list of booleans representing a binary number into a Decimal number
  # The porpouse of this function is to be able to manage the memory registers with boolean binary numbers
  # The busWidth parameter tells the function how many powers of two has to use in order to convert to decimal.
    decimalNumber = 0
    for i in range(0, busWidth):
      if (boolBinary[i]):
        decimalNumber += 2**(busWidth-1-i)
    return decimalNumber
  
  def acumulator(self, write, data):
  # To acces the data in the acumulator you MUST use this function
  # to write in the acumulator, set 'write' to True
  # to read the data stored in the acumulator, set 'write' to False
    self.componentColors["acumulator"] = "blue"
    if (write):
      self.acumulatorData = data
      self.acumulatorString = str(self.binaryToDec_(self.acumulatorData,4))
      if (len(self.acumulatorString) == 1):
        self.acumulatorString = "0" + self.acumulatorString
      self.printCpu()
      self.componentColors["acumulator"] = "white"
    else:
      self.printCpu()
      self.componentColors["acumulator"] = "white"
      return self.acumulatorData

  def counter(self, enableCount):
  # To get the current number stored in the counter, call the function like this: self.counter(False)
  # To get the current number stored in the counter and sum 1 to the count, call the function like this: self.counter(True)
    self.componentColors["counter"] = "blue"
    self.printCpu()
    self.componentColors["counter"] = "white"
    if (enableCount):
      self.counterCount = self.adderSubstractor_(self.counterCount, [False, False, False, True], False) # Sum 1 to the counter count using the adder/substractor
      self.counterCountStr = str(self.binaryToDec_(self.counterCount,4))
      if (len(self.counterCountStr) == 1) :
        self.counterCountStr = "0" + self.counterCountStr
    return self.counterCount

  def mar(self, memoryDirection, s3, writeOnMemory, readDirect):
  # To provide a memory direction to the ram, you MUST use the mar. 
  # To call it using the current value stored in the counter, call it like this: self.mar(self.counter(False), False, False)
  # To call it using the next value in the counter, call it like this: self.mar(self.counter(True), False, False)
  # To call it providing a different memory direction than the one sotred in the counter, call it like this: self.mar(memoryDirection, False, False) # Where 'memoryDirection' is a list of booleans that represent a binary value  
  # To call it when a writing to memory its going to take place in the next clock cycle and the address comes from counter, do this: self.mar(memoryDirection, False, True)
  # To call it when the next state its a writing and the address comes from the control unit, use the next: self.mar(memoryDirection, True, True)
  # If you don't want to write, but the source of your address its the control unit, call it like this: self.mar(memoryDirection, True, False)
    self.marMemoryDirection = memoryDirection
    self.marMemoryDirectionStr = str(self.binaryToDec_(self.marMemoryDirection,4))
    if (len(self.marMemoryDirectionStr) == 1):
      self.marMemoryDirectionStr = "0" + self.marMemoryDirectionStr
    self.componentColors["mar"] = "blue"
    self.printCpu() 
    self.componentColors["mar"] = "white"
    if (not writeOnMemory): 
      if (s3): #this tells us wheter we're receiving from Program Counter or the Control Unit, if True, we have to return a value to the CU, else it has to keep the fetch cycle to MDR
        if (readDirect):
          dataFetched = self.ram(self.marMemoryDirection, False, "dont care")
          return self.mdr(dataFetched, s3, False) 
        dataFetched = self.rom(self.marMemoryDirection)
        return self.mdr(dataFetched, s3, False) 
      dataFetched = self.rom(self.marMemoryDirection)
      self.mdr(dataFetched, s3, False)
    else:   #This happens when we want to write to memory and the RAM its set on Write mode and the data stored in MDR its written on the needed register.
      data = self.mdrData
      self.ram(self.marMemoryDirection , True , data)

  def mdr(self, data, s3, writeOnRAM):
    #The data variable should be considered as an 8-bit register, hence, the mdr is an 8-bit register.
    #When converting to string, the data is passed to binaryToDec_ in chunks of 4 bits (two of them), each chunk is composed by opcode and data respectively
    #The parameter s3 has the functionality to establish if we are into a fetch cycle from counter or from the control unit
    #If writeOnRAM its enabled, the module does nothing, it is only used to store the data that will be written on memory in next clock cycle. It's like the enable of the module.
    self.mdrData = data
    self.mdrDataStr[0] = str(self.binaryToDec_(self.mdrData[:3],3))
    self.mdrDataStr[1] = str(self.binaryToDec_(self.mdrData[4:],4))
    self.mdrDataStr[2] = "#" if self.mdrData[3]==True else " " #This just writes a # tag if true, indicating it contains raw data, if not, it writes a blank space  
    if (len(self.mdrDataStr[0]) == 1):
      self.mdrDataStr[0] = "0" + self.mdrDataStr[0]
    if (len(self.mdrDataStr[1]) == 1):
      self.mdrDataStr[1] = "0" + self.mdrDataStr[1]
    self.componentColors["mdr"] = "blue"
    self.printCpu()
    self.componentColors["mdr"] = "white"
    #Here the control unit work begins
    if (not writeOnRAM):  
      if (s3): #If data comes directly from memory or if it comes from Control Unit, if True it comes from CU, else it comes from memory and it proceeds to call CU
        return self.mdrData
      self.controlUnit(self.mdrData)
    #return self.mdrDataStr

  def mir(self, data):
    #This module only receives data with a bus width of 3 bits because that's the required length of our opcode
    self.mirData = data
    self.mirDataStr = str(self.binaryToDec_(self.mirData[:3],3))
    if (len(self.mirDataStr) == 1):
      self.mirDataStr = "0" + self.mirDataStr
    self.componentColors["mir"] = "blue"
    self.printCpu()
    self.componentColors["mir"] = "white"

  def controlUnit(self, dataIn):
    #The most important function of this module is decoder, it's called in the last line of the module, it could be considered to be the main of the Control Unit
    self.componentColors["control-unit"] = "blue"
    self.printCpu()  

    def decoder(rawData):
      #This is the module that has to be called whenever the Control Unit receives data in raw format directly from the MDR. The module has several tasks:
      #Has to split instrucions (aka OPCODE) and the data (or possible register address) that was fetched from the memory.
      #Has to determine which instruction is supposed to be done and if it has to be on direct or immediate mode
      #Because the different circuits have been modularized, the states execution is done through the calling of such modules
      #################################################### IMPORTANT ###################################################
      instructionFetched = rawData[:3]    #IMPORTANT: the opcode only takes the first 3 bits from left to right
      self.mir(instructionFetched)
      if (not instructionFetched[0]):     #The ALU instructions have a zero in the first bit of the opcode, namely it should be False to be considered an ALU operation
        aluInstructions(rawData)
      else:                               #Here are grouped all the instructions related to transferring data
        dataTransferInstructions(rawData)
      self.componentColors["control-unit"] = "blue"
      self.printCpu()
      self.componentColors["control-unit"] = "white"
    
    def dataTransferInstructions(rawData):
      #Because here we're dealing with addresses, there's no need for a direct and immediate mode, that's why we should always verify if the 
      #data that has been passed to us its composed by an address, namely, if the fourth bit its set to False
      def setColorsBefore_():
        self.componentColors["control-unit"] = "blue"
        self.printCpu()
        self.componentColors["control-unit"] = "white"

      def setColorsAfter_():
        self.componentColors["control-unit"] = "blue"
        self.printCpu()

      instructionFetched = rawData[:3]
      isData =  "#" if rawData[3]==True else " " 
      dataFetched = rawData[4:]
      if (not instructionFetched[1] and not instructionFetched[2]): #LDA
        if (not rawData[3]):                                        #If the data contains a reference to a memory address
          self.componentColors["control-unit"] = "white"
          dataFetched =  self.mar(dataFetched, True, False, True)[-4:]
        setColorsBefore_()
        self.acumulator(True, dataFetched)
      elif (not instructionFetched[1] and instructionFetched[2]): #MOVAR, it works the same as a LDA on direct mode
        self.componentColors["control-unit"] = "white"
        dataFetched =  self.mar(dataFetched, True, False, True)[-4:]
        setColorsBefore_()
        self.acumulator(True, dataFetched)
      elif (instructionFetched[1] and not instructionFetched[2]): #MOVAW
        dataAcc = [False for _ in range(3)]
        dataAcc.append(True)
        for i in self.acumulator(False, "Don't care"):            #Since dataAcc has only 4-bit width, we need to append to it 4 zeros bits at the beggingg of it
          dataAcc.append(i)
        self.mdr(dataAcc, True, True)
        self.mar(dataFetched, True, True, False)  
      elif (instructionFetched[1] and instructionFetched[2]): #NOP                      #The s3 parameter is a don't care
        self.componentColors = {
          "team-members" : "white",
          "border" : "yellow",
          "title" : "white",
          "counter": "red",
          "mar" : "red",
          "ram" : "red",
          "clock" : "red",
          "mir" : "red",
          "mdr" : "red",
          "alu" : "red",
          "control-unit" : "red",
          "outside-text" : "white",
          "acumulator" : "red",
        }
        self.printCpu()
        self.componentColors = {
          "team-members" : "white",
          "border" : "yellow",
          "title" : "white",
          "counter": "white",
          "mar" : "white",
          "ram" : "white",
          "clock" : "red",
          "mir" : "white",
          "mdr" : "white",
          "alu" : "white",
          "control-unit" : "white",
          "outside-text" : "white",
          "acumulator" : "white",
        }
        self.printCpu()

    def aluInstructions(rawData):
      instructionFetched = rawData[:3]
      isData =  "#" if rawData[3]==True else " " 
      dataFetched = rawData[4:]
      if (not rawData[3]): #if rawData[3] is on False, the data is a reference to a memory address and direct MODE its invoked (it does another fetch cycle)
        self.componentColors["control-unit"] = "white"
        dataFetched =  self.mar(dataFetched, True, False, True)[-4:] #Goes to mar and sends it the address fetched in the last cycle, sets the reference from CU as true and false for writting
                                                               #because the received data its 8-bits long, the first 4 are ignored and the last four are fetched.
      #Immediate MODE
      self.componentColors["control-unit"] = "blue"
      self.printCpu()
      self.componentColors["control-unit"] = "white"
      self.alu(instructionFetched[1], instructionFetched[2], dataFetched)
      self.componentColors["control-unit"] = "blue"
      self.printCpu()
    
    decoder(dataIn) #MAIN CALL TO DECODER METHOD
#cpu = CPU()