def reverse(x: int) -> int:

    max_int = 2**31 - 1
    min_int = -2**31

    result = 0

    while x:
        # python modulo is not remainder, it is true mathematical modulo
        # therefore, to get remainder, the following calculations must be 
        # done if the input integer is < 0.
        if x < 0:
            # if x is a negative mulitple of ten, then the trailing digit is 0
            if x % 10 == 0:
                digit = 0
            # otherwise, the remainder is calculated as such
            else:
                digit = (10 - (x % 10)) * -1
        # if x is positive, the modulo functions as expected and gets the remainder
        else:
            digit = x % 10

        # divide input by 10 and round off the decimal places
        x = int(x / 10)

        # check for overflow
        if (result > max_int // 10) or (result == max_int // 10 and digit >= max_int % 10):
            return 0
        if (result < min_int // 10) or (result == min_int // 10 and digit <= (10 - (min_int % 10))):
            return 0
        
        result = (result * 10) + digit
    
    return result



print(reverse(123))

########################
# MY ORIGINAL SOLUTION #
########################

# this is incorrect because int(num_str) below cannot be run in an environment
# that cannot store ints > 2**31 - 1, which this step is requiring

def reverse(x: int) -> int:
    x_str = str(x)
    x_str_list = [s for s in x_str]

    if x_str_list[0] == '-':
        x_str_list.pop(0)
        x_str_list.reverse()
        num_str = ''.join(x_str_list)
        num = int(num_str) * -1
    else:
        x_str_list.reverse()
        num_str = ''.join(x_str_list)
        num = int(num_str)

    if num < -2**31 or num > 2**31 - 1:
        return 0
    else:
        return num

