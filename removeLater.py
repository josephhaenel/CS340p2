class Node:
    def __init__(self, parent, left, key, right):
        self.parent = parent
        self.left = left
        self.key = key
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def create_node(self, parent, left, key, right):
        return Node(parent, left, key, right)

    def remove_node(self, del_node):
        if self.is_leaf(del_node):
            parent = del_node.parent
            if parent.right == del_node:
                parent.right = None
            else:
                parent.left = None
            del del_node
        elif self.has_left_child_only(del_node):
            parent = del_node.parent
            if parent.left == del_node:
                parent.left = del_node.left
            else:
                parent.right = del_node.left
            del del_node
        elif self.has_right_child_only(del_node):
            parent = del_node.parent
            if parent.left == del_node:
                parent.left = del_node.right
            else:
                parent.right = del_node.right
            del del_node
        else:
            successor = del_node.right
            while successor.left != None:
                successor = successor.left
            del_node.key = successor.key
            if del_node.right == successor:
                del_node.right = successor.right
            else:
                parent = successor.parent
                parent.left = successor.right
            del successor

    def has_two_children(self, node):
        return node.left and node.right

    def has_left_child_only(self, node):
        return node.left and not node.right

    def has_right_child_only(self, node):
        return node.right and not node.left

    def is_leaf(self, node):
        return not node.left and not node.right

    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            return node.key
            self.inorder(node.right)

    def find(self, key):
        iter = self.root
        while iter != None:
            if key == iter.key:
                return iter.key
            elif key < iter.key:
                iter = iter.left
            else:
                iter = iter.right
        raise ValueError(str(key) + " not found.")

    def insert(self, key):
        if self.root == None:
            self.root = self.create_node(None, None, key, None)
        else:
            parent = self.root
            while parent != None:
                if key < parent.key:
                    if parent.left == None:
                        parent.left = self.create_node(parent, None, key, None)
                        parent = None
                    else:
                        parent = parent.left
                else:
                    if parent.right == None:
                        parent.right = self.create_node(
                            parent, None, key, None)
                        parent = None
                    else:
                        parent = parent.right

    def remove(self, key):
        del_node = self.root
        while del_node != None:
            if key == del_node.key:
                self.remove_node(del_node)
                return True
            elif key < del_node.key:
                del_node = del_node.left
            else:
                del_node = del_node.right
        raise ValueError("Did not remove " + str(key) + ". It was not found.")

    def inorder_traversal(self):
        self.inorder(self.root)

    def is_empty(self):
        return self.root == None
