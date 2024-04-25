# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/23 13:34:57 by lflandri          #+#    #+#              #
#    Updated: 2024/04/25 17:38:12 by lflandri         ###   ########.fr        #
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
        isPower = False
        while ope != None :
            if ope.operator == "^":
                isPower = True
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = mult
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            elif isPower :
                isPower = False
            elif type(ope.left) == float :
                ope.left *= mult
                while ope != None  and ope.operator != None and ope.operator in "*/^" :
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
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            if ope.operator != "^":
                ope = ope.right
        return "Done"
    
def addVMultToOperation(ope, mult, isReverse):
        # TODO : finish function 
        isPower = False
        while ope != None :
            if ope.operator == "^" and not isReverse:
                isPower = True
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = mult
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            elif isPower :
                isPower = False
            elif isReverse :
                while ope.right != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                print(f"for {ope} : test for {ope.left} {ope.operator} {ope.right}")
                newOpe = operation("")
                newOpe.left = mult
                newOpe.operator = ope.operator
                ope.operator = "/"
                newOpe.right = ope.right
                ope.right = newOpe
                print(f"result {ope} ")
                ope = ope.right
                if ope == None :
                    return "Done"
                # newOpe = operation(mult + "*" + mult)
                # newOpe.right.left = ope.left
                # ope.left = 1
                # newOpe.right.operator = ope.operator
                # ope.operator = "/"
                # newOpe.right.right = ope.right
                # ope.right = newOpe
                # while ope != None and ope.operator != None  and ope.operator in "*/^" :
                #     ope = ope.right
                # if ope == None :
                #     return "Done"
            else :
                print(f"for {ope} : test for {ope.left} {ope.operator} {ope.right}")
                newOpe = operation("")
                newOpe.left = ope.left
                ope.left = mult
                newOpe.operator = ope.operator
                ope.operator = "*"
                newOpe.right = ope.right
                ope.right = newOpe
                print(f"result {ope} ")
                while ope != None and ope.operator != None  and ope.operator in "*/^" :
                    ope = ope.right
                if ope == None :
                    return "Done"
            if ope.operator != "^":
                ope = ope.right
        return "Done"
class operation:
    
    def __init__(this, str) -> None:
        this.left = None
        this.operator = None
        this.right = None
        if len(str) == 0:
            return
        # print(f"Need to parse {str}")
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
                    raise BaseException(f"No end to paranthese init at {save} index of {str} string")
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
                        raise BaseException(f"Unknow caracter '{str[i]}' at {i} index of {str} string")
                elif save != -1 and str[i] != " ":
                    raise BaseException(f"Need Operator at {i} index of {str} string (find '{str[i]}')")
                i+=1
            if this.left == None:
                this.left = parseValueOperation(str)
        except BaseException as exeption :
            raise exeption
        
    def opti(this):
        nbModif = 42
        while nbModif > 0:
            nbModif = this.selfOptiNumberAndNumber()
            print(this)
        nbModif = 42
        while nbModif > 0:
            nbModif = this.selfOptiNumberAndOperation()
            nbModif += this.selfOptiVariableAndOperation()
            print(this)
            
            
    def selfOptiVariableAndOperation(this):
        opera = this
        degre = 0
        modifNb = 0
        while opera != None :
            result = None
            if type(opera.left) == operation:
                # print(f"Enter other branch {opera.left}")
                modifNb += opera.left.selfOptiVariableAndOperation()
                # print("Exit other branch")
            if (type(opera.left) == str and opera.right != None and type(opera.right.left) == operation) or (type(opera.left) == operation and opera.right != None and type(opera.right.left) == str):
                # print(f"try for {opera.left} {opera.operator} {opera.right.left}")
                if type(opera.left) == str:
                    nb = opera.left
                    ope = opera.right.left
                else :
                    nb = opera.right.left
                    ope = opera.left
                if opera.operator == "*" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addVMultToOperation(ope, nb, False)
                elif type(opera.right.left) == str and opera.operator == "/" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addVMultToOperation(ope,nb, True)

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
            
    def selfOptiNumberAndOperation(this):
        # TODO : finish function : ^
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
                elif type(opera.right.left) == float and opera.operator == "/" and opera.right.left == 0.0 and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    raise BaseException("can't divise by 0.")
                elif type(opera.right.left) == float and opera.operator == "/" and degre < 2 and (opera.right.operator == None or opera.right.operator != "^"):
                    result = addMultToOperation(ope, 1 / nb)

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
            
    def __repr__(this):
        returnValue = ""
        opera = this
        while opera != None :
            if (opera.operator != None) :
                if type(opera.left) == operation:
                    returnValue += f"({opera.left}) {opera.operator} "
                else :
                    returnValue += f"{opera.left} {opera.operator} "  
            else :
                if type(opera.left) == operation:
                    returnValue += f"({opera.left})"
                else :
                    returnValue += f"{opera.left}"
            opera = opera.right 
        return returnValue

    def __str__(this):
        returnValue = ""
        opera = this
        while opera != None :
            if (opera.operator != None) :
                if type(opera.left) == operation:
                    returnValue += f"({opera.left}) {opera.operator} "
                else :
                    returnValue += f"{opera.left} {opera.operator} "  
            else :
                if type(opera.left) == operation:
                    returnValue += f"({opera.left})"
                else :
                    returnValue += f"{opera.left}"
            opera = opera.right 
        return returnValue