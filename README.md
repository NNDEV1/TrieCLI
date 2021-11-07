A library implementing the trie datastructure. The trie maintains a global state, meaning the state of the trie can be changed from anywhere. A list of commands are as follows:

    help:                        shows all commands available through the cli
    add_[words]:                 adds words or a word to the trie
    remove_[words]:              deletes words or a word from the trie
    search_[words]:              searches for the words or word in the trie and returns words found and not found
    visualize:                   displays all items currently in the trie
    searchbyprefix_[prefix]:     returns all items in the trie starting with the given prefix