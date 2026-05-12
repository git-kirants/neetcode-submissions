class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()      

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.end = True
    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.end

            ch = word[i]

            # Normal character
            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(i + 1, node.children[ch])

            # Wildcard case
            for child in node.children.values():
                if dfs(i + 1, child):
                    return True
            return False

        return dfs(0, self.root)