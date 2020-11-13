from time import sleep
from os import system as sys

class CPU:
  def __init__(self):
  # Set initial values
    self.clockSpeed = 0.5
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
    self.ramMemory = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False],
                      [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False],
                      [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False],
                      [False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]
    self.ramString = ["00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"]
    self.counterCount = [False, False, False, False]
    self.counterCountStr = "00"
    self.marMemoryDirection = [False, False, False, False]
    self.marMemoryDirectionStr = "00"
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
    print("                        {}{}              {}              {}\n{}##################################################################################################################\n#                                               >>{}CPU EMULATOR{}<<	                                         #\n#                                                                                                                #\n#                 {}_______________                {}_______________                {}_______________                  {}#\n#                {}|    COUNTER    |              {}|      MAR      |              {}|      RAM      |                 {}#\n#                {}|      {}       |              {}|      {}       |              {}|               |                 {}#\n#                {}|_______________|              {}|_______________|              {}| {}  {} {}  {} |                 {}#\n#                                                                              {}|               |                 {}#\n#                                                                              {}| {}  {} {}  {} |                 {}#\n#                                       {}_______________     {}_______________    {}|               |                 {}#\n#                     {}(Clock) {}        {}|               |   {}|               |   {}| {}  {} {}  {} |                 {}#\n#                                      {}|      MIR      |   {}|      MDR      |   {}|               |                 {}#\n#                                      {}|_______________|   {}|_______________|   {}| {}  {} {}  {} |                 {}#\n#               {}_______      _______                                           {}|               |                 {}#\n#               {}\      \    /      /             {}__________________            {}|_______________|                 {}#\n#                {}\      \  /      /             {}|                  |                                             {}#\n#                 {}\      \/      /              {}|                  |                                             {}#\n#                  {}\    ALU     /               {}|   CONTROL UNIT   |                                             {}#\n#                   {}\__________/                {}|                  |                                             {}#\n#                   {}____________                {}|__________________|                                             {}#\n#                  {}| Acumulator |                                                                                {}#\n#                  {}|     {}     |                                                                                {}#\n#                  {}|____________|                                                                                {}#\n#                                                                                                                #\n##################################################################################################################{}"
    .format(self.colorPallete[self.componentColors["team-members"]],self.teamMembers[0], self.teamMembers[1], self.teamMembers[2],
    self.colorPallete[self.componentColors["border"]], self.colorPallete[self.componentColors["title"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]],self.counterCountStr, self.colorPallete[self.componentColors["mar"]], self.marMemoryDirectionStr, self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.ramString[0], self.ramString[1], self.ramString[2], self.ramString[3], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["ram"]], self.ramString[4], self.ramString[5], self.ramString[6], self.ramString[7], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["clock"]], clockString, self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.ramString[8], self.ramString[9], self.ramString[10], self.ramString[11], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
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
    ))

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
    while True:
      self.alu(True, False, [False, False, True, True]) # Sum 2 to the acumulator
      self.ram(self.mar(self.counter(True)), True, self.acumulator(False, "Don't care")) # Store in the direction in the mar (wich takes the counter + 1) th data stores in the acumulator.
      self.printCpu()

  def alu(self, s0, s1, b):
  # Sample call: self.alu(True, False, True, False, [True, False, True, False]) # Where [True, False, True, False] is a list of booleans that represents the hexagesimal value of B in binary
  # The values of a are allways going to be the values stored in the acumulator because of the (retroalimentación en inlgés)
  # If you want to pass data stored in ram you must look for it first and then call alu() with the retrived data from ram
  # If you want to access the retived data from thr alu, it will be always stored in the acumulator, the method DOES NOT retrive data directly
  # Sample return: [True, False, True, False] (a binary number represented with python booleans stored in a list)
  # !s0 && !s1: bitwise or [False, False]
  # !s0 && s1: bitwise and [False, True]
  # s0 && !s1: bitwise sum [True, False]
  # s0 && s1: bitwise substraction [True, True]
    self.componentColors["alu"] = "blue"
    a = self.acumulator(False, "Don't care")
    self.printCpu()
    if (not s0):
      if (not s1): #Bitwise or
        self.acumulator(True, [a[0] or b[0], a[1] or b[1], a[2] or b[2], a[3] or b[3]])
      if (s1): #Bitwise and
        self.acumulator(True, [a[0] and b[0], a[1] and b[1], a[2] and b[2], a[3] and b[3]])
    if (s0):
      self.acumulator(True, self.adderSubstractor_(a, b, s1)) # bitwise sum or substraction deppending on s2
    self.componentColors["alu"] = "white"
  
  def ram(self, memoryDirection, write, data=[]):
  # Reads/Writes data depending in the boolean 'write'. True: write. False: read
  # It needs a memory direction to write/read the data as a list of booleans representing a 4-bit binary number
  # if you want to write data, you must send it as a list of booleans representing a 4-bit binary number
  # sample call: self.ram([True, False, True, False], True, )
    self.componentColors["ram"] = "blue"
    self.printCpu()
    self.componentColors["ram"] = "white"
    if (not write):
      return self.ramMemory[self.binaryToDec_(memoryDirection)]
    else:
      self.ramMemory[self.binaryToDec_(memoryDirection)] = data
      dataStr = str(self.binaryToDec_(data))
      if (len(dataStr) == 1):
        dataStr = "0" + dataStr
      self.ramString[self.binaryToDec_(memoryDirection)] = dataStr

  def binaryToDec_(self, boolBinary):
  # Converts a list of booleans representing a binary number into a Decimal number
  # The porpouse of this function is to be able to manage the memory registers with boolean binary numbers
    decimalNumber = 0
    for i in range(0, 4):
      if (boolBinary[i]):
        decimalNumber += 2**(3-i)
    return decimalNumber
  
  def acumulator(self, write, data):
  # To acces the data in the acumulator you MUST use this function
  # to write in the acumulator, set 'write' to True
  # to read the data stored in the acumulator, set 'write' to False
    self.componentColors["acumulator"] = "blue"
    self.printCpu()
    self.componentColors["acumulator"] = "white"
    if (write):
      self.acumulatorData = data
      self.acumulatorString = str(self.binaryToDec_(self.acumulatorData))
      if (len(self.acumulatorString) == 1):
        self.acumulatorString = "0" + self.acumulatorString
    else:
      return self.acumulatorData

  def counter(self, enableCount):
  # To get the current number stored in the counter, call the function like this: self.counter(False)
  # To get the current number stored in the counter and sum 1 to the count, call the function like this: self.counter(True)
    self.componentColors["counter"] = "blue"
    self.printCpu()
    self.componentColors["counter"] = "white"
    if (enableCount):
      self.counterCount = self.adderSubstractor_(self.counterCount, [False, False, False, True], False) # Sum 1 to the counter count using the adder/substractor
      self.counterCountStr = str(self.binaryToDec_(self.counterCount))
      if (len(self.counterCountStr) == 1) :
        self.counterCountStr = "0" + self.counterCountStr
    return self.counterCount

  def mar(self, memoryDirection):
  # To provide a memory direction to the ram, you MUST use the mar. 
  # To call it using the current value stored in the counter, call it like this: self.mar(self.counter(False))
  # To call it using the next value in the counter, call it like this: self.mar(self.counter(True))
  # To call it providing a different memory direction than the one sotred in the counter, call it like this: self.mar(memoryDirection) # Where 'memoryDirection' is a list of booleans that represent a binary value
    self.componentColors["mar"] = "blue"
    self.printCpu()
    self.componentColors["mar"] = "white"
    self.marMemoryDirection = memoryDirection
    self.marMemoryDirectionStr = str(self.binaryToDec_(self.marMemoryDirection))
    if (len(self.marMemoryDirectionStr) == 1):
      self.marMemoryDirectionStr = "0" + self.marMemoryDirectionStr
    return self.marMemoryDirection


cpu = CPU()
