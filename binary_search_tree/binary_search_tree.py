"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        text = f"{self.value} "
        if self.left:
            text += str(self.left)
        if self.right:
            text += str(self.right)
        return text

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value) # root
        if node.right:
            node.right.in_order_print(node.right)

    # def in_order_print(self):
    #     if self.left:
    #         self.left.in_order_print()
    #     print(self.value)
    #     if self.right:
    #         self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()
        queue.append(node)

        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value)
        # ^ really don't need all that stuff
        # node.pre_order_dft(node)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)


# x = BSTNode(5)
# x.insert(3)
# x.insert(6)
# x.insert(1)
# x.insert(9)
# x.insert(4)
# x.insert(6)
# print(x)


# y = BSTNode(1)
# y.insert(8)
# y.insert(5)
# y.insert(7)
# y.insert(6)
# y.insert(3)
# y.insert(4)
# y.insert(2)
# print(y)
# y.dft_print(y)

# z = BSTNode(10)
# z.insert(5)
# z.insert(15)
# z.insert(3)
# z.insert(8)
# z.insert(1)
# z.insert(4)
# z.insert(13)
# z.insert(16)
# z.insert(12)
# z.insert(14)
# z.dft_print(z)
# z.pre_order_dft(z)
# print("\n===\n")
# z.post_order_dft(z)
# print("\n===\n")
# z.in_order_print()
# print("\n===\n")
# z.bft_print(z)
