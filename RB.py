# Insert
# Search
# InOrderTreeTraversal
# Print Color(key)
# PrintParentKey(key)
# PrintParentColor(key)
# PrintLeftChild(key)
# PrintRightChild(key)
# PrintUncleColor(key)
# PrintPathToRoot(key)

class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.p = None


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, color='BLACK')
        self.root = self.nil

    def RBInsert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'RED'
        self.RBInsertFixup(z)


    def RBInsertFixup(self, z):
        while z.p.color == 'RED':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y is not None and y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self._LeftRotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self._RightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y is not None and y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self._RightRotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self._LeftRotate(z.p.p)
        self.root.color = 'BLACK'


    def _LeftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def _RightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        
    def RBSearch(self, key):
        x = self.root
        while x != self.nil and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x if x != self.nil else None

    def InOrderTreeTraversal(self, x=None):
        if x is None:
            x = self.root
        values = []
        if x != self.nil:
            values.extend(self.InOrderTreeTraversal(x.left))
            values.append(x.key)
            values.extend(self.InOrderTreeTraversal(x.right))
        return values
            
    def PrintColor(self, key):
        x = self.RBSearch(key)
        if x == self.nil:
            print("Key not found")
        else:
            print(x.color)
            
    def PrintParentKey(self, key):
        x = self.RBSearch(key)
        if x == self.nil:
            print("Key not found")
        elif x == self.root:
            print("NIL")
        else:
            print(x.p.key)

    def PrintParentColor(self, key):
        x = self.RBSearch(key)
        if x == self.nil:
            print("Key not found")
        elif x == self.root:
            print("NIL")
        else:
            print(x.p.color)
            
    def PrintLeftChild(self, key):
        x = self.RBSearch(key)
        if x == self.nil:
            print("Key not found")
        elif x.left != self.nil:
            print(x.left.key)
        else:
            print("NIL")

    def PrintRightChild(self, key):
        x = self.RBSearch(key)
        if x == self.nil:
            print("Key not found")
        elif x.right != self.nil:
            print(x.right.key)
        else:
            print("NIL")
            

    def PrintUncleColor(self, key):
        z = self.RBSearch(key)
        if not z:
            print("Node not found.")
        elif not z.p:
            print("Node has no parent.")
        else:
            if not z.p.p:
                print("Node's parent has no parent (i.e., root node).")
            else:
                if z.p == z.p.p.left:
                    uncle = z.p.p.right
                else:
                    uncle = z.p.p.left
                if not uncle:
                    print("Node's uncle is None (i.e., black).")
                else:
                    print("Node's uncle color is", uncle.color)


    def PrintPathToRoot(self, key):
        node = self.RBSearch( key)
        if node is None:
            print("Key not found in the tree")
        else:
            path = []
            while node is not None:
                if node.color == 'RED':
                    path.append((node.key, "RED"))
                else:
                    path.append((node.key, "BLACK"))
                node = node.p
            for i in range(len(path)-1, -1, -1):
                print(f"{path[i][0]}({path[i][1]})", end='')
                if i != 0:
                    print(" -> ", end='')
            print()
            
    def PrintDepth(self, key=None):
        # calculate the depth of the tree if key is not provided
        depth = 0
        if key is None:
            node = self.root
            while node != self.nil:
                depth += 1
                node = node.left

            print("Depth of the tree is:", depth)

        # If key is provided, calculate the depth of the node
        if key is not None:
            node = self.RBSearch(key)
            if node == self.nil:
                print("Key not found in the tree")
            else:
                depth = 0
                while node != self.root:
                    depth += 1
                    node = node.p
                print("Depth of node", key, "is:", depth)
             
            
# Testing code 
if __name__ == "__main__":   
    tree = RedBlackTree()
    tree.RBInsert(Node(5))
    tree.RBInsert(Node(10))
    tree.RBInsert(Node(20))
    tree.RBInsert(Node(30))
    tree.RBInsert(Node(40))
    tree.RBInsert(Node(50))
    tree.RBInsert(Node(60))
    tree.RBInsert(Node(70))
    tree.RBInsert(Node(80))
    tree.RBInsert(Node(90))
    tree.RBInsert(Node(100))
    tree.RBInsert(Node(110))
    tree.RBInsert(Node(0))
    # # print(tree.RBSearch(30).key)
    # print(tree.InOrderTreeTraversal())
    # tree.PrintColor(10)
    # tree.PrintParentKey(10)
    # tree.PrintParentColor(10)
    # tree.PrintLeftChild(10)
    # tree.PrintRightChild(20)
    # tree.PrintUncleColor(30)
    # tree.PrintUncleColor(20)
    # tree.PrintUncleColor(30)
    # tree.PrintUncleColor(5)
    # tree.PrintUncleColor(40)
    # tree.PrintUncleColor(50)
    # tree.PrintUncleColor(60)
    # tree.PrintUncleColor(70)
    # tree.PrintUncleColor(80)
    # tree.PrintUncleColor(90)
    # tree.PrintUncleColor(110)
    tree.PrintPathToRoot(10)
    tree.PrintPathToRoot(110)
    tree.PrintPathToRoot(0)
    tree.PrintDepth()
    tree.PrintDepth(110)
    tree.PrintDepth(0)

