#Language Fundamentals Lecture 01

'''
• Python is very easy to learn.
• Founder of python was "Guido Van Rossam" in 1991.
• Python name came from the famous comedy Tv show named Monty's Python Circus.
• Python is a General Purpous High Level Programming Language.

## Features Of Python ##
1. Simple & Easy to learn.
2. High Level Language.
3. Freeware & Open source.
4. Platform Independent (PVM - Python Virtual Machine).
5. Dynamically Typed. (Means we need not need to declare the type of the variable)
6. Procedure Oriented & Object oriented as well scripting language.
7. Interpreted    


• Functional Programming Feature Took from - C Language.
• OOPS Feature took from - C++ Language.
• Scripting Language took from - Perl & Shell Script.
• Modular Programming feature took from - Muodula 3
• Almost most of the features of python take from - C & ABC Language.

## In which Area we can use python? ##
• Desktop Application.
• Web Application.
• DataBase Application.
• Machine Learning.
• Data Science.
• Data Analytics.
• IOT & Many more


## Limitations Of Python ##
1. Performance Issue.


## Variable / Identifier ##
Variable is the name of the memory which stores some data.

## Rules for defining a variable ##
1. Variable name cannot start with a digit.
2. Cannot use Python keywords like if,for,class
3. Can contain letters,numbers or underscore after the first character.
4. Python is Case Sensitive.
Ex : Abc, ABC,ABc,AbC,abc,Cba All are different variables

## Keywords / Reserved Words ##
• Keywords are the fixed words that have special meaning to the compiler.
• There are 35 keywords are there in python

'''

# a=10
# pi=3.14
# IsFollowed =True
# name="Akash"
# print(type(a))
# print(type(pi))
# print(type(IsFollowed))
# print(type(name)) 



## Output ##
''' 
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
'''

## Program Statement to view the Keywords ##
# import keyword
# print(keyword.kwlist)

## Keywords Output ##
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

#Data Types in Python 

#Fundamental Data Types
'''
1. int
2. float
3. string(str)
4. bool
5. complex
'''

#Number System
'''
1. Decimal
2. Binary
3. Octal
4. HexaDecimal
'''

#If we write 0B or 0b in any number the compiler convert it to a binary value
'''
a=0b1000
print(a) 8 will be the output
'''
#for octal use 0o or 0O
'''
b=0o1000
print(b) 512 will be the output
'''
#for decimal 0x or 0X
'''
c=1000
print(c) 1000 will be the output
'''

## Exponential in Python ##
'''
We can give exponential in either small e or capital E

e or E means 10 in Decimal
a=1.2e4
print(a) Output : 12000.0

'''

#Complex Data Type
'''
• Ex Of Complex no 2+3i (i was there in 12)
• But in python i was replaced by j
• Here 2 is the real part & 3i was the imaginary part

a=3+4j
print(type(a)) Output : <class 'complex'>


Example :
a=3+4j
b=2+5j
c=a+b
print(c) #Output : 5+9j
d=a-b
print(d) #Output : 1-1j
e=a*b
print(e) #Output : (-14+23j)

#Multiplication of complex numbers
(3+4j)(2+5j)
6+15j+8j+20j^2  #Here j^2 means -1
6-20+23j
-14+23j

How to check the real & imaginary part of complex numbers?
print(a.real) #Output : 3.0
print(a.imag) #Output : 4.0
'''

#bool Data Type
'''
• bool means True or False 
• True & False are the keywords
• Internaly True means 1 and False means 0

10<20 True or False --> True

a=10<20
print(a) #Output : True  

a=True+True  #Output : 2
b=False+True #Output : 1
'''

#string Data Type
name="Akash"
print(name[0]) #Output : A
print(name[1]) #Output : K
print(name[2]) #Output : A
print(name[3]) #Output : S
print(name[4]) #Output : H