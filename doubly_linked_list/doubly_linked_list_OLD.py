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
        text += f"= HEAD: {self.head}\n"
        text += f"= TAIL: {self.tail}\n"
        text += f"= LIST-->\n"
        current = self.head
        while current is not None:
            text += f"= {current.value}\n"
            current = current.next
        return text

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        if self.length == 0:
            self.__init__(ListNode(value))
        else:
            newNode = ListNode(value, prev=None, next=self.head)
            self.head.prev = newNode
            self.head = newNode
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length <= 1:
            val = self.head
            self.__init__()
        else:
            val = self.head
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
        if self.length == 0:
            self.__init__(ListNode(value))
        else:
            newNode = ListNode(value, next=None, prev=self.tail)
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length <= 1:
            val = self.head
            self.__init__()
        else:
            val = self.tail
            self.tail = val.prev
            self.tail.next = None
            self.length -= 1
        return val.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.head == node:
            return
        else:
            current = self.head
            while current != node:
                current = current.next
            # now current is pointing to the proper node
            if current == self.tail:
                self.tail = current.prev
            if current.next:
                current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current.prev = None
        current.next = self.head
        self.head.prev = current
        self.head = current

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        current = self.head
        while current != node:
            current = current.next
        if current == self.head:
            self.head = current.next
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        current.prev = self.tail
        current.next = None
        self.tail.next = current
        self.tail = current

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # startting iterations on head
        current = self.head
        # single item list or empty
        if self.length <= 1 or current == node:
            self.remove_from_head()
            return
        # loop to find element to delete
        while current.next != None and current != node:
            current = current.next

        if current == self.head:
            self.head == None
        # is it the tail

        # else node.delete()
        # delete logic HERE
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        self.length -= 1
        # doesn't actually account for deleting tail element oops

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        the_max = self.head.value
        current = self.head
        while current:
            the_max = current.value if current.value > the_max else the_max
            current = current.next
        return the_max


x = DoublyLinkedList(ListNode(3))
print(x)
x.delete(ListNode(3))
print(x)
