def longestPalindrome(s: str) -> str:

    substr = ""
    substr_len = 0


    for i, _ in enumerate(s):
        # odd palindromes
        left_pntr, right_pntr = i, i
        while left_pntr >= 0 and right_pntr < len(s) and s[left_pntr] == s[right_pntr]:
            if (right_pntr - left_pntr + 1) > substr_len:
                substr = s[left_pntr:right_pntr+1]
                substr_len = len(substr)
            left_pntr -= 1
            right_pntr += 1
        
        # even palindromes
        left_pntr, right_pntr = i, i+1
        while left_pntr >= 0 and right_pntr < len(s) and s[left_pntr] == s[right_pntr]:
            if (right_pntr - left_pntr + 1) > substr_len:
                substr = s[left_pntr:right_pntr+1]
                substr_len = len(substr)
            left_pntr -= 1
            right_pntr += 1

    return substr
            

print(longestPalindrome('aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa'))









#############################
# MY TIME TOO LONG SOLUTION #
#############################
# works, but rejected by leetcode for "time limit exceeded" with test case of
# long palindrome above
def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    
    def isPalindrome(s):
        if s == s[::-1]:
            return True
        else:
            return False

    palindromes = []

    for left_pointer in range(len(s)):
        for right_pointer in range(len(s)+1):
            
            substr = s[left_pointer:right_pointer]

            if isPalindrome(substr):
                if substr != '':
                    palindromes.append(substr)

    
    lengths = [len(x) for x in palindromes]

    index_longest = lengths.index(max(lengths))

    return palindromes[index_longest]