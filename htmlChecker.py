#  File: htmlChecker.py
#  Description: Checks an html file to make sure symbols match
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 6/26/2017
#  Date Last Modified: 6/26/2017


# defines the Stack class as described in class
class Stack (object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    # added __str__ method for printing
    def __str__(self):
        return str(self.items)


def getTag(file):
    # initializes variables needed for method
    tags = []
    temp = ""
    write = False
    # processes valid characters
    for line in file:
        for char in line:
            if char in "> ":
                if temp != "":
                    tags.append(temp)
                    temp = ""
                    write = False
            if write:
                temp += char
            if char == "<":
                write = True
    return tags


def main():
    # initialized variables needed for process
    VALIDTAGS = []
    EXCEPTIONS = ["br", "hr", "meta"]
    stack = Stack()
    # processes file
    in_file = open("htmlfile.txt", "r")
    tags = getTag(in_file)
    print("tagList =", tags)
    print()
    # raises error if tag does not match
    try:
        for tag in tags:
            # ignore tags in exception
            if tag in EXCEPTIONS:
                print("Tag", tag, "does not need to match:  stack is still", stack)
                continue
            # updates valid tags
            if tag not in VALIDTAGS:
                print("New tag", tag, "found and added to list of valid tags")
                VALIDTAGS.append(tag)
            # matching tag
            if tag[0] != "/":
                stack.push(tag)
                print("Tag", tag, "pushed:  stack is now", stack)
            # processes tag
            else:
                stackTop = stack.pop()
                if stackTop == tag[1:len(tag)]:
                    print("Tag", tag, "matches top of stack:  stack is now", stack)
                else:
                    print()
                    print("Error:  tag is", tag, "but top of stack is", stackTop)
                    raise ValueError
        # end of function outputs
        if stack.isEmpty():
            print()
            print("Processing complete.  No mismatches found.")
        else:
            print()
            print("Processing complete.  Unmatched tags remain on stack: ", stack)
        in_file.close()
    except ValueError:
        pass
    # final values of VALIDTAGS and EXCEPTIONS
    print()
    VALIDTAGS.sort();
    print("VALIDTAGS =", VALIDTAGS)
    print("EXCEPTIONS =", EXCEPTIONS)

main()
