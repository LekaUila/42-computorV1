# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/19 16:39:00 by lflandri          #+#    #+#              #
#    Updated: 2024/04/23 18:49:01 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from class_d.operation import operation

def __main__() -> int:
    sys.setrecursionlimit(2000000000)
    try :
        if len(sys.argv) != 2:
            raise (BaseException("Wrong number of argument."))
        #TODO separer les 2 entré en temps que 2 partire de l'équation
        ope = operation(sys.argv[1])
        ope.print()
        ope.opti()
        print("__________________________________________")
        ope.print()
    except BaseException as exeption :
        print(f"Error : {exeption.args[0]} ")
        # o = 1/0
        return 1
    return 0

if __name__ == '__main__':
    exit( __main__())