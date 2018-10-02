#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = Node(None) # Dummy Node
        self.tail = self.head
        self.count = 0
    def list_add(self, data):
        newNode = Node(data) # Create New Node to add
        self.tail.next = newNode # Set tail's next node to New Node
        self.tail = newNode # Set tail point to New Node
        self.count += 1 # Increase size by 1
    def list_remove(self, data):
        pointer = self.head# set pointer as head
        if self.head.next == self.tail:
            print("List is Empty") # if list is empty, print this message, and return
            return
        while pointer.next is not self.tail: # Follow next pointer until end of list
            if pointer.next.data == data: # if next Node's data is same with data which want to delete
                pointer.next = pointer.next.next # point current Node's next pointer to next next Node
                print("Remove successfully")
                self.count -= 1
                return 
            pointer = pointer.next # Keep search next datas
        if pointer.next == None: # It means, there are no data which want to delete
            print("There are No data")
            return 
    def list_print(self):
        pointer = self.head
        while pointer.next is not self.tail:
            pointer = pointer.next
            print(pointer.data, end=' ')
        print("")
    def list_size(self):
        print(self.count)
        return 
    def is_empty(self):
        return Head is None # Return True or False

