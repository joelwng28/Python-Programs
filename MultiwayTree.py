#  File: MultiwayTree.py
#  Description: Processes and compares multiway trees
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 8/3/2017
#  Date Last Modified: 8/3/2017


# defines the MultiwayTree class
class MultiwayTree:
    # initializes a MultiwayTree
    def __init__(self, pyTree):
        self.data = pyTree.pop(0)
        self.children = []
        pyTree = pyTree.pop(0)
        for child in pyTree:
            if len(child) > 0:
                self.children.append(MultiwayTree(child))

    # prints the tree out in preOrder notation
    def preOrder(self):
        print(str(self.data) + " ", end="")
        for child in self.children:
            child.preOrder()

    # determines if two trees are isomorphic
    def isIsomorphicTo(self, other):
        if len(self.children) != len(other.children):
            return False
        if len(self.children) == 0:
            return True
        for i in range(len(self.children)):
            if not self.children[i].isIsomorphicTo(other.children[i]):
                return False
        return True


def main():
    # reads in inputs from file
    file = open("MultiwayTreeInput.txt", "r")
    count = 1
    # reads two lines at a time
    while True:
        line1 = file.readline()
        line2 = file.readline()
        # strips new line character
        line1 = line1.rstrip()
        line2 = line2.rstrip()
        # determines if file has been exhausted
        if not line1 or not line2:
            break
        # prints the first tree
        print("Tree " + str(count) + ":  " + line1)
        pyTree = eval(line1)
        # makes the tree
        tree = MultiwayTree(pyTree)
        # prints the preOrder notation of the tree
        print("Tree " + str(count) + " preorder:   ", end="")
        tree.preOrder()
        print()
        print()
        count += 1
        # prints the second tree
        print("Tree " + str(count) + ":  " + line2)
        pyTree = eval(line2)
        # makes the second tree
        tree1 = MultiwayTree(pyTree)
        # prints the preOrder notation of the second tree
        print("Tree " + str(count) + " preorder:   ", end="")
        tree1.preOrder()
        print()
        print()
        # determines and prints if the trees are isomorphic
        if tree.isIsomorphicTo(tree1):
            print("Tree " + str(count - 1) + " is isomorphic to Tree " + str(count))
        else:
            print("Tree " + str(count - 1) + " is not isomorphic to Tree " + str(count))
        count += 1
        print()
        print()

main()
