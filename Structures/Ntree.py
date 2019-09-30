class Ntree:
    def __init__(self,value,size):
        self.size = size
        self.count = 0
        self.root = self.Node(value=value,size=size)

    def addChild(self,value):
        node = self.Node(value,self.size)
        if len(self.root.child) < self.size:
            self.root.child.append(node)
            return
        iter = self.root
        while len(iter.child) == self.size:
            for i in range(len(iter.child)):
                iter = iter.child[i]
                if(len(iter.child) < self.size):
                    iter.child.append(node)
                    return

    def showTree(self,node):
        x = node
        print(x.value)

    class Node:
        def __init__(self,value,size):
            self.child = []
            self.countChild = 0
            self.value = value


tree = Ntree(value=1,size=5)
tree.addChild(1)
tree.addChild(2)
tree.addChild(3)
tree.addChild(4)
tree.addChild(5)
tree.addChild(6)
tree.addChild(7)
tree.addChild(8)
tree.addChild(9)
tree.addChild(10)
tree.addChild(11)
tree.addChild(12)
tree.addChild(12)
tree.addChild(12)
tree.addChild(12)
tree.addChild(12)
tree.addChild(12)
tree.addChild(12)
tree.addChild(12)
tree.addChild(12)
tree.addChild(12)
print(tree.root.child)
print(tree.root.child[0].child)
print(tree.root.child[0].child[0].child)
print(tree.root.child[1].child)
print(tree.root.child[2].child)
print(tree.root.child[3].child)
print(tree.root.child[4].child)
print(tree.root.child[1].child)
print(tree.root.child[2].child)

print(len(tree.root.child[1].child))
