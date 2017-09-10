#  File: ERsim.py
#  Description: Simulates an emergency room with queues
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 6/30/2017
#  Date Last Modified: 6/30/2017

# implements Queue class as exemplified in class
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]
    # added __str__ method for printing
    def __str__(self):
        return str(self.items)


def main():
    # initialized queues for different classes
    critical = Queue()
    serious = Queue()
    fair = Queue()
    # reads in text file
    in_file = open("ERsim.txt", "r")
    while 1:
        # processes text file
        line = in_file.readline()
        if not line:
            break
        line = line.split()
        # processes exit command
        if line[0] == "exit":
            print("Command: Exit")
            break
        # processes add command
        elif line[0] == "add":
            if line[1] == "Critical":
                critical.enqueue(line[2])
            elif line[1] == "Serious":
                serious.enqueue(line[2])
            elif line[1] == "Fair":
                fair.enqueue(line[2])
            # prints results
            print("Command: Add patient", line[2], "to", line[1], "queue")
            print()
            print("   Queues are:")
            print("   Fair:    ", fair)
            print("   Serious: ", serious)
            print("   Critical:", critical)
            print()
        # processes treat command and its sub commands
        elif line[0] == "treat":
            # processes treat next
            if line[1] == "next":
                patient = ""
                queue = ""
                print("Command: Treat next patient")
                print()
                if not critical.isEmpty():
                    patient = critical.dequeue()
                    queue = "Critical"
                elif not serious.isEmpty():
                    patient = serious.dequeue()
                    queue = "Serious"
                elif not fair.isEmpty():
                    patient = fair.dequeue()
                    queue = "Fair"
                else:
                    print("   No patients in queues")
                    print()
                    continue
                # prints the results
                print("   Treating", patient, "from", queue, "queue")
                print("   Queues are:")
                print("   Fair:    ", fair)
                print("   Serious: ", serious)
                print("   Critical:", critical)
                print()
            # processes the treat critical command
            elif line[1] == "Critical":
                print("Command: Treat next patient on Critical queue")
                print()
                if critical.isEmpty():
                    print("   No patients in queue")
                    print()
                    continue
                else:
                    # prints the results
                    print("   Treating", critical.dequeue(), "from Critical queue")
                    print("   Queues are:")
                    print("   Fair:    ", fair)
                    print("   Serious: ", serious)
                    print("   Critical:", critical)
                    print()
            # processes the treat serious command
            elif line[1] == "Serious":
                print("Command: Treat next patient on Serious queue")
                print()
                if serious.isEmpty():
                    print("   No patients in queue")
                    print()
                    continue
                else:
                    # prints the results
                    print("   Treating", serious.dequeue(), "from Serious queue")
                    print("   Queues are:")
                    print("   Fair:    ", fair)
                    print("   Serious: ", serious)
                    print("   Critical:", critical)
                    print()
            # processes the treat fair command
            elif line[1] == "Fair":
                print("Command: Treat next patient on Fair queue")
                print()
                if fair.isEmpty():
                    print("   No patients in queue")
                    print()
                    continue
                else:
                    # prints the results
                    print("   Treating", fair.dequeue(), "from Fair queue")
                    print("   Queues are:")
                    print("   Fair:    ", fair)
                    print("   Serious: ", serious)
                    print("   Critical:", critical)
                    print()
            # processes the treat all command
            elif line[1] == "all":
                print("Command: Treat all patients")
                print()
                # processes in order Critical > Serious > Fair
                while not critical.isEmpty():
                    print("   Treating", critical.dequeue(), "from Critical queue")
                    print("   Queues are:")
                    print("   Fair:    ", fair)
                    print("   Serious: ", serious)
                    print("   Critical:", critical)
                    print()
                while not serious.isEmpty():
                    print("   Treating", serious.dequeue(), "from Serious queue")
                    print("   Queues are:")
                    print("   Fair:    ", fair)
                    print("   Serious: ", serious)
                    print("   Critical:", critical)
                    print()
                while not fair.isEmpty():
                    print("   Treating", fair.dequeue(), "from Critical queue")
                    print("   Queues are:")
                    print("   Fair:    ", fair)
                    print("   Serious: ", serious)
                    print("   Critical:", critical)
                    print()
                # all Queues empty
                print("   No patients in queues")
                print()

main()