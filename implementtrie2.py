class Trie:
    class TrieNode:
        def __init__(self):
            self.node = [None] * 26
            self.flag = False
            self.count = 0
            self.precount = 0

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        tmp = self.root
        for char in word:
            index = ord(char) - ord('a')
            if tmp.node[index] is None:
                next_node = self.TrieNode()
                tmp.node[index] = next_node
                tmp = next_node
            else:
                tmp = tmp.node[index]
            tmp.precount += 1
        tmp.flag = True
        tmp.count += 1

    def countWordsEqualTo(self, word):
        tmp = self.root
        for char in word:
            index = ord(char) - ord('a')
            if tmp.node[index] is None:
                tmp = None
                break
            else:
                tmp = tmp.node[index]
        if tmp is None:
            return 0
        return tmp.count

    def countWordsStartingWith(self, word):
        tmp = self.root
        for char in word:
            index = ord(char) - ord('a')
            if tmp.node[index] is None:
                tmp = None
                break
            else:
                tmp = tmp.node[index]
        if tmp is None:
            return 0
        return tmp.precount

    def erase(self, word):
        tmp = self.root
        for char in word:
            index = ord(char) - ord('a')
            if tmp.node[index] is None:
                tmp = None
                break
            else:
                tmp = tmp.node[index]
            tmp.precount -= 1
        if tmp is not None and tmp.flag:
            tmp.flag = False
            tmp.count -= 1
