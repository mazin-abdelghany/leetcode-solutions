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


print(reverse(1534236469))