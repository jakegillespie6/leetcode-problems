from Trie import TrieNode
from Trie import Trie
import time
import statistics as st
import pandas as pd
import random
import os
import tracemalloc
from Trie_inputs import word_list
from Trie_inputs import partialsList
from Trie_inputs import prefixesList

def startsWith(prefix, wordlist):
    for sub in wordlist:
        if sub.startswith(prefix):
            return True
    return False

def searchPartial(part, wordlist):
    for word in wordlist:
        searchword = part.lstrip(".")
        if searchword in word:
            return True
    return False


def searchKnownWordInList(word):
    if word in word_list:
        return True
    return False

myTrie = Trie()
myBlankList = []

testSizes = [1,10,50,100,500,1000,2000,5000,10000,15000,25000,50000,90000]
trieList = []
listList = []

myTrie = Trie()
myBlankList = []

#TESTING THE DURATION OF ADD WORD
print("starting addWord")
for testSize in testSizes:
    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        myTrie.addWord(word_list[i]) 
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    trieList.append(["Trie", "addWord", testSize, (endTime-startTime), memUsage])

    
    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        myBlankList.append(word_list[i])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    endTime = time.time_ns()
    listList.append(["List", "addWord", testSize, (endTime-startTime),memUsage])
print("finish addWord")


#TESTING THE DURATION OF SEARCH FULL WORD
print("starting search Known Word")
for testSize in testSizes:
    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        myTrie.searchKnownWord(word_list[i])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()   
    endTime = time.time_ns()
    trieList.append(["Trie", "SearchKnownWord", testSize, (endTime-startTime),memUsage])

    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        searchKnownWordInList(word_list[i])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop() 
    endTime = time.time_ns()
    listList.append(["List", "SearchKnownWord", testSize, (endTime-startTime),memUsage])
print("finish Search Known Word")

print("starting starts with")
for testSize in testSizes:
    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        myTrie.startsWith(word_list[i])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()   
    endTime = time.time_ns()
    trieList.append(["Trie", "starts with", testSize, (endTime-startTime),memUsage])


    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        startsWith(prefixesList[i], word_list)
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()   
    endTime = time.time_ns()
    listList.append(["List", "starts with", testSize, (endTime-startTime),memUsage])
print("finsih sttart with")

print("starting partial serach")
for testSize in testSizes:
    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        myTrie.search(word_list[i])
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()  
    endTime = time.time_ns()
    trieList.append(["Trie", "Search partial word", testSize, (endTime-startTime),memUsage])


    
    startTime = time.time_ns()
    tracemalloc.start()
    for i in range(testSize):
        searchPartial(partialsList[i], word_list)
    memUsage = tracemalloc.get_traced_memory()
    tracemalloc.stop()   
    endTime = time.time_ns()
    listList.append(["List", "Search partial word", testSize, (endTime-startTime),memUsage])
print("fin partial serach")



listFrame = pd.DataFrame(listList)
trieFrame = pd.DataFrame(trieList)
print(listFrame)
print(trieFrame)

with pd.ExcelWriter(r'C:\Users\jgillespie\OneDrive - Crown Castle USA Inc\Desktop\leetcode\Visualize Code\Trie Visualization\Trie Execution Logs.xlsx', mode="a", engine="openpyxl",if_sheet_exists='overlay') as writer:
        listFrame.to_excel(writer, sheet_name="Sheet1", header=None, index=False, startrow=1) 
        trieFrame.to_excel(writer, sheet_name="Sheet2", header=None, index=False, startrow=1)







