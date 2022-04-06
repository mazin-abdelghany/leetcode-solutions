###############
# MY SOLUTION #
###############
def romanToInt(s: str) -> int:
    # 'MCMXCIV'
    # ['V' 'I' 'C' 'X' 'M'    'C' 'M']
    # [5,   1, 100, 10, 1000, 100, 1000]

    # have an empty list []
    # start at index 0
    # is index 0 > index 1?
        # yes, 
            # list[0] = index 1 - index 0
            # increase to index 2
        # no
            # list [0] = index[0]
            # increase index by 1

    atomic_romans = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    numerals = [char for char in s]
    numerals.reverse()
    
    arabic = [atomic_romans[numeral] for numeral in numerals]
    
    addition = []

    while len(arabic) >= 1:
        print(arabic, addition)
        num = arabic.pop(0)
        if len(arabic) == 0:
            addition.append(num)
            break
        if num > arabic[0]:
            addition.append(num - arabic[0])
            arabic.pop(0)
        else:
            addition.append(num)
            
    return sum(addition)

###################
# BETTER SOLUTION #
###################
def romanToInt(s: str) -> int:
    atomic_romans = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    rightmost_num = 0
    sum = 0

    for numeral in s[::-1]:
        if atomic_romans[numeral] >= rightmost_num:
            sum += atomic_romans[numeral]
        else:
            sum -= atomic_romans[numeral]
        rightmost_num = atomic_romans[numeral]
    return sum