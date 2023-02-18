class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26
        self.is_end_word = False
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t) -> int:
        return ord(t) - ord('a')

    def insert(self, key):
        if not key:
            return False

        key = key.lower()
        current = self.root

        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")

            current = current.children[index]

        current.is_end_word = True
        print("'" + key + "' inserted")

    def search(self, key):
        return False

    def delete(self, key):
        pass


keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

t = Trie()
print("Keys to insert:\n", keys)

for words in keys:
    t.insert(words)
