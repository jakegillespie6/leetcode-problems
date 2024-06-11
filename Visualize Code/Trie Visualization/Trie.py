class TrieNode:
    def __init__(self):
        self.children={}
        self.isCompleteWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr=curr.children[c]
        curr.isCompleteWord=True
        
    def search(self, word):
        #helper function to recursively search when encountering a .
        def dfs(word, curr):
            for i,c in enumerate(word):
                if c not in curr.children:
                    if c =='.':
                        for ch in curr.children:
                            if dfs(word[i+1:], curr.children[ch]):
                                return True
                    return False
                else:
                    curr=curr.children[c]
            return curr.isCompleteWord
        return dfs(word, self.root)
    
    def searchKnownWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isCompleteWord==True
    
    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True




    