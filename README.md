# trie_project CLI
SLINGSHOT take home project submission


## Demo Video

***maybe?***

<!-- ABOUT THE PROJECT -->
## About The Project

Using the Trie data structure to create a usable command line interface with various commands such as add, remove, and search by prefix. I used figlet for a nice looking interface, I used flask and requests to implement the cli with the global state. Lastly I used PythonAnywhere to host the whole thing.

A list of commands are as follows:

    help:                        shows all commands available through the cli
    add_[words]:                 adds words or a word to the trie
    remove_[words]:              deletes words or a word from the trie
    search_[words]:              searches for the words or word in the trie and returns words found and not found
    visualize:                   displays all items currently in the trie
    searchbyprefix_[prefix]:     returns all items in the trie starting with the given prefix

Here are some resources I used to build this project:

* [Wikipedia Article for a Trie](https://en.wikipedia.org/wiki/Trie)
* [Medium Article on Understand Tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)
* [GeeksForGeeks Implementation(no code copied)](https://www.geeksforgeeks.org/trie-insert-and-search/)


### Built With

* [Flask](https://flask.palletsprojects.com/)
* [Requests](https://docs.python-requests.org/)
* [PyFiglet](http://www.figlet.org/)
* [PythonAnywhere](https://https://www.pythonanywhere.com/)


<!-- GETTING STARTED -->
## Getting Started

* *Clone git repository*
* *Make sure correct packages are installed(Prerequisites)*
* *Run server.py* using ```python server.py``` inside triecli

Example run:
![](https://user-images.githubusercontent.com/36611240/138568591-3eb0883a-a874-4dbb-b2b9-545c535b6578.png)
![](https://user-images.githubusercontent.com/36611240/138568606-1ba74026-76e1-4a46-a9d1-281714dee749.png)
![](https://user-images.githubusercontent.com/36611240/138568673-68af66f5-7539-4285-8e38-e7d6a631474a.png)

If you would like to run elsewhere change the link at line 49 in server.py and make sure you have the files: trie1.py, app.py, server.py


### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* flask
  ```pip install flask```
* pyfiglet
  ```pip install pyfiglet```
* requests
  ```pip install requests```
* Make sure you have python 3
<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.
<!-- CONTACT -->
## Contact
Nalin Nagar - nalinnagar1@gmail.com
