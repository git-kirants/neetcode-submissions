class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()      

    def addWord(self, word: str) -> None:
        cur = self.root # start at root
        for ch in word: # for every letter in word
            if ch not in cur.children: # if char not found in current children
                cur.children[ch] = Node() # create new node for char
            cur = cur.children[ch] # if already present switch to it
        cur.end = True # mark the work end

    def search(self, word: str) -> bool:
        def dfs(i, node):

            # BASE CASE
            # If we have processed all characters in 'word'
            # Example: searching "bad"
            # When i == 3 (len("bad")), we check if current node marks end of a word
            if i == len(word):  
                # Return True only if this node was marked as end=True during addWord
                return node.end  

            ch = word[i]

            # --------------------------------------------------
            # CASE 1: Normal character (not a dot)
            # --------------------------------------------------
            # Example:
            # Trie contains: "bad", "dad", "mad"
            # Searching: "bad"
            #
            # i = 0 → ch = 'b'
            # If 'b' not in root.children → return False
            # If exists → move to that child node
            if ch != ".":

                # If character not present in current node's children
                # Example: searching "pad"
                # 'p' not in root.children → immediately False
                if ch not in node.children:
                    return False

                # If present:
                # Move to next character (i + 1)
                # and move to corresponding child node
                # Example flow for "bad":
                # dfs(0, root)
                # → dfs(1, node_for_'b')
                # → dfs(2, node_for_'a')
                # → dfs(3, node_for_'d')
                return dfs(i + 1, node.children[ch])

            # --------------------------------------------------
            # CASE 2: Wildcard '.'
            # --------------------------------------------------
            # '.' can match ANY character at this position
            #
            # Example:
            # Trie contains: "bad", "dad", "mad"
            # Searching: ".ad"
            #
            # i = 0, ch = '.'
            # node.children = {'b', 'd', 'm'}
            #
            # We must try ALL possible branches

            for child in node.children.values():

                # Try matching rest of word from this child
                # Example:
                # Try 'b' → check "ad"
                # Try 'd' → check "ad"
                # Try 'm' → check "ad"
                if dfs(i + 1, child):
                    # If ANY branch returns True,
                    # we stop early (short-circuit)
                    return True

            # If loop finishes:
            # That means NONE of the branches worked
            # Example: searching ".at"
            # Try 'b' → fails
            # Try 'd' → fails
            # Try 'm' → fails
            # Therefore return False
            return False

        # Start DFS from index 0 at root
        return dfs(0, self.root)