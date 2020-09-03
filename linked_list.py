class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def find(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True 
            current = current.next
        
        return False

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def append(self,data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove(self,data):

        if not self.head:
            raise Exception("does not exist")

        if self.head.data == data:
            self.head = self.head.next

        current = self.head

        while current.next is not None:
            if current.next.data== data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                break
            else:
                current = current.next  




fruitll = LinkedList()
fruitll.append("apple")
fruitll.append("berry")
fruitll.append("cherry")
fruitll.append("durian")
fruitll.append("elderberry")
fruitll.append("fig")

