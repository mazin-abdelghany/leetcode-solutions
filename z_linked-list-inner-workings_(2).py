import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ans_list = [7, 8, 9, 10]

dummy = ListNode()
result = dummy

print('dummy: ', dummy, ' ', dummy.val, ' ', dummy.next, '\n', 
      'result: ', result, ' ', result.val, ' ', result.next, '\n', sep='')

for num in ans_list:
    print('before node insertion:')
    print('result value: ', result.val, '\n', 'result next: ', result.next,'\n', sep='')
    print('dummy values: ')
    tmp = copy.deepcopy(dummy)
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next
    
    result.next = ListNode(num)
    print('num = ', num, sep='')
    print('result.next = ListNode(num)')
    print('after node insertion:')
    print('result value: ', result.val, '\n', 'result next: ', result.next, '\n', sep='')
    print('dummy values: ')
    tmp = copy.deepcopy(dummy)
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next

    result = result.next
    print('result = result.next')
    print('after node assignment:')
    print('result value: ', result.val, '\n', 'result next: ', result.next, '\n', sep='')
    print('dummy values: ')
    tmp = copy.deepcopy(dummy)
    while tmp is not None:
        print(tmp.val)
        tmp = tmp.next


while result is not None:
    print(result.val)
    result = result.next

while dummy is not None:
    print(dummy.val)
    dummy = dummy.next