class Node:
    def __init__(self, data, end):
        self.children = []
        self.data = data
        self.end = end

class Trie:

    def __init__(self):

        self.root = Node("*", False)
        self.words = []

    def get_words(self):

        self.words.clear()
        for child in self.root.children:

            self.get_words_helper(child, "")

        return self.words

    def get_words_helper(self, node, prefix):

        new_prefix = prefix + node.data
        if node.end and new_prefix not in self.words:

            self.words.append(new_prefix)

        for child in node.children:

            self.get_words_helper(child, new_prefix)


    def add_word(self, word):

        if self.search(word):

            return False

        node = self.root
        chars = list(word)

        for i in range(len(chars)):

            target_char = chars[i]
            found = False

            for child in node.children:

                if child.data == target_char:
                    node = child

                    found = True
                    if i == len(chars) - 1:

                        node.end = True

            if not found:

                end = False

                if i == len(chars) - 1:

                    end = True

                new_node = Node(target_char, end)
                node.children.append(new_node)
                node = new_node
            
        return True
    
    def search(self, word):

        node = self.root
        chars = list(word)

        for i in range(len(chars)):

            found = False
            target_char = chars[i]

            for child in node.children:

                if child.data == target_char:

                    found = True
                    node = child

            if not found:

                return False
        if node.end:

            return True

        return False
    
    def autocomplete(self, prefix):
        words = self.get_words()
        result = []

        for word in words:

            chars = list(word)

            if len(word) >= len(prefix):
                sub = ""

                for i in range(len(prefix)):

                    sub += chars[i]

                if sub == prefix:

                    result.append(word)

        return result

    def delete(self, to_delete):

        words = self.get_words()
        self.root.children.clear()

        for word in words:

            if word not in to_delete:
                
                self.add_word(word)