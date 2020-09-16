class BinarySearchNode():
    def __init__(self, data=None, left=None, right=None):
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
    
    def levelOrder(self,root):
        levels = []

        if root is None:
            return levels

        def helper(node,level):
            if node:
                if len(levels)==level:
                    levels.append([])
                levels[level].append(node.data)

                helper(node.left,level+1)
                helper(node.right,level+1)
            
        helper(root,0)

        return levels
    

node_15 = BinarySearchNode(15)
node_7 = BinarySearchNode(7)
node_9 = BinarySearchNode(9)

node_20 = BinarySearchNode(20)
node_3 = BinarySearchNode(3)
node_20.right= node_7
node_20.left= node_15
node_3.right = node_20
node_3.left = node_9