###############
# MY SOLUTION #
###############
def canConstruct(ransomNote: str, magazine: str) -> bool:

    # deconstruct ransomNote and magazine into lists
    # sort them by alphabetical order
    # check first letter of ransomNote with first letter of magazine
        # if they are equal, remove them
            # if removing them makes len(ransomNote) == 0
                # break
        # if they are not equal, return false
        
    
    # deconstruct ransomNote and magazine into lists
    note_list = [char for char in ransomNote]
    magazine_list = [char for char in magazine]
    
    # sort them by alphabetical order
    note_list.sort()
    magazine_list.sort()
    
    # implement the for loop
    while len(magazine_list) > 0:
        if note_list[0] == magazine_list[0]:
            note_list.pop(0)
            magazine_list.pop(0)
            if len(note_list)==0: return True
        else:
            magazine_list.pop(0)
            if len(magazine_list)==0: return False

###################
# BETTER SOLUTION #
###################
def canConstruct(ransomNote: str, magazine: str) -> bool:
    for letter in ransomNote:
        if letter in magazine:
            magazine = magazine.replace(letter, "", 1)
        else:
            return False
    return True