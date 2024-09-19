class Node:
    def __init__(self):
        self.son = dict()
        self.isword = False

class Trie:
    def __init__(self):
        self.root = Node()

    # 添加 word
    def insert(self, word: str) -> None:
        cur = self.root
        for x in word:
            if x not in cur.son:
                cur.son[x] = Node()
            cur = cur.son[x]
        cur.isword = True

    # 查找是否存在 word
    def search(self, word: str) -> bool:
        cur = self.root
        for x in word:
            if x not in cur.son:
                return False
            cur = cur.son[x]
        return cur.isword

    # 检测 prefix 是否为已插入单词的前缀
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for x in prefix:
            if x not in cur.son:
                return False
            cur = cur.son[x]
        return True