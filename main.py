# commit main.py Jacob Heller (c) 2023
# the following is the independent work and sole intellectual property of Jacob Heller
# this work is not to be copied or reprodouced without explicit consent from its author

import os
import time
from colorama import Fore
from variables import variables
from errors import inlineCommentError

global COMMANDS

FILENAME = "index.flo"

def delist(void):
  void = str(void)
  void = void.replace('"', '')
  void = void.replace("'", "")
  void = void.replace("[", "")
  void = void.replace("]", "")
  void = void.replace(",", "")
  return void

def stdout(args):
  if '"' == str(args)[-3]:
    if '"' == str(args)[2]:
      text = delist(args)
      print(text)
    else:
      stdoutError(delist(str(args)))
  else:
    stdoutError(delist(str(args)))

def puts(args):
  if '"' == str(args)[-3]:
    if '"' == str(args)[2]:
      text = delist(args)
      print(text, end='')
  else:
    putsError(delist(str(args)), lines)

def _op_add_(args):
  print(args)

def _op_sub_(args):
  print(args)

COMMANDS = {
  "STDOUT": stdout,
  "PUTS": puts,
}

OPERATIONS = {
  "OP_ADD": _op_add_,
  "OP_SUB": _op_sub_,
}

def parse(code):
  with code as f:
    lines = 1
    for line in f.readlines():
      line = line.strip()
      cmd = line.split(' ')[0]
      args = line.split(' ')[1:]
      
      # ignore comments
      if cmd[0] == "/" and cmd[1] == "/":
        inlineCommentError(cmd, lines)
        
      elif cmd in COMMANDS:
        result = COMMANDS[cmd](args)
        args_str = ', '.join(args)
        lines += 1
        
      else:
        if lines != 1:
          print()
        print(Fore.RED + f'Syntax error, line {lines}\n{cmd} is not recognized as an internal command.')
        lines += 1
  f = open("variables.py", "w")
  f.write("variables = {}")
  f.close()
  empty = open(FILENAME, "r")
  code = str(empty.read())
  empty.close()
  if code == "":
    print(Fore.RED + f"Interpreter void: {FILENAME}\nNo code to execute")

with open(f"{FILENAME}") as f:
  lines = 1
  for line in f.readlines():
    line = line.strip()
    cmd = line.split(' ')[0]
    args = line.split(' ')[1:]
    
    # ignore comments
    if cmd[0] == "/" and cmd[1] == "/":
      pass
      
    elif cmd in COMMANDS:
      result = COMMANDS[cmd](args)
      args_str = ', '.join(args)
      lines += 1
      
    else:
      if lines != 1:
        print()
      print(Fore.RED + f'Syntax error, line {lines}\n{cmd} is not recognized as an internal command.')
      lines += 1
f = open("variables.py", "w")
f.write("variables = {}")
f.close()
empty = open(FILENAME, "r")
code = str(empty.read())
empty.close()
if code == "":
  print(Fore.RED + f"Interpreter void: {FILENAME}\nNo code to execute")
