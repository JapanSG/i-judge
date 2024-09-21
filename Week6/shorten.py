'''shorten'''
from Node import Node
class Linked:
    '''Linked lis class'''
    def __init__(self,val = None):
        '''Contructor'''
        if val is None:
            self.node = None
            self.head = self.node
            self.tail = self.node
        else:
            self.node = Node(val)
            self.head = self.node
            self.tail = self.node
    def add(self,val):
        '''add'''
        if self.node is None:
            self.node = Node(val)
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    def __str__(self):
        '''toString'''
        string = ""
        pointer = self.head
        while pointer is not None:
            string += f"{pointer.val}, "
            pointer = pointer.next
        return string
def main():
    '''Driver Code'''
    lis = Linked()
    num = int(input())
    while num != -1:
        lis.add(num)
        num = int(input())
    pointer = lis.head
    if pointer is not None:
        pointer.get_val()
        pointer.ser_val()
    string = ""
    while pointer is not None:
        head = pointer.val
        while pointer.next is not None:
            if pointer.next.val == pointer.val+1:
                pointer = pointer.next
            else:
                break
        if head == pointer.val:
            string += f"{head}"
            if pointer.next is not None:
                string += ", "
        else:
            string += f"{head}-{pointer.val}"
            if pointer.next is not None:
                string += ", "
        pointer = pointer.next
    print(string)
    print(lis)
main()
