# CPU-Emulator #

## Installation. ##
1. Go to [Python's official site](https://www.python.org/) and head to "Downloads" section.

![installation-1](/src/img/installation-1.png)

2. Download the latest version of Python available.

![installation-2](/src/img/installation-2.png)

>> NOTE: In case you already have Python installed, make sure your version is at least 3.7.0 for the program to run correctly.

>> You can update your Python version by typing `python -m pip install --upgrade pip` on your Windows terminal and typing `sudo -H pip3 install --upgrade pip` if you are on a Linux distro.

>> You can always check your `pip` version by typing `pip --version` on you terminal.

## User guide. ##
1. At first, you’ll find yourself in the file explorer. What you want to do is to head on the “main.py" file and then run it on the terminal by pressing `F5`.

![Guide-1](/src/img/guide1.png)

2. Then select the “Python file” option and hit Enter. Welcome to the main menu! See, as it is shown below the first few lines of the program list the instruction set for our CPU. The `D | I` means that you can use the instruction in both *immediate* and *direct mode*. If the instruction you want to execute has no `D | I` it is assumed that the instruction is **ONLY** direct.

![Guide-1](/src/img/guide2.png)

3. Now, moving forward you are able to see that the cursor is located under the new instruction line. Here you are supposed to write you instruction and add it to the queue. The structure for this is as it follows:
a. **Direct instructions:** OPCODE  |  BLANK SPACE |  “h”  |  DIRECTION
b. **Immediate instructions:** OPCODE  |  BLANK SPACE |  “#”  |  DATA
For instance, let’s add a 5 t number to the accumulator. To do this, I should first type the opcode *ADD*, and because I know what data I want to pass to the accumulator I can do an immediate instruction so it is as simple as type a blank space and then type the “#” symbol followed by my data which in this case it turns out to be a number 5. 
>>NOTE: after the symbol you must type your data (be it mere data or a memory address).

Our result would be something like this:

![Guide-1](/src/img/guide3.png)

Once you hit enter you will be asked whether or not you want to add another instruction to the queue. In case you want to add more instructions `press 1`. Otherwise `press 2` in order to start the emulation.

![Guide-1](/src/img/guide4.png)

4. In case you'd like to change the **clock speed**, head to the "CPU_emulator" file and change the value of the variable "clockSpeed" with your desired speed in seconds.

![Guide-5.png](/src/img/guide5.png)

And it is as simple as that. Your emulation will start running and once all the tasks are finished, the program will stop. If you want to run another set of instructions run the program again as it was established at the beginning of the guide.



## Instruction Set ##
| Opcode | Type                 | Category                | Description                                                                                                                                                                                                                                                                                   |
|--------|----------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD    | Direct and immediate | ALU operation           | This instruction when called adds the desired number to the current value stored in the accumulator. If direct mode is used, the value is obtained from the given address. When called in immediate mode the given value is directly summed to the current value of the accumulator.          |
| SUB    | Direct and immediate | ALU operation           | This instruction when called subtracts the desired number to the current value stored in the accumulator. If direct mode is used, the value is obtained from the given address. When called in immediate mode the given value is directly subtracted to the current value of the accumulator. |
| AND    | Direct and immediate | ALU operation           | Bitwise AND comparison operation.                                                                                                                                                                                                                                                             |
| OR     | Direct and immediate | ALU operation           | Bitwise OR comparison operation.                                                                                                                                                                                                                                                              |
| LDA    | Direct and immediate | Data transfer operation | Replaces the current stored value in the accumulator with the given value (immediate mode). In case this instruction is called in direct mode, the value in the given register memory is the one replacing the accumulator value.                                                             |
| MOVAR  | Direct               | Data transfer operation | The current value stored in the accumulator is replaced with the stored value in the RAM given address.                                                                                                                                                                                       |
| MOVAW  | Direct               | Data transfer operation | The current RAM value in the given register is replaced with the current value stored in the accumulator.                                                                                                                                                                                     |
| NOP    | Direct               | Data transfer operation | It does not do any action. It just waits until the PC changes so a new instruction takes place.       

## Logical Flow ##
![Logical-flow](/src/img/logical-flow.jpg)

## Data formats ##
| Type of instruction |  First segment | Second segment | Third segment |Fourth segment |
|:-------:|:-------:|:------:|:------:|:------:|
|    Immediate    |  OPCODE |    Blank space   |    'h'   |   Data    |
|    Direct    | OPCODE |    Blank space    |    '#'    |     Address    |
In both cases, the Data and the Address should be represented as an hexadecimal digit. One-digit numbers doesn't need a zero before.
The NOP instruction does not require any aditional segment, just the plain instruction.
## System buses ##
| Bus | Bitwidth-in | Bitwidth-out |
|:---:|:-----------:|:------------:|
| MAR |    4-bit    |     4-bit    |
| MIR |    3-bit    |     3-bit    |
| MDR |    8-bit    |     8-bit    |
| RAM |    4-bit    |     8-bit    |
| ROM |    4-bit    |     8-bit    |
|  CU |    8-bit    |    Varies    |

## Timing issues and performance ##

| Opcode | Type      | Execution time                                       |
|--------|-----------|------------------------------------------------------|
| ADD    | Direct    | 0.26873016357421875 seconds + clock speed in seconds |
| ADD    | Immediate | 0.42658519744873047 seconds + clock speed in seconds |
| SUB    | Direct    | 0.24445748329162598 seconds + clock speed in seconds |
| SUB    | Immediate | 0.34108805656433105 seconds + clock speed in seconds |
| AND    | Direct    | 0.3138000965118408 seconds + clock speed in seconds  |
| AND    | Immediate | 0.30643796920776367 seconds + clock speed in seconds |
| OR     | Direct    | 0.27966880798339844 seconds + clock speed in seconds |
| OR     | Immediate | 0.2461867332458496 seconds + clock speed in seconds  |
| LDA    | Direct    | 0.22153925895690918 seconds + clock speed in seconds |
| LDA    | Immediate | 0.27804112434387207 seconds + clock speed in seconds |
| MOVAR  | Direct    | 0.2588512897491455 seconds + clock speed in seconds  |
| MOVAW  | Direct    | 0.26668643951416016 seconds + clock speed in seconds |
| NOP    | Direct    | 0.2182176113128662 seconds + clock speed in seconds  |

>> NOTE: This tests were made with a Intel i5 8th generation 2.30Ghz CPU. This results may vary according to your CPU.

## Made by: ##
* Ulises Aviles T031438
* Elian Cruz T032218
* Abner Silva T032069
* René Nuñez T032277
* Dennis Cárdenas T026290