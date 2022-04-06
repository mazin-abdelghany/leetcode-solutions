# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

###############
# MY SOLUTION #
###############
class Solution:
    def isPalindrome(self, head) -> bool:
        
        list = []
        current_node = head
        
        while current_node is not None:
            list.append(current_node.val)
            current_node = current_node.next
        
        return list == list[::-1]