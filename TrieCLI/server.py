import requests
from pyfiglet import Figlet


f1 = Figlet(font='larry3d')
f2 = Figlet(font='big')
print(f1.renderText('Trie CLI'))

print("------------- github.com/NNDEV1/trie_project ------------")
print(f2.renderText("Enter 'help' for a list of usable commands"))


def displayCommands():
    print(f2.renderText("--- Commands ---"))
    print("help:                        shows all commands available through the cli")
    print("add_[words]:                 adds words or a word to the trie")
    print("remove_[words]:              deletes words or a word from the trie")
    print("search_[words]:              searches for the words or word in the trie and returns words found and not found")
    print("visualize:                   displays all items currently in the trie")
    print(
        "searchbyprefix_[prefix]:     returns all items in the trie starting with the given prefix")


def runner():

    input_text = input("-- ")

    if len(input_text) < 1:
        print("Please enter a valid command")
        runner()

    command_list = input_text.split(" ")

    if command_list[0] == "help":
        displayCommands()

    else:

        extension = ""
        for idx in range(len(command_list)):

            extension += command_list[idx]

            if idx < len(command_list) - 1:

                extension += "_"

        output = requests.get("http://nalinn.pythonanywhere.com/" + extension)
        print(output.text)

    runner()


runner()
