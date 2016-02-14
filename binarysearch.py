import sys
import random

class TreeNode(object):
    def __init__(self,key,value=None,rightChild=None,leftChild=None,parent=None):
        self.key = key
        self.payload = value
        self.rightChild = rightChild
        self.leftChild = leftChild
        self.parent = parent
        self.root=0

    def make_root(self):
        self.root=1

    def assign_left_child(self,leftChild):
        self.leftChild=leftChild

    def assign_right_child(self,rightChild):
        self.rightChild=rightChild

    def assign_parent(self,parent):
        self.parent=parent

    def has_any_child(self):
        return self.leftChild or self.rightChild

class BinarySearchTree(object):
    def __init__(self,root_node):
        self.root_node = root_node
        self.visited = []
        self.right_visited = []

    def insert_node(self,current_node,new_node):
        if new_node.key > current_node.key:
            if current_node.rightChild is None:
                current_node.rightChild = new_node
                new_node.parent = current_node
                return 1
            else:
                self.insert_node(current_node.rightChild,new_node)
        elif new_node.key < current_node.key:
            if current_node.leftChild is None:
                current_node.leftChild = new_node
                new_node.parent=current_node
                return 1
            else:
                self.insert_node(current_node.leftChild,new_node)

    def inorder(self,node):
        if node.leftChild:
            for elem in self.inorder(node.leftChild):
                yield elem
        yield node
        if node.rightChild:
            for elem in self.inorder(node.rightChild):
                yield elem


    def preorder(self,node):
        yield node
        if node.leftChild:
            for elem in self.preorder(node.leftChild):
                yield elem
        if node.rightChild:
            for elem in self.preorder(node.rightChild):
                yield elem

    def postorder(self,node):
        if node.leftChild:
            for elem in self.postorder(node.leftChild):
                yield elem
        if node.rightChild:
            for elem in self.postorder(node.rightChild):
                yield elem
        yield node

    def traverse(self,start,chooser):
        return chooser(start)



if __name__ == "__main__":
    root_node = TreeNode(7,'/')
    search_tree = BinarySearchTree(root_node)
    for number,payload in [(1,'+'),(0,'0'),(3,'*'),(2,'2'),(5,'*'),(4,'4'),(6,'6'),(9,'-'),(8,'8'),(10,'10')]:
        search_tree.insert_node(root_node,TreeNode(number,payload))

    print("Postorder",[x.payload for x in search_tree.traverse(root_node,search_tree.postorder)])
    print("Preorder",[x.payload for x in search_tree.traverse(root_node,search_tree.preorder)])
    print("Inorder",[x.payload for x in search_tree.traverse(root_node,search_tree.inorder)])






