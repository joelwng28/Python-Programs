#  File: sorting.py
#  Description: Simulates the runtimes of different sorting algorithms
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 6/14/2017
#  Date Last Modified: 6/14/2017

import random
import time
import sys
sys.setrecursionlimit(10000)


# imported sort functions
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


# random Bubble Sort function
def randomBubble(n):
    tempList = [i for i in range(n)]
    random.shuffle(tempList)
    total = 0.0
    for i in range(5):
        startTime = time.perf_counter()
        bubbleSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
        random.shuffle(tempList)
    return total/5


# random Insertion Sort function
def randomInsertion(n):
    tempList = [i for i in range(n)]
    random.shuffle(tempList)
    total = 0.0
    for i in range(5):
        startTime = time.perf_counter()
        insertionSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
        random.shuffle(tempList)
    return total/5


# random Merge Sort function
def randomMerge(n):
    tempList = [i for i in range(n)]
    random.shuffle(tempList)
    total = 0.0
    for i in range(5):
        startTime = time.perf_counter()
        mergeSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
        random.shuffle(tempList)
    return total/5


# random Quick Sort function
def randomQuick(n):
    tempList = [i for i in range(n)]
    random.shuffle(tempList)
    total = 0.0
    for i in range(5):
        startTime = time.perf_counter()
        quickSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
        random.shuffle(tempList)
    return total/5


# sorted Bubble Sort function
def sortedBubble(n):
    tempList = [i for i in range(n)]
    total = 0.0
    for i in range(5):
        startTime = time.perf_counter()
        bubbleSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# sorted Insertion Sort function
def sortedInsertion(n):
    tempList = [i for i in range(n)]
    total = 0.0
    for i in range(5):
        startTime = time.perf_counter()
        insertionSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# sorted Merge Sort function
def sortedMerge(n):
    tempList = [i for i in range(n)]
    total = 0.0
    for i in range(5):
        startTime = time.perf_counter()
        mergeSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# sorted Quick Sort function
def sortedQuick(n):
    tempList = [i for i in range(n)]
    total = 0.0
    for i in range(5):
        startTime = time.perf_counter()
        quickSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# reverse Bubble Sort function
def reverseBubble(n):
    total = 0.0
    for i in range(5):
        tempList = [i for i in range(n, 0, -1)]
        startTime = time.perf_counter()
        bubbleSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# reverse Insertion Sort function
def reverseInsertion(n):
    total = 0.0
    for i in range(5):
        tempList = [i for i in range(n, 0, -1)]
        startTime = time.perf_counter()
        insertionSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# reverse Merge Sort function
def reverseMerge(n):
    total = 0.0
    for i in range(5):
        tempList = [i for i in range(n, 0, -1)]
        startTime = time.perf_counter()
        mergeSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# reverse Quick Sort function
def reverseQuick(n):
    total = 0.0
    for i in range(5):
        tempList = [i for i in range(n, 0, -1)]
        startTime = time.perf_counter()
        quickSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# almost sorted Bubble Sort function
def almostBubble(n):
    total = 0.0
    for i in range(5):
        tempList = [k for k in range(n)]
        done = []
        # swaps 10% of the values
        for j in range(n // 10):
            randomIndex1, randomIndex2 = random.sample(range(len(tempList)), 2)
            while randomIndex1 in done or randomIndex2 in done:
                randomIndex1, randomIndex2 = random.sample(range(len(tempList)), 2)
            done.append(randomIndex1)
            done.append(randomIndex2)
            temp = tempList[randomIndex1]
            tempList[randomIndex1] = tempList[randomIndex2]
            tempList[randomIndex2] = temp
        startTime = time.perf_counter()
        bubbleSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total/5


# almost sorted Insertion Sort function
def almostInsertion(n):
    total = 0.0
    for i in range(5):
        tempList = [k for k in range(n)]
        done = []
        # swaps 10% of the values
        for j in range(n // 10):
            randomIndex1, randomIndex2 = random.sample(range(len(tempList)), 2)
            while randomIndex1 in done or randomIndex2 in done:
                randomIndex1, randomIndex2 = random.sample(range(len(tempList)), 2)
            done.append(randomIndex1)
            done.append(randomIndex2)
            temp = tempList[randomIndex1]
            tempList[randomIndex1] = tempList[randomIndex2]
            tempList[randomIndex2] = temp
        startTime = time.perf_counter()
        insertionSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total / 5


# almost sorted Merge Sort function
def almostMerge(n):
    total = 0.0
    for i in range(5):
        tempList = [k for k in range(n)]
        done = []
        # swaps 10% of the values
        for j in range(n // 10):
            randomIndex1, randomIndex2 = random.sample(range(len(tempList)), 2)
            while randomIndex1 in done or randomIndex2 in done:
                randomIndex1, randomIndex2 = random.sample(range(len(tempList)), 2)
            done.append(randomIndex1)
            done.append(randomIndex2)
            temp = tempList[randomIndex1]
            tempList[randomIndex1] = tempList[randomIndex2]
            tempList[randomIndex2] = temp
        startTime = time.perf_counter()
        mergeSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total / 5


# almost sorted Quick Sort function
def almostQuick(n):
    total = 0.0
    for i in range(5):
        tempList = [k for k in range(n)]
        done = []
        # swaps 10% of the values
        for j in range(n // 10):
            randomIndex1, randomIndex2 = random.sample(range(len(tempList)), 2)
            while randomIndex1 in done or randomIndex2 in done:
                randomIndex1, randomIndex2 = random.sample(range(len(tempList)), 2)
            done.append(randomIndex1)
            done.append(randomIndex2)
            temp = tempList[randomIndex1]
            tempList[randomIndex1] = tempList[randomIndex2]
            tempList[randomIndex2] = temp
        startTime = time.perf_counter()
        quickSort(tempList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        total += elapsedTime
    return total / 5


def main():
    # prints the random values
    print("Input type = Random")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    " + "%.6f  " % randomBubble(10), "%.6f  " % randomBubble(100),
          "%.6f" % randomBubble(1000))
    print("   insertionSort    " + "%.6f  " % randomInsertion(10), "%.6f  " % randomInsertion(100),
          "%.6f" % randomInsertion(1000))
    print("       mergeSort    " + "%.6f  " % randomMerge(10), "%.6f  " % randomMerge(100), "%.6f" % randomMerge(1000))
    print("       quickSort    " + "%.6f  " % randomQuick(10), "%.6f  " % randomQuick(100), "%.6f" % randomQuick(1000))
    print()
    print()
    # prints the sorted values
    print("Input type = Sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    " + "%.6f  " % sortedBubble(10), "%.6f  " % sortedBubble(100),
          "%.6f" % sortedBubble(1000))
    print("   insertionSort    " + "%.6f  " % sortedInsertion(10), "%.6f  " % sortedInsertion(100),
          "%.6f" % sortedInsertion(1000))
    print("       mergeSort    " + "%.6f  " % sortedMerge(10), "%.6f  " % sortedMerge(100), "%.6f" % sortedMerge(1000))
    print("       quickSort    " + "%.6f  " % sortedQuick(10), "%.6f  " % sortedQuick(100), "%.6f" % sortedQuick(1000))
    print()
    print()
    # prints the reversed values
    print("Input type = Reverse")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    " + "%.6f  " % reverseBubble(10), "%.6f  " % reverseBubble(100),
          "%.6f" % reverseBubble(1000))
    print("   insertionSort    " + "%.6f  " % reverseInsertion(10), "%.6f  " % reverseInsertion(100),
          "%.6f" % reverseInsertion(1000))
    print("       mergeSort    " + "%.6f  " % reverseMerge(10), "%.6f  " % reverseMerge(100),
          "%.6f" % reverseMerge(1000))
    print("       quickSort    " + "%.6f  " % reverseQuick(10), "%.6f  " % reverseQuick(100),
          "%.6f" % reverseQuick(1000))
    print()
    print()
    # prints the almost sorted values
    print("Input type = Almost sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    " + "%.6f  " % almostBubble(10), "%.6f  " % almostBubble(100),
          "%.6f" % almostBubble(1000))
    print("   insertionSort    " + "%.6f  " % almostInsertion(10), "%.6f  " % almostInsertion(100),
          "%.6f" % almostInsertion(1000))
    print("       mergeSort    " + "%.6f  " % almostMerge(10), "%.6f  " % almostMerge(100),
          "%.6f" % almostMerge(1000))
    print("       quickSort    " + "%.6f  " % almostQuick(10), "%.6f  " % almostQuick(100),
          "%.6f" % almostQuick(1000))


main()
