import random
import statistics as st
from llHashSet import MyHashSet
from llHashSet import ListNode
import pandas as pd
import os
import tracemalloc
import time
from bstHashSet import BSTHashSet
from bstHashSet import TreeNode
from bstHashSet import Bucket
from bstHashSet import BSTree
from nums import nums_list
import array as arr
#test the number of collisions at each index in the hashmap
#test the runtime and memory of each test for different sizes


evenLLHashSet = MyHashSet(1000)
primeLLHashSet = MyHashSet(997)

evenBSTHashSet = BSTHashSet(1000)
primeBSTHashSet = BSTHashSet(997)

controlHashSet = set()
controlArray = arr.array('i')


testSizes = [1,10,100,500,1000,5000,10000, 12000, 20000]
execution_list = []


evenList = []
primeList = []
#test the even hashSet for collisions

stack = []

for _ in range(100):
    a = MyHashSet(1000)
    b = MyHashSet(997)
    for j in range(12000):
        randInt = random.randint(1,2147483647)
        a.add(randInt)
        b.add(randInt)
    evenList.append(a.index_distribution())
    primeList.append(b.index_distribution())
 
evenFrame = pd.DataFrame(evenList)
primeFrame = pd.DataFrame(primeList)

with pd.ExcelWriter(r'Visualize Code\HashSet Visualization\Hash_Set Execution Logs.xlsx', mode="a", engine="openpyxl",if_sheet_exists='overlay') as writer:
        evenFrame.transpose().to_excel(writer, sheet_name="Even2", header=None, index=False, startrow=0) 
        primeFrame.transpose().to_excel(writer, sheet_name="Prime2", header=None, index=False, startrow=0)

"""
#TESTING ADD FUNCTION
for testSize in testSizes:
    evenLLHashSet = MyHashSet(1000)
    primeLLHashSet = MyHashSet(997)

    evenBSTHashSet = BSTHashSet(1000)
    primeBSTHashSet = BSTHashSet(997)

    controlHashSet = set()
    controlArray = arr.array('i')

    #evenLLHASHSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        evenLLHashSet.add(nums_list[i])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["evenLLHashSet", "Add", testSize, (endTime-startTime), memUsage, ])


    #primeLLHASHSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for j in range(testSize):
        primeLLHashSet.add(nums_list[j])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["primeLLHashSet", "Add", testSize, (endTime-startTime), memUsage])

    #primeBSTHASHSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for k in range(testSize):
        primeBSTHashSet.add(nums_list[k])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["primeBSTHashSet", "Add", testSize, (endTime-startTime), memUsage])

    #evenBSTHASHSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for l in range(testSize):
        evenBSTHashSet.add(nums_list[l])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["evenBSTHashSet", "Add", testSize, (endTime-startTime), memUsage])

    #control HashSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for l in range(testSize):
        controlHashSet.add(nums_list[l])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["ControlHashSet", "Add", testSize, (endTime-startTime), memUsage])

    #control Array TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for l in range(testSize):
        controlArray.append(nums_list[l])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["ControlArray", "Add", testSize, (endTime-startTime), memUsage])




#TESTING REMOVE FUNCTION=================================================================================================

    #evenLLHASHSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        evenLLHashSet.remove(nums_list[i])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["evenLLHashSet", "remove", testSize, (endTime-startTime), memUsage])


    #primeLLHASHSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for j in range(testSize):
        primeLLHashSet.remove(nums_list[j])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["primeLLHashSet", "remove", testSize, (endTime-startTime), memUsage])

    #primeBSTHASHSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for k in range(testSize):
        primeBSTHashSet.remove(nums_list[k])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["primeBSTHashSet", "remove", testSize, (endTime-startTime), memUsage])

    #evenBSTHASHSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for l in range(testSize):
        evenBSTHashSet.remove(nums_list[l])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["evenBSTHashSet", "remove", testSize, (endTime-startTime), memUsage])

    #control HashSet TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for m in range(testSize):
        controlHashSet.remove(nums_list[m])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["ControlHashSet", "remove", testSize, (endTime-startTime), memUsage])

    #control Array TEST
    startTime = time.time_ns()
    tracemalloc.start()
    for n in range(testSize):
        controlArray.remove(nums_list[n])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    execution_list.append(["ControlArray", "remove", testSize, (endTime-startTime), memUsage])

    



addFrame = pd.DataFrame(execution_list)
with pd.ExcelWriter(r'Visualize Code\HashSet Visualization\Hash_Set Execution Logs.xlsx', mode="a", engine="openpyxl",if_sheet_exists='overlay') as writer:
        addFrame.to_excel(writer, sheet_name="Execution Logs2", header=None, index=False, startrow=0) 


"""

