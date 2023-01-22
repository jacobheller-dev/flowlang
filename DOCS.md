# Flowlang Docs
### Installation
First, ensure that you have [Python 3.0](https://www.python.org/) or later installed on your machine. This is necessary for Flow to run as the language is based in
Python. Next, install Flow as a ZIP file from GitHub with your preferred installation method.  
  
Flow will run in native python if you `[CTRL] + [F]` in FLOW.py and remove every instance of `colorama` and `Fore` from the file.  
However, this is not optimal as error messages will appear in the same color as plain code. This can be fixed by running `pip install colorama` in your terminal
and insuring that you have the Fore module installed from colorama.  
  
You can write Flowlang code by creating a text file ending in .flo on your machine. This file must be in the same folder as your Flow installation. Next, change the
`FILENAME = main.flo` variable at the top of your FLOW.py file to whatever you named yours. Your code will be interpreted and executed as FLOW.py is run in the terminal.
### Documentation
[Syntax](docs/syntax.md)
