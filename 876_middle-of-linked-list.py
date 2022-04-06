###############
# MY SOLUTION #
###############
def middleNode(self, head):
    
    node_value_fast = head
    node_value_slow = head
    
    while node_value_fast is not None:
        if node_value_fast.next is None:
            break
        node_value_fast = node_value_fast.next.next
        node_value_slow = node_value_slow.next
        
    return node_value_slow

##################
# OTHER SOLUTION #
##################
def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow