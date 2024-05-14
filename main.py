# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/19 16:39:00 by lflandri          #+#    #+#              #
#    Updated: 2024/05/14 18:58:44 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from class_d.operation import  operation

def __main__() -> int:
    sys.setrecursionlimit(2000)
    try :
        if len(sys.argv) != 2:
            raise (BaseException("Wrong number of argument."))
        entry = sys.argv[1]
        p = entry.find("=")
        if p == -1 :
            raise BaseException("this isn't an equation.")
        print(f"start to parse with : '{entry[:p]} = {entry[p + 1:]}'\n")
        ope1 = operation(entry[:p])
        ope2 = operation(entry[p + 1:])
        print(f"ope1 before operation : {ope1}")
        print("__________________________________________")
        ope1.checkVariableForEquation()
        ope1.opti()
        print("__________________________________________")
        print(f"ope1 after operation : {ope1}")
        print("__________________________________________")
        print(f"ope2 before operation : {ope2}")
        print("__________________________________________")
        ope2.checkVariableForEquation()
        ope2.opti()
        print("__________________________________________")
        print(f"ope2 after operation : {ope2}")
        print("__________________________________________")
        print(f"ope after operation : {ope1} = {ope2}")
        # TODO : try destroing div by X
        # print("__________________________________________")
        
        # testNum = 42
        # while testDiv != None:
        #     testDiv = ope1.
        # ope1 = ope1 * operation("X + 9")
        # ope2 = ope2 * operation("X + 9")
        # print(f"ope after mult : {ope1} = {ope2}")
        
        # TODO : find type équation
        # TODO : resolve équation
    except BaseException as exeption :
        print(f"Error : {exeption.args[0]} ")
        o = 1/0
        return 1
    return 0

if __name__ == '__main__':
    exit( __main__())