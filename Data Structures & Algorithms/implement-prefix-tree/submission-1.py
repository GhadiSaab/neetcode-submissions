class PrefixTree:

    def __init__(self):
        # will contain the nodes
        self.trie = {}
        

    def insert(self, word: str) -> None:
        d = self.trie

        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]

        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie
        
        for char in word: 
            if char not in d :
                return False
            d = d[char]

        if '.' in d:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        
        for char in prefix: 
            if char not in d :
                return False
            d = d[char]

        return True

        