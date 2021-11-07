# Base node class

class Node():

    def __init__(self):

        self.children = [None]*26
        self.isend = False

#Trie class
class Trie():

    def __init__(self):

        self.__root = Node()

    def __len__(self):
        """
        returns length of the trie

        Returns:
            [int]: [length of the trie]
        """        

        return len(self.search_by_prefix(''))

    def __str__(self):
        """
        returns all values in the trie

        Returns:
            [string]: [all values in the trie]
        """    

        ll = self.search_by_prefix('')
        string = ""

        for i in ll:

            string += i
            string += "\n"

        return string

    def chartoint(self, character):

        """
        returns the unicode value of a character

        Returns:
            [int]: [integer value of the character]
        """        

        return ord(character) - ord('a')

    def remove(self, string):
        """
        removes an item from the trie

        Args:
            string ([string]): [string to be removed]

        Raises:
            ValueError: [handles if the keyword does not exist in the trie]
            ValueError: [handles if the keyword does not exist in the trie]
        """        
        ptr = self.__root
        length = len(string)
        exists = True

        for idx in range(length):

            i = self.chartoint(string[idx])

            if ptr.children[i] is not None:

                ptr = ptr.children[i]

            else:

                exists = False

        if ptr.isend is not True:

            exists = False

        if exists == False:

            print("Keyword does not exist in trie")

        ptr.isend = False

        return

    def insert(self, string):
        """
        inserts a string into the trie

        Args:
            string ([string]): [string to be inserted into the trie]
        """        
        ptr = self.__root
        length = len(string)

        for idx in range(length):

            i = self.chartoint(string[idx])

            if ptr.children[i] is not None:

                ptr = ptr.children[i]

            else:

                ptr.children[i] = Node()
                ptr = ptr.children[i]

        ptr.isend = True

    def search(self, string):
        """
        searches for a string inside the trie

        Args:
            string ([string]): [string to search for]

        Returns:
            [bool]: [if the string is found in the trie or not]
        """        
        ptr = self.__root
        length = len(string)

        for idx in range(length):

            i = self.chartoint(string[idx])

            if ptr.children[i] is not None:

                ptr = ptr.children[i]

            else:

                return False

        if ptr.isend is not True:

            return False

        return True

    def __getall(self, ptr, key, key_list):
        """
        gets all values given arguments

        Args:
            ptr ([type])
            key ([type])
            key_list ([list])
        """        
        if ptr is None:

            key_list.append(key)

            return

        if ptr.isend is True:

            key_list.append(key)

        for i in range(26):

            if ptr.children[i] is not None:

                self.__getall(ptr.children[i], key +
                              chr(ord('a') + i), key_list)

    def search_by_prefix(self, key):
        """
        gets all strings starting with a prefix

        Args:
            key ([string]): [key to search by]

        Returns:
            [list]: [list with all strings starting with key]
        """        
        ptr = self.__root
        key_list = []
        length = len(key)

        for idx in range(length):

            i = self.chartoint(key[idx])

            if ptr.children[i] is not None:

                ptr = ptr.children[i]

            else:

                return None

        self.__getall(ptr, key, key_list)

        return key_list

