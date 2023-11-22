class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):  # O(n^2) TS
        for i in range(len(string)):
            c = string[i]
            self.root[c] = self.root.get(c, {})
            node = self.root[c]
            
            for j in range(i + 1, len(string)):
                s = string[j]
                node[s] = node.get(s, {})
                node = node[s]

            node["*"] = True

    def contains(self, string):  # O(n) T | O(1) S
        node = self.root
        for c in string:
            if c not in node:
                return False
            node = node[c]

        if "*" in node:
            return True
        else:
            return False

