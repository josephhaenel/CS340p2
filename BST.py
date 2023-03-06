class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def treeInsert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z


            
    def search(self, x, k):  # Iterarive Search
        # Search for a node in the BST
        # Return the node of key looking for
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def printParentKey(self, key):
        x = self.search(self.root, key)
        if x == None:
            print("NIL")
        else:
            if x.parent == None:
                print("NIL")
            else:
                print(x.parent.key)

    def printRightChild(self, key):
        x = self.search(self.root, key)
        if x == None or x.right == None:
            print("NIL")
        else:
            print(x.right.key)

    def printLeftChild(self, key):
        x = self.search(self.root, key)
        if x == None or x.left == None:
            print("NIL")
        else:
            print(x.left.key)
            
    def printPathToRoot(self, key):
        node = self.search(self.root, key)
        if node is None:
            return
        path = []
        while node is not None:
            path.append(node.key)
            node = node.parent
        print(path)
        

    def inOrderTraversal(self, node):
        if node is None:
            return []
        left_vals = self.inOrderTraversal(node.left)
        right_vals = self.inOrderTraversal(node.right)
        return left_vals + [node.key] + right_vals


    # def inorderTreeTraversal(self, sNode):
    #     if sNode != None:
    #         self.inorderTreeTraversal(sNode.left)
    #         print(sNode.key)
    #         self.inorderTreeTraversal(sNode.right)
            
# Testing
if __name__ == "__main__":
    my_tree = Tree()
    my_tree.treeInsert(Node(5))
    my_tree.treeInsert(Node(3))
    my_tree.treeInsert(Node(7))
    my_tree.treeInsert(Node(2))
    my_tree.treeInsert(Node(1))
    my_tree.treeInsert(Node(0))

    my_tree.printPathToRoot(0)
    
    print(my_tree.search(my_tree.root, 3))
    
    print(my_tree.printInOrderTraversal())

    # my_tree.printRightChild(5)
    # my_tree.printLeftChild(5)

    # result = my_tree.search(my_tree.root, 3)

    # print(result)
    # print(result.key)

    # my_tree.printParentKey(3)
    # my_tree.printParentKey(5)
    # my_tree.printParentKey(7)

    # my_tree.inorderTreeTraversal(my_tree.root)


