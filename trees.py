class Node():

    def __init__(self,data,children=None):
        self.data=data
        self.children = children

    def __repr__(self):
        return "<Node {data}>".format(data=self.data)

    def find(self,data):
        to_visit =[self]
        while to_visit:
            current = to_visit.pop()
            if current.data == data:
                return current
            elif current.children != None:
                to_visit.extend(current.children)
        print("Node does not exist")
    
class Tree():
    def __init__(self,root):
        self.root=root
    
    def __repr__(self):
        return "<Tree root= {root}>".format(root=self.root)
    
    def find_in_tree(self,data):
        return self.root.find(data)

A = Node("A")
D = Node ("D")
F = Node ("F")
B = Node ("B",[A,D])
G = Node ("G",[F])
E = Node ("E",[B,G])


letters = Tree(E)