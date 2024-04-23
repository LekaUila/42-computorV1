# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/23 13:34:57 by lflandri          #+#    #+#              #
#    Updated: 2024/04/23 16:29:40 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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


class operation:
    
    def __init__(this, str) -> None:
        this.left = None
        this.operator = None
        this.right = None
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
        # this.checKVariableAndValue()
        
    def checKVariableAndValue(this):
        opera = this
        if type(this.left) == operation:
            this.left.checKVariableAndValue()
        elif type(this.left) != float :
            this.left = parseValueOperation(this.left)
        while opera.right != None :
            opera = opera.right
            if type(opera.left) == operation:
                opera.left.checKVariableAndValue()
            elif type(opera.left) != float :
                opera.left = parseValueOperation(opera.left)
                
    def selfOpti(this):
        return
    
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