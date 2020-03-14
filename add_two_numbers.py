#Definition for singly-linked list.

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    n1 = l1
    n2 = l2
    carry = 0
    ans_linked_list = []
    while n1 != None or n2 != None:
        num1 = num2 = 0
        if n1: 
            num1 = n1.val
            n1 = n1.next 
        if n2:
            num2 = n2.val 
            n2 = n2.next
        new_num = num1 + num2 + carry
        carry = 0
        if new_num >= 10:
            new_num = new_num%10 
            carry = 1
        #print("rel: ", new_num,  carry)
        ans_linked_list.append(ListNode(new_num))
    if carry == 1:
        ans_linked_list.append(ListNode(carry))
    head = ans_linked_list[0]
    new_node = head
    for node in ans_linked_list[1:]:
        new_node.next = node
        #print(new_node.val)
        new_node = node
    return head


#Input: (2 -> 4) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 5

l1 = ListNode(2)
n2 = ListNode(4)
l1.next = n2
#n3 = ListNode(3)
#n2.next = n3

l2 = ListNode(5)
n2 = ListNode(6)
l2.next = n2
n3 = ListNode(4)
n2.next = n3

addTwoNumbers(l1, l2)
