Core elements of a program
==========================

IDE
___
Integrated Development Environment (IDE and in pythons case it's IDLE). It includes a
1. Text editor, that help typing programs
2. Shell, an environment that interprets the text (added bonus highlighting)
3. Debugger

Objects
_______

Everything in Python is an object. Python code is an object. Each object has a **type**, that tells what kind of an object it is and what we can do with it.

There *type()* function to tell what type is the object (int, float, bool, etc.).

Two fundamental types
1. scalar - indivisable (atoms of a programming language)
2. non-scalar

For every type there is a literal.

Expression
__________

It is a sequence of operands (objects) and operators. In Python 2.x, *int* division provides a floor function and returns an int.

The operator **+** is overloaded. Overloaded operators have a meaning, that depends upon the type of the operands.

Type errors are a good thing. The language does type checking in order to reduce the probability of a programmers writing a program that will surprise its author.

Program
_______

Program = script. A program is a sequence of commands.

Variable. In Python it's a name for the object (a way to name the object). The assignment statement binds a name to an object, I.e. *x = 3*.

*raw_input()* always interprets the input as a string, *input()* interprets it as a Python program.

**Straight line programs**

It is a sequence of commands you execute one after the other, you execute all of them exactly once. It's like a recipe without tests (aka no taste if it's salty enough).

**Conditional statements allow for branching programs**

The statements:

1. if
2. elif
3. else

For comparisons we use **==** to test for equality. **%** is a mod operator. Indentation affects the meaning of a program.

Programs are intended to be read, not just executed, because the only way to debug a program is to read it. Thus people using indentation in languages that don't require it.

We can do a lot with branching programs. How long does it a straight line program to run? It relies on the number of commands issued, I.e. it has nothing to do with its input. A branching program takes *at most* the number of commands issued. Most programms should rely on the amount of data with regards to how long it will run.

Branching programs are not proportional to the amount of input.

**Looping construct - iteration**

These three enable the programming language to be Turing complete. This allows executing statements more than once.

Recitation
==========

So programming languages are themselves abstractions of binary code. This is done for the same reason as is the case with higher and higher level programming languages, I.e. they abstract more and more of data/instructions into higher level concepts.

Python
______

Interpreted language that is used in many places. Programs in Python are sequences of expressions composed of operands and operators.

```Python
mywar 	 =         'a string'
#operand #operator #operand
```
Everything is an object, that have types. There are different operations that can be done with different objects:

1. int (7, 0, -1, 2) - _+, -, *, /, **, %_
2. float (1.2, 0.0, -1.2) - _+, -, *, /, **_
    - int & float - _<, >, <=, >=, !=, ==_
3. string ('a string', "a string", "a string 'quoted'" - _+ (concatenation)_
4. bool (True, False) - _and, or, not_
    - and, or take two operands
    - not takes one
5. None (None) -
6. list
7. tuples
8. dictionaries

**If statements**

if <condition>:
	_execute_
elif <condition>:
	_execute_
else:
	_execute_

Flow control.

**Loops**

1. for loop - when you want to iterate over a finite set of elements
    - for i in range(1, 10):
	_execute_
2. while loop - executes as long as the condition is true
    - while <condition>:
	_execute_


