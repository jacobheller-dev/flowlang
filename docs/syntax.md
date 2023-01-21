## Syntax
### Basic Syntax
Flowlang uses an all-caps syntax for operators, commands, functions, data structures, and methods. To use the `OP_MUL` operator with integer arguements as an arguement
for the `PUTS` command, you write `PUTS OP_MUL 1 1` using only capital letters for the command and the operator.  
  
Flowlang also uses different commands for various subclasses of operations. To print the string "Hello world!" to the screen, you use the standard output command
`STDOUT` with "Hello world!" as the arguement. `STDOUT "Hello world!"` However, to print the value of 2 + 2 to the screen, you use the `PUTS` command with the
`OP_ADD` command and its arguements as arguements. `PUTS OP_ADD 2 2`
### Operators
Operators are the most basic pieces of Flowlang. They control simple string and numerical operations, such as multiplication with the `OP_MUL` operator.
Operators are always written in all capital letters, and use the `OP_` idiom to declare that they are an operator. `OP_[CMD]`  
  
Operators have either numerical or string arguements, and these arguements are always adjacent with no joining characters. (eg: + | \ etc.) The syntax of an operator
declaration looks like this: `OP_[CMD] ARGS1 ARGS2 *` with * representing possible additional arguements.  
  
Operators can also be used as arguements for other elements, such as commands. The syntax for an arguementative operator looks like this:
`[MAIN] OP_[CMD] ARGS1 ARGS2 *` and changes rigidly rather than flexibly, preventing the use of further nested arguements.
### Commands
Commands are pieces of Flowlang code that reference machine behaviors, such as fetching a variable value or printing a string to the stream. Commands are
always written in all capital letters, and do not have a prefixal idiom. Commands are written simply as their name with specific arguement types following them.  
  
Commands always have adjacent arguements with no joining characters.The syntax of command declaration looks like this: `[COMMAND] ARGS1 *` with * representing
possible additional arguements. An operator can also be used as a command arguement, such as `OP_DIV` to divide numbers. Printing the product of 4 / 2 looks like
this: `PUTS OP_DIV 4 2` with the command and operator in all capitals and the arguements adjacent and not separated.  
  
Commands may return errors if their arguement types do not align with their intended use. For example, attempting to pass a string to the stream using `PUTS` rather
than `STDOUT` will return a type error. `PUTS "Hello world!"` returns `Was not expecting string object "Hello world!"` as an error. This is because `PUTS` is used
with operators, while running a standard output stream with `STDOUT` is the correct way to print a string to the screen.
### Variables
Variables have an inferred declaration syntax. If you attempt to pass a line of code with an unknown value and an equals sign, Flowlang will infer variable declaration
and store the arguements. For example, `x = "Hello variable!"` will store a value of "Hello variable!" in a memory location called "x" in RAM.  
  
Variables have rigid inferred types, meaning that you do *not* have to declare the type of a variable directly, but you *do* have to use specific syntax to declare
the type. To declare one variable equaling another, use the `x = y` syntax with x being the variable you are assigning and y being the existing variable.
To declare a string variable, use the `x = "Hello world!"` syntax with x being the variable you are assigning and `"Hello world!` being its value.
Finally, do declare an integer variable, use the `x = 7` syntax with x being the variable you are assigning and 7 being its value.  
  
Variables can be overridden in memory simply by redeclaring their values in the original manner, or with the RE command for code readability. To change the value
of a variable called "x" with a value of 7, simply run `x = 6` and x will equal six. You can also use rigid inference to infer variable type change. This means that
you can assign x, which now equals seven, a string value simply by running `x = "Hello world!"` which will reassign the variable.  
  
This syntax is very similar with the RE command, which takes a traditional variable assignment as its one arguement. Running `x = 5` will give us a variable with
a value of five. If we then run `RE x = "Hello world!"` then x's value will change to this specified string.  
  
You can fetch the value of a variable with the `GET` command, which takes variable names as arguements. This command works with all data types and will print the
value of a variable to the screen. For example, running `x = 2` followed by `GET x` will print 2 to the screen.
### Comments
You can initialize a 1-line code comment by starting a line with two forward slashes, followd by a space. ie: `// [COMMENT]`  
  
Any comments in your code will be completely ignored by the interpreter, including comments that include recognizable Flowlang code. For example, running
`// PUTS OP_ADD 3 3` will do nothing because it is being ignored as a comment.
