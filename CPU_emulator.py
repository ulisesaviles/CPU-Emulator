from os import system as sys
class CPU:
  def __init__(self, bandWidth):
    # Set initial values
    self.bandwidth = bandWidth
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
    }
    self.printCpu()

  # Print the CPU in the terminal with the right colors depending on the use of the components
  def printCpu(self):
    if self.clock == False:
      self.componentColors["clock"] == "red"
    else:
      self.componentColors["clock"] == "green"
    sys("cls")
    print("                        {}{}              {}              {}\n{}##################################################################################################################\n#                                                >>{}CPU EMULATOR{}<<	                                         #\n#                                                                                                                #\n#                 {}_______________                {}_______________                {}_______________                  {}#\n#                {}|               |              {}|               |              {}|               |                 {}#\n#                {}|    COUNTER    |              {}|      MAR      |              {}|               |                 {}#\n#                {}|_______________|              {}|_______________|              {}|               |                 {}#\n#                                                                              {}|               |                 {}#\n#                                                                              {}|               |                 {}#\n#                                       {}_______________     {}_______________    {}|      RAM      |                 {}#\n#                        {}0             {}|               |   {}|               |   {}|               |                 {}#\n#                                      {}|      MIR      |   {}|      MDR      |   {}|               |                 {}#\n#                                      {}|_______________|   {}|_______________|   {}|               |                 {}#\n#               {}_______      _______                                           {}|               |                 {}#\n#               {}\      \    /      /             {}__________________            {}|_______________|                 {}#\n#                {}\      \  /      /             {}|                  |                                             {}#\n#                 {}\      \/      /              {}|                  |                                             {}#\n#                  {}\    ALU     /               {}|   CONTROL UNIT   |                                             {}#\n#                   {}\__________/                {}|                  |                                             {}#\n#                                               {}|__________________|                                             {}#\n#                                                                                                                #\n#                                                                                                                #\n##################################################################################################################{}"
    .format(self.colorPallete[self.componentColors["team-members"]],self.teamMembers[0], self.teamMembers[1], self.teamMembers[2],
    self.colorPallete[self.componentColors["border"]], self.colorPallete[self.componentColors["title"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["counter"]], self.colorPallete[self.componentColors["mar"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["clock"]], self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["mir"]], self.colorPallete[self.componentColors["mdr"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["ram"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["alu"]], self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]], 
    self.colorPallete[self.componentColors["control-unit"]], self.colorPallete[self.componentColors["border"]],
    self.colorPallete[self.componentColors["outside-text"]],
    ))

cpu = CPU(4)


