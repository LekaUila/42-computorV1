# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/19 16:39:00 by lflandri          #+#    #+#              #
#    Updated: 2024/04/19 17:38:39 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def convertNumber(str: str ) -> float:
    
    return 

def createInstructionList(equation: str) -> list:
    instructionList = []
    actualInstruction = {"coef": None, "degree" : 0, "sign" : "1"}
    needSign = False
    needNumber = False
    needToBeReverse = False
    numberCreator = ""
    isExponent = False
    for i in range(len(equation)):
        if equation[i] != " ":
            if equation[i] in "+-":
                instructionList.append(actualInstruction)
                needSign = False
                if equation[i] == "-" :
                    actualInstruction = {"coef": None, "degree" : 0, "sign" : "-1"}
                else :
                    actualInstruction = {"coef": None, "degree" : 0, "sign" : "1"}
            elif equation[i] in "*/" :
                needSign = False
                if (equation[i] == "/") :
                    needToBeReverse = True
            elif equation[i] in "0123456789." :
                numberCreator += equation[i]
            elif equation[i] == "x" :
                actualInstruction["degree"] += 1
            elif equation[i] == "^" :
                if isExponent :
                    print(f"Error : Can't add an other exponent at pos {i}.")
                    exit(1)
                else :
                    isExponent = True
            else :
                print(f"Error : unknow character at pos {i}.")
                exit(1)
    
    return instructionList

def __main__() -> int:
    if len(sys.argv) != 2:
        print("Error : Wrong number of argument.")
    instructionList = createInstructionList(sys.argv[1])
    return 1

if __name__ == '__main__':
    exit( __main__())