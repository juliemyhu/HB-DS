import Node from node.py

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

    #traversing through linkedlist
    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    #O(1)
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

    
    def remove_by_index(self,index):
        if self.head is None:
            return 
        if index == 0:
            self.head= self.head.next

    def delete_dups(self):
        nums = set()
        current = self.head
        previous = None
        while current != None:
            if current.data in nums:
                previous.next = current.next
            else:
                nums.add(current.data)
                previous = current
            current = current.next

    def rearrange(self):
        if self.head is None:
            return 
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow
        temp = 0
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
    
        n1= self.head
        n2 = prev
        print(n2.data)
        while n2.next:
            temp = n1.next
            n1.next=n2
            n1 = temp

            temp = n2.next
            n2.next = n1
            n2 = temp
        
    

fruitll = LinkedList()
fruitll.append("apple")
fruitll.append("berry")
fruitll.append("durian")
fruitll.append("elderberry")
fruitll.append("fig")

numsll = LinkedList()
numsll.append(2)
numsll.append(2)
numsll.append(3)
numsll.append(3)
numsll.append(5)


