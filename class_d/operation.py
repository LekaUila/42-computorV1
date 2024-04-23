# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/23 13:34:57 by lflandri          #+#    #+#              #
#    Updated: 2024/04/23 21:33:37 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mathFunction import power

def parseValueOperation(str):
    i = 0
    result = None
    while i < len(str) and str[i] == ' ' :
        i += 1
    if i == len(str):
        raise BaseException("Inexistant Value In Operation.")
    elif str[i] in "0123456789" :
        try :
            result = float(str)
        except :
            raise BaseException(f"{str} cannot be convert to number")
    else :
        save = i
        while i < len(str) and str[i] != ' ' :
            i+= 1
        result = str[save : i]
        while i < len(str) and str[i] == ' ' :
            i += 1
        if i != len(str):
            raise BaseException(f"'{str}' cannot be variable name.")
    return result

def addMultToOperation(ope, mult):
        while ope != None :
            if ope.operator == "^":
                if ope.right != None and ope.right.right != None :
                    ope = ope.right.right
            elif type(ope.left) == float :
                ope.left *= mult
                while ope != None  and ope.operator != None and ope.operator in "*/" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            else :
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = mult
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                while ope != None and ope.operator != None  and ope.operator in "*/" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            ope = ope.right
        return "Done"

class operation:
    
    def __init__(this, str) -> None:
        this.left = None
        this.operator = None
        this.right = None
        if len(str) == 0:
            return
        print(f"Need to parse {str}")
        i = 0
        try :
            save = -1
            count = 0
            while i < len(str) and str[i] == ' ':
                i+=1
            if i < len(str) and str[i] == '(' :
                save = i
                count = 1
                i+=1
                while i < len(str) and count != 0:
                    if str[i] == '(' :
                        count += 1
                    if str[i] == ')' :
                        count -=1
                    i+=1
                if (count != 0):
                    raise BaseException(f"No end to paranthese init at {save} index")
                else :
                    this.left = operation(str[save + 1 : i - 1])
            while i < len(str):
                if str[i] not in " 0123456789.abcdefghijclmnopqrstuvwxyz_":
                    if str[i] in "+-*/^":
                        if save == -1 :
                            this.left = parseValueOperation(str[0: i])
                        this.operator = str[i]
                        this.right = operation(str[i + 1:])
                        break
                    else :
                        raise BaseException(f"Unknow caracter '{str[i]}' at {i} index")
                elif save != -1 and str[i] != " ":
                    raise BaseException(f"Need Operator at {i} index (find '{str[i]}')")
                i+=1
            if this.left == None:
                this.left = parseValueOperation(str)
        except BaseException as exeption :
            raise exeption
        
    def opti(this):
        nbModif = 42
        while nbModif > 0:
            nbModif = this.selfOptiNumberAndNumber()
        this.selfOptiNumberAndOperation()
            
    def selfOptiNumberAndOperation(this):
        # TODO : finish function
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiNumberAndOperation()
                # print("Exit other branch")
            if (type(opera.left) == float and opera.right != None and type(opera.right.left) == operation) or (type(opera.left) == operation and opera.right != None and type(opera.right.left) == float):
                # print(f"try for {opera.left} {opera.operator} {opera.right.left}")
                if type(opera.left) == float:
                    nb = opera.left
                    ope = opera.right.left
                else :
                    nb = opera.right.left
                    ope = opera.left
                if opera.operator == "*" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addMultToOperation(ope, nb)
                # elif opera.operator == "/" and opera.right.left == 0.0 and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                #     raise BaseException("can't divise by 0.")
                # elif opera.operator == "/" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                #     result = opera.left / opera.right.left

                # elif opera.operator == "^":
                #     result = power(opera.left, opera.right.left)
                if result != None :
                    # print(f"opera done for {opera.left} {opera.operator} {opera.right.left}")
                    opera.operator = opera.right.operator
                    opera.right = opera.right.right
                    opera.left = ope
                    modifNb += 1
            if opera.operator != None and opera.operator == "^":
                degre = 2
            elif opera.operator != None and opera.operator in "/*":
                degre = 1
            else :
                degre = 0
            opera = opera.right
        return modifNb

        
    def selfOptiNumberAndNumber(this):
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiNumberAndNumber()
                # print("Exit other branch")
                if opera.left.operator == None:
                    opera.left = opera.left.left
            elif type(opera.left) == float and opera.right != None and type(opera.right.left) == float:
                # print(f"try for {opera.left} {opera.operator} {opera.right.left}")
                if opera.operator == "/" and opera.right.left == 0.0 and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    raise BaseException("can't divise by 0.")
                elif opera.operator == "/" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = opera.left / opera.right.left
                elif opera.operator == "*" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = opera.left * opera.right.left
                elif opera.operator == "+" and degre < 1 and (opera.right.operator == None or opera.right.operator not in "*/^"):
                    result = opera.left + opera.right.left
                elif opera.operator == "-" and degre < 1 and (opera.right.operator == None or opera.right.operator not in "*/^"):
                    result = opera.left - opera.right.left 
                elif opera.operator == "^":
                    result = power(opera.left, opera.right.left)
                if result != None :
                    # print(f"opera done for {opera.left} {opera.operator} {opera.right.left}")
                    opera.operator = opera.right.operator
                    opera.right = opera.right.right
                    opera.left = result
                    modifNb += 1
            if opera.operator != None and opera.operator == "^":
                degre = 2
            elif opera.operator != None and opera.operator in "/*":
                degre = 1
            else :
                degre = 0
            if result == None :
                opera = opera.right
        return modifNb
    
    def print(this):
        opera = this
        print(f"{opera.left}   {opera.operator}")
        while opera.right != None :
            opera = opera.right
            if (opera.operator != None) :
                print(f"{opera.left}   {opera.operator}")
            else :
                print(f"{opera.left}")
            
    def __repr__(this):
        if this.operator == None :
            str = f"{this.left}"
        else :
            str = f"({this.left} {this.operator} {this.right})"
        return str
    def __str__(this):
        if this.operator == None :
            str = f"{this.left}"
        else :
            str = f"({this.left} {this.operator} {this.right})"
        return str