
from math import ceil
from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_ = []
        # Loop in head, that is a list to contain number, until last number
        while head != None:
            # added first number of the list
            list_.append(head.val)
            # added next number of the list
            head = head.next

        # fined the middle of list for scaning the reversing position that have same position 
        half_index = int(ceil((len(list_) - 1) / 2))
        
        # reversal process
        for i in range(0, half_index):
            # if the first index not be the same last index that mean the list is not palindrome number
            if list_[i] != list_[len(list_) - 1 - i]:
                return False
        return True

print(Solution().isPalindrome([1, 2, 3, 2, 1]))