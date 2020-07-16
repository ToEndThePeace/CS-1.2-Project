"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __str__(self):
        text = "\n==============>\n"
        text += f"= LIST-->\n"
        text += "= "
        if self.length == 0:
            text += "EMPTY!\n"
        current = self.head
        while current is not None:
            text += f"{current.value} "
            current = current.next
        return text

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    #                                         <--     head      tail

    def add_to_head(self, value):
        print(f"add_to_head({value})")
        newNode = ListNode(value)
        if self.length == 0:
            # for empty list, reinitialize with new node
            self.__init__(newNode)
        else:
            # create the new node with the current head as its next node
            newNode.prev = None
            newNode.next = self.head
            #   ^  <------
            # self.head.prev === None
            self.head.prev = newNode
            self.head = newNode
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        print(f"remove_from_head()")
        val = self.head
        if self.length <= 1:
            self.__init__()
        else:
            self.head = val.next
            self.head.prev = None
            self.length -= 1
        return val.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        print(f"add_to_tail({value})")
        newNode = ListNode(value)
        if self.length == 0:
            self.__init__(newNode)
        else:
            newNode.prev = self.tail
            newNode.next = None
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        print(f"remove_from_tail()")
        val = self.tail
        if self.length <= 1:
            self.__init__()
        else:
            self.tail = val.prev
            self.tail.next = None
            self.length -= 1
        return val.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        node = node if isinstance(node, ListNode) else ListNode(node)
        print(f"delete({node})")
        # check for edge cases
        if self.length == 0:
            return
        elif self.head.value == node.value:
            print("---\/")
            return self.remove_from_head()
        else:
            # loop over every element of the list
            current = self.head
            while current:
                # break the loop on the first matching element
                if current.value == node.value:
                    break
                current = current.next  # at the last run, it's None

            # if current is none, no match was found in list
            if not current:
                # therefore, we return None
                return
            # otherwise, check if the only match was the tail
            if current == self.tail:
                print("---\/")
                return self.remove_from_tail()
            # remove whatever middle node we ended up with
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        print("= get_max()\n")
        the_max = self.head.value
        current = self.head
        while current:
            the_max = current.value if current.value > the_max else the_max
            current = current.next
        return the_max


y = DoublyLinkedList()
print(y)
y.add_to_tail(3)
y.add_to_tail(4)
y.add_to_tail(5)
y.add_to_tail(6)
y.add_to_tail(7)
y.add_to_tail(8)
print(y)
y.add_to_tail(5)
print(y)
y.delete(5)
y.delete(3)
print(y)
y.add_to_tail(8)
print(y)
y.delete(8)
y.delete(8)
print(y)
