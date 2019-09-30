class BinnaryTree:
    def __init__(self,value):
        self.root = self.Node(value=value)
        self.size = 1
        self.Node.count += 1

    def add(self, value):
        if(self.size == 1):
            node = self.Node(value)
            if(value > self.root.value):
                self.root.right = node
            else:
                self.root.left = node
            self.size+=1
            self.Node.count+=1
            return
        x = self.root
        while(x is not None):
            if(value > x.value):
                if(x.right is None):
                    x.right = self.Node(value)
                    self.Node.count += 1
                    return
                x = x.right
            else:
                if (x.left is None):
                    x.left = self.Node(value)
                    self.Node.count += 1
                    return
                x = x.left

    def showTree(self,node):
        if(node is None):
            return
        print(str(node.index)+'.'+str(node.value))
        self.showTree(node.left)
        self.showTree(node.right)

    def delete(self,node,index):
        if (node is None):
            return
        if(node.left.index == index):
            node.left = None
            return
        if(node.right.index==index):
            node.right = None
            return


        self.delete(node=node.left,index=index)
        self.delete(node=node.right,index=index)

    def allNodeSumm(self,node,sum):
        if(node is None):
            return
        sum+=node.value
        self.allNodeSumm(node.right,sum)
        self.allNodeSumm(node.left,sum)

    def find(self, value):
        x = self.root
        while x.value != value :
            if(value > x.value):
                x = x.right
            else:
                x = x.left
            if x is None:
                return
        return [x.index, x.value]

    class Node:

        count = 0
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value
            self.index = self.count


tree = BinnaryTree(5)
tree.add(6)
tree.add(2)
tree.add(7)
tree.add(3)
tree.add(7)
tree.add(8)
tree.showTree(tree.root)
print(tree.find(3))
tree.delete(node=tree.root,index=1)
print('---------')
tree.showTree(tree.root)
print(BinnaryTree.Node.count)
print(tree.root.index)
print(tree.root.left.index)