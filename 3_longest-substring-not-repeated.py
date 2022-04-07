def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left_pointer = 0
    substr_count = 0

    for right_pointer in range(len(s)):

        # print('start:')
        # print('left', left_pointer, 'right', right_pointer)
        # print('set', char_set)
        # print('string', s[left_pointer], s[right_pointer])
        # print('count', substr_count, '\n')
        

        while s[right_pointer] in char_set:
            char_set.remove(s[left_pointer])
            left_pointer += 1

        char_set.add(s[right_pointer])
        substr_count = max(substr_count, (right_pointer - left_pointer + 1) )
        
        # print('end:')
        # print('left', left_pointer, 'right', right_pointer)
        # print('set', char_set)
        # print('string', s[left_pointer], s[right_pointer])
        # print('count', substr_count, '\n')
    
    return substr_count


print(lengthOfLongestSubstring('dvdef'))