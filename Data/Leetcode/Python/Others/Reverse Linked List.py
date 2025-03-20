# https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

"""
Given the head of a singly linked list, reverse the list, and return the reversed list
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resultNode = None
        currentNode = head

        while currentNode:
            temp = currentNode.next
            currentNode.next = resultNode
            resultNode = currentNode
            currentNode = temp

        return resultNode
    

node3 = ListNode(3)
node2 = ListNode(2, node3)
head = ListNode(1, node2)

solution = Solution()
reversedHead = solution.reverseList(head)

# Printing the reversed linked list
current = reversedHead
while current:
    print(current.val)
    current = current.next
