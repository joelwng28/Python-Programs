#  File: ExpressionTree.py
#  Description: Processes arithmetic operations with a binary tree
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 7/30/2017
#  Date Last Modified: 7/30/2017


class BinaryTree:
    # initializes tree
    def __init__(self, initVal, parent):
        self.data = initVal
        self.left = None
        self.right = None
        self.parent = parent
    # creates a tree according to expr
    def createTree(self, expr):
        operators = ['+', '-', '*', '/']
        tags = expr.split()
        current = self
        # loops through elements
        for char in tags:
            if char == ")":
                current = current.getParent()
            elif char == "(":
                current.insertLeft(None)
                current = current.getLeftChild()
            elif char in operators:
                current.setRootVal(char)
                current.insertRight(None)
                current = current.getRightChild()
            else:
                current.setRootVal(char)
                current = current.getParent()
        return current
    # evaluates a tree
    def evaluate(self):
        # empty tree
        if self is None:
            return 0

        # leaf node
        if self.getLeftChild() is None and self.getRightChild() is None:
            return eval(self.getRootVal())

        # evaluate left tree
        left_sum = self.getLeftChild().evaluate()

        # evaluate right tree
        right_sum = self.getRightChild().evaluate()

        # check which operation to apply
        if self.getRootVal() == '+':
            return left_sum + right_sum

        elif self.getRootVal() == '-':
            return left_sum - right_sum

        elif self.getRootVal() == '*':
            return left_sum * right_sum

        else:
            return left_sum / right_sum
    # prints the tree in preorder
    def preOrder(self):
        print(self.getRootVal() + " ", end="")
        if self.getLeftChild():
            self.getLeftChild().preOrder()
        if self.getRightChild():
            self.getRightChild().preOrder()
    # prints the tree in post order
    def postOrder(self):
        if self.getLeftChild():
            self.getLeftChild().postOrder()
        if self.getRightChild():
            self.getRightChild().postOrder()
        print(self.getRootVal() + " ", end="")
    # sets the parent value
    def setParent(self, parent):
        self.parent = parent
    # returns the parent's value
    def getParent(self):
        return self.parent
    #inserts a left child
    def insertLeft(self, newNode):
        if self.left is None:
            self.left = BinaryTree(newNode, self)
        else:
            t = BinaryTree(newNode, self)
            self.left.setParent(t)
            t.left = self.left
            self.left = t
    # inserts a right child
    def insertRight(self, newNode):
        if self.right is None:
            self.right = BinaryTree(newNode, self)
        else:
            t = BinaryTree(newNode, self)
            self.left.setParent(t)
            t.right = self.right
            self.right = t
    # returns the left child
    def getLeftChild(self):
        return self.left
    # returns the right child
    def getRightChild(self):
        return self.right
    # sets the root's value
    def setRootVal(self, value):
        self.data = value
    # gets the root's value
    def getRootVal(self):
        return self.data


def main():
    # reads in file
    in_file = open("treedata.txt", "r")
    # loops through each line
    for line in in_file:
        # formatting output
        print("Infix expression:  " + line)
        # creates tree
        temp = BinaryTree(None, None)
        # formats the tree
        temp.createTree(line)
        # evaluates the expression
        print("   Value:   " + str(temp.evaluate()))
        print("   Prefix expression:   ", end="")
        # prints preorder equation
        temp.preOrder()
        print()
        print("   Postfix expression:   ", end="")
        # prints post order equation
        temp.postOrder()
        print()
        print()

main()
