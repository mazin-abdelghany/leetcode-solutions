def longestCommonPrefix(strs) -> str:
    
    # find the index of the shortest string
    # the shortest is needed so that the enumerate below does not
    # throw an index error
    str_lens = [len(i) for i in strs]
    index_of_shortest_string = str_lens.index(min(str_lens))
    
    # the first longest common prefix will be the shortest string in the list
    new_common = strs[index_of_shortest_string]
    
    # initialize a temporary list
    temp = []
    
    # iterate through the strings
    for i in range(len(strs)):
        
        # iterate through the common letters
        for index, letter in enumerate(new_common):
            
            # if the letter in the common variable is in the string
            # in the exact order, append it to the temporary variable
            # otherwise, break the loop
            if letter == strs[i][index]:
                temp.append(letter)
            else:
                break
        
        new_common = ''.join(temp)
        temp = []
    
    return new_common