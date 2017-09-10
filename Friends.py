#  File: Friends.py
#  Description: Use linked lists to implement the "friend" functionality of a Facebook-like application
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 7/11/2017
#  Date Last Modified: 7/11/2017


class Node (object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data            # returns a POINTER

    def getNext(self):
        return self.next            # returns a POINTER

    def setData(self, newData):
        self.data = newData         # changes a POINTER

    def setNext(self, newNext):
        self.next = newNext         # changes a POINTER


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        # add a new Node to the beginning of an existing list
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

# defines the class User


class User:
    # defines the init method
    def __init__(self, name):
        self.name = name
        self.friends = UnorderedList()
    # defines the comparison of users

    def __eq__(self, other):
        return self.name == other
    # defines the addAccount method

    def addAccount(self, name, users):
        users.add(User(name))

    def addFriend(self, name):
        self.friends.add(User(name))
    # defines the deleteFriend method

    def deleteFriend(self, name):
        self.friends.remove(name)
    # defines the listFriends method

    def listFriends(self):
        printList(self.friends)
    # defines the query method

    def query(self, name):
        return self.friends.search(name)

# prints the contents of a list


def printList(nodePtr):
    if nodePtr is not None:
        print(nodePtr.getData().name + " ", end="")
        printList(nodePtr.getNext())


def main():
    # list of users
    users = UnorderedList()
    # reads in a file
    in_file = open("FriendData.txt", "r")
    # processes each line
    for line in in_file:
        # formatting
        print()
        print("-->", line, end="")
        print("\t", end="")
        line = line.split()
        # processes the person command
        if line[0] == "Person":
            if users.search(line[1]):
                print("A person with name", line[1],  "already exists.")
                continue
            else:
                users.add(User(line[1]))
                print(line[1], "now has an account.")
        # processes the friend command
        elif line[0] == "Friend":
            # determines if names are valid
            if not users.search(line[1]):
                print("A person with name", line[1], "does not currently exist.")
                continue
            elif not users.search(line[2]):
                print("A person with name", line[2], "does not currently exist.")
                continue
            else:
                # adds to eachother's list of friends
                temp = users.head
                while temp is not None:
                    if temp.getData().name == line[1]:
                        break
                    temp = temp.getNext()
                if temp.getData().friends.search(line[2]):
                    print(line[1], "and", line[2], "are already friends.")
                    continue
                elif temp.getData().name == line[2]:
                    print("A person cannot friend him/herself.")
                    continue
                else:
                    temp.getData().addFriend(line[2])
                    temp = users.head
                    while temp is not None:
                        if temp.getData().name == line[2]:
                            break
                        temp = temp.getNext()
                    temp.getData().addFriend(line[1])
                    print(line[1], "and", line[2], "are now friends.")
        # processes the unfriend method
        elif line[0] == "Unfriend":
            # determines if inputs are valid
            if not users.search(line[1]):
                print("A person with name", line[1], "does not currently exist.")
                continue
            elif not users.search(line[2]):
                print("A person with name", line[2], "does not currently exist.")
                continue
            else:
                # removes users from eachother's friends lists
                temp = users.head
                while temp is not None:
                    if temp.getData().name == line[1]:
                        break
                    temp = temp.getNext()
                if temp.getData().name == line[2]:
                    print("A person cannot unfriend him/herself.")
                    continue
                elif not temp.getData().friends.search(line[2]):
                    print(line[1], "and", line[2], "aren't friends, so you can't unfriend them.")
                    continue
                else:
                    temp.getData().deleteFriend(line[2])
                    temp = users.head
                    while temp is not None:
                        if temp.getData().name == line[2]:
                            break
                        temp = temp.getNext()
                    # prints the results
                    temp.getData().deleteFriend(line[1])
                    print(line[1], "and", line[2], "are no longer friends.")
        # defines the list command
        elif line[0] == "List":
            temp = users.head
            while temp is not None:
                if temp.getData() == line[1]:
                    break
                temp = temp.getNext()
            # determines if the inputs are valid
            if temp.getData().friends.isEmpty():
                print(line[1], "has no friends.")
            else:
                # prints the contents
                print("[ ", end="")
                printList(temp.getData().friends.head)
                print("]")
        # defines the query command
        elif line[0] == "Query":
            # determines if the inputs are valid
            if line[1] == line[2]:
                print("A person cannot query him/herself.")
                continue
            if not users.search(line[1]):
                print("A person with name", line[1], "does not currently exist.")
                continue
            if not users.search(line[2]):
                print("A person with name", line[2], "does not currently exist.")
                continue
            # processed the contents
            temp = users.head
            while temp is not None:
                if temp.getData().name == line[1]:
                    break
                temp = temp.getNext()
            # prints the contents
            if temp.getData().friends.search(line[2]):
                print(line[1], "and", line[2], "are friends.")
            else:
                print(line[1], "and", line[2], "are not friends.")
        # processes the exit command
        elif line[0] == "Exit":
            print("Exiting...")
    in_file.close()

main()
