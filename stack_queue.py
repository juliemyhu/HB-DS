class Stack():
    
    def __init__(self):
        self.stack = []
        self.current_max = float("-inf")

    def push(self,number):
        
        if number > self.current_max:
            self.current_max = number
        self.stack.append((number,self.current_max))

    def peek(self):
        return self.stack[-1]
    
    def pop(self):

        top = self.peek()
        if top[1] != self.stack[-2]:
            self.current_max = self.stack[-2][1]
        self.stack.pop()

    def is_empty(self):
        return self.stack is None 

    def max(self):
        return self.current_max
    

    
s1 = Stack()
s1.push(15)
s1.push(54)
s1.push(-63)
s1.push(2)
s1.push(32)

s2 = Stack()
s2.push(1)
s2.push(2)
s2.push(3)
s2.push(4)
s2.push(5)


# class Queue():
#     def __init__:
#         self.queue=[]

#     def enqueue(number):

#     def dequeue

#     def peek
#     def is_empty()
