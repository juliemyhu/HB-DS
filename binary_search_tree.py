class BinarySearchNode():
    def __int__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right 
    
    def __repr__(self):
        return "<BinaryNode {data}>".format(data=self.data)
    
    def find(self,data):
        current = self
        while current:
            if current.data == data:
                return current
            elif data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right

    def maxDepth(self,root):
        if root is None:
            return 0
        else:
            left = root.left
            right =root.right
        return max(self.maxDepth(left), self.maxDepth(right)) + 1 
    
node_3 = BinarySearchNode(3,BinarySearchNode(9),node_20)
node_20 = BinarySearchNode(,15,7)