# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mathFunction.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lflandri <liam.flandrinck.58@gmail.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/23 20:35:34 by lflandri          #+#    #+#              #
#    Updated: 2024/04/23 20:35:35 by lflandri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def power(flt1, flt2) -> float:
    result = flt1
    if flt2 == 0 :
        return 1
    if flt2 == 1 :
        return flt1
    for i in range(int(flt2)):
        result *= flt1
    return result

def sqrt(n):
    i = 0
    result = 1
    while i < 50:
        result = (result + (n / result)) / 2
        i+=1
    return result