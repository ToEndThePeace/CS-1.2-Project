"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   
"""
import importlib
import sys
sys.path.append('singly_linked_list')

listLib = importlib.import_module("singly_linked_list")
LinkedList = listLib.LinkedList

# with arrays
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size       

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)
#         return

#     def pop(self):
#         if self.size == 0:
#             return
#         val = self.storage[self.size - 1]
#         self.size -= 1
#         self.storage.remove(val)
#         return val

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size
    
    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        return
    
    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        val = self.storage.remove_tail()
        return val