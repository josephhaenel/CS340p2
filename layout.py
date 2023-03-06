class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.key = key
        self.right = right
        
        
        
# Sample Insert
def treeInsert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def insert(root, key):
    parent = None
    curNode = root.
    
    # Insert a new node to the BST
    pass
    
def search(x, k): # Iterarive Search
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x
    # Search for a node in the BST
    # Return the node of key looking for
    
def inorderTreeTraversal(sNode):
    if sNode != None:
        inorderTreeTraversal(sNode.left)
        print(sNode.left)
        inorderTreeTraversal(sNode.right)
        
def printParentKey(key):
    # If the key exists in the tree, print the key of its parent node.
    # In case the key is at the root with no meaningful parent, print “NIL”.
    pass

def printRightChild(key):
    # If the key exists in the tree, print the key of its right child node.
    # In case the right child is NIL or NULL, print “NIL”.
    pass

def printLeftChild(key):
    # If the key exists in the tree, print the key of its left child node.
    # In case the left child is NIL or NULL, print “NIL”.
    pass

def printPathToRoot(key):
    # If the key exists in the tree, print its parent node’s key, its grand-parent’s
    # key, its great-grandparent’s key, …, all the way to the root
    pass

    
    

