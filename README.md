# ProjectX

To run the skeleton code, open *three* command prompts in the repo directory and run these commands in order, one in each repo:

python Server.py  
python Receiver.py  
python Sender.py

There are several functions in each file that are "blocking" i.e. execution of whatever python file it is in pauses until the blocking function executes. I have commented each blocking function so we can better trace the flow of execution.
The important theme to keep in mind is that code execution in each file does not go all the way at once. In other words, just because Server.py is executed first does not mean that all the code in Server.py runs before Receiver.py

Additional documentation reference: https://docs.python.org/3/library/socket.html

### Tkinter - GUI library
#### Tools/Examples
* https://likegeeks.com/python-gui-examples-tkinter-tutorial/
* http://effbot.org/tkinterbook/tkinter-classes.htm

### Encryption/Decryption Techniques
* [Caesar Cipher](https://inventwithpython.com/chapter14.html)
