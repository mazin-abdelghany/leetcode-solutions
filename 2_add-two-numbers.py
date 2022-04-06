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
    #     
    #     Ideal naming would not be "result" and "dummy"
    #     Better would be "current_result" and "container"

    for letter in ans_list:
        result.next = ListNode(int(letter))
        result = result.next
    
    # dummy.next is returned because the first value in dummy is 0
    # (see the linked list definition above)
    return dummy.next


######################
# DIFFERENT SOLUTION #
######################
def addTwoNumbers(l1, l2):

    # initialize the linked list
    container = ListNode()
    current_result = container

    # remember the carry
    carry = 0

    while (l1 or l2 or carry):
        # pull the first values from each input linked list
        l1_value = l1.val if l1 is not None else 0
        l2_value = l2.val if l2 is not None else 0

        # new digit to insert into the final result
        insert_value = l1_value + l2_value + carry

        # get the carry
        # floor division is used so that when the insert_value is >10,
        # the carry is 1 and with the insert_value is <10, the carry is 0
        # another way of saying this is:
        #      carry = 1 if carry > 10 else 0
        carry = insert_value // 10 

        # then, keep only the ones place of the insert_value, since we removed
        # the 1 in the tens place above
        # if the insert value is >10, this operation gives the ones place
        # if the insert value is <10, this operation keeps the insert_value the same
        insert_value = insert_value % 10

        # insert the value into the linked list
        current_result.next = ListNode(insert_value)

        # update pointers
        current_result = current_result.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return container.next