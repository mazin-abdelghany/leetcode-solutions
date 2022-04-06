# Definition of a singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

###############
# MY SOLUTION #
###############

def addTwoNumbers(l1, l2):
    # the first number is l1
    first_num = l1
    # create an empty list to fill in with the first number
    first_list = []
    
    # the second number is l2
    second_num = l2
    # create an empty list to fill in with the second number
    second_list = []
    
    # create two variables that point to the same linked list
    dummy = ListNode()
    result = dummy
    
    # deconstruct the first linked list into a list
    # add the numbers in as a string to allow for the below manipulations
    while first_num is not None:
        first_list.append(str(first_num.val))
        first_num = first_num.next
    
    # deconstruct the second linked list into a list
    # add the numbers in as a string to allow for the below manipulations
    while second_num is not None:
        second_list.append(str(second_num.val))
        second_num = second_num.next
        
    # the output of the above while loops returns a number that is reversed
    # so the list needs to be reversed
    first_list.reverse()
    second_list.reverse()
    
    # join list of separate numbers into a single string of the numbers to add 
    str_first_num = ''.join(first_list)
    str_second_num = ''.join(second_list)
    
    # add the two numbers together
    num = int(str_first_num) + int(str_second_num)
    # trun that back into a string
    num = str(num)
    
    # create a list from the string
    ans_list = [letter for letter in num]
    # reverse the list to enter it into the linked list
    ans_list.reverse()
    
    # this is the most challenging thing to understand for me
    # two helpful Python linked list concepts:
    #   1. when ListNode() is called a new "box" is made, 
    #   2. when a value is assigned to .next a new pointer is drawn (or moved)
    # applying these concepts to the below for loop these images can be drawn:
    #     before iteration 1: result and dummy point to the same location 
    #     in memory containing the same value of 0
    #
    #            result       dummy 
    #               \           /
    #                \         /
    #                 \       /
    #                 ---------
    #                 |   0   |
    #                 ---------    
    #    
    #     iteration 1:
    #     result.next() = ListNode(int(letter)) 
    #     draws a new pointer to a node that contains the first number
    #      
    #            result       dummy 
    #               \           /
    #                \         /
    #                 ---------
    #                 |   x   |
    #                 --------- 
    #                     |
    #                 ---------
    #                 |   y   |
    #                 --------- 
    #
    #     result = result.next 
    #     assigns result to the value of result.next, which points to the
    #     second linked list value
    #
    #            result        dummy 
    #             |             /
    #             |            /
    #             |   ---------
    #             |   |   x   |
    #             |   --------- 
    #             |       |
    #             |   ---------
    #             --->|   y   |
    #                 --------- 
    #
    #     after iterating over the whole list, the linked list will be complete
    #     with result pointing to the last item in the list and dummy pointing to
    #     the entire linked list.

    for letter in ans_list:
        result.next = ListNode(int(letter))
        result = result.next
    
    # dummy.next is returned because the first value in dummy is 0
    # (see the linked list definition above)
    return dummy.next