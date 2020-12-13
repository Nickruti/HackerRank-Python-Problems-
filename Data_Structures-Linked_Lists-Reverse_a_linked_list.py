'''
Problem url - https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    #if list is empty
    if head is None:
        return None
    prev = head
    node = prev.next
    
    #if list contain only one element
    if node is None:
        return head
    
    #if list contain only 2 element
    if node.next is None:
        node.next = prev
        prev.next = None
        head = node 
        return head
    
    #if list conatins more than 2 elements
    post = node.next
    node.next = prev
    prev.next = None
    
    #repeat until node pointer is at last node
    while post is not None:
        prev = node
        node = post
        post = post.next
        node.next = prev
    
    node.next = prev
    head = node
    return head
           
                              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
