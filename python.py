Section: 1

Welcome to the Python Programming Course! Thank you for joining me
1. Welcome to this Python Course! What you need to know before starting.

Section: 2

Setting Up Python On Your Computer
2. Get Started by Installing Python 3.5
3. Setting up Sublime Text to Build Python


Section: 3
Introduction to your first program with Python, data types and variables
4. First Program in Python

>>> print('welcome')
welcome
>>> print 'welcome'
  File "<stdin>", line 1
    print 'welcome'
                  ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('welcome')?

5. Data Types

>>> type(2)
<class 'int'>
>>> type(2.2)
<class 'float'>
>>> type(200000000)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type('a')
<class 'str'>

6. Variables

>>> number = 2
>>> real = 2.2
>>> word = "word"
>>> print(word)
word
>>> a=b=c=1.5
>>> print(a)
1.5
>>> print(b)
1.5
>>> print(c)
1.5
>>> 
>>> one, two, three = 1, 'two', 3.0
>>> print(one)
1
>>> print(two)
two
>>> print(three)
3.0

>>> number =1
>>> str = 'string'
>>> number = str
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


7. Indentation

def test():
    statement1
    statement2
    statement3
    statement4

def test2():
    statement1
    statement2
    statement3
    statement4

8. How to Clear Screen

import os
clear = lambda: os.system('cls')
clear()

print()


Section: 4

Comments in Python
9. Single-line Comments

# single line comment

10. Multi-line Comments

''' 
multiple 
lines 
comments

'''


Section: 5

Expressions in Python
11. Basic Arithmetic
12. Division Characteristics
13. Operator Precedence
14. Complex Arithmetic
15. Binary Number Manipulation

2+2
50 - 5*6
(50 - 5*6) / 4
8 / 5   	# division always returns a floating point number
17/3    	# classic division returns a float
17//3   	# floor division discards the fractional part
17 % 3  	# the % operator returns the remainder of the division
5 * 3 + 2
5 ** 2  	# 5 squared
2 ** 7	     	# 2 to the power of 7

width = 20
height = 5 * 9
width * height


4 * 3.75 - 1

tax = 12.5 / 100
price = 100.50
price * tax

price + _
round(_, 2)


Section: 6

Learn about Strings
16. Basic String Manipulation


'spam eggs'  		# single quotes

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
'Py' 'thon'

text = ('Put several strings within parentheses '
        'to have them joined together.')
text

prefix = 'Py'
prefix + 'thon'

word = 'Python'
word[0]   # character in position 0
word[5]   # character in position 5
word[-1]  # last character
word[-2]  # second-last character
word[-6]

word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)

word[:2] + word[2:]
word[:4] + word[4:]

word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

s = 'supercalifragilisticexpialidocious'
len(s)

17. Using the format Method

print('Today I had {0} cups of {1}'.format(3, "coffee"))
Today I had 3 cups of coffee
print('price :({x},{y},{z})'.format(x = 2.0, y = 1.5, z = 5))
price :(2.0,1.5,5)
print('The {vehicle} had {0} crashes in {1} months'.format(5,6, vehicle = 'car'))
The car had 5 crashes in 6 months
print('{:<20}'.format("text"))
text
print('{:>20}'.format("text"))
                text
print('{:b}'.format(21))
10101
print('{:x}'.format("21"))
15
print('{:o}'.format("21"))
25

18. Specific Characters

'doesn\'t'   		# use \' to escape the single quote...
"doesn't"    		# ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

'"Isn\'t," they said.'
s = 'First line.\nSecond line.'  # \n means newline
s  				 # without print(), \n is included in the output
print(s)  			 # with print(), \n produces a new line
print('C:\some\name')    	 # here \n means newline!
print(r'C:\some\name')  	 # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


Section: 7

Branching in Python
19. Logical Operators and Conditional Statements
<, >, <=, >=, !=, ==

print(5 < 6)
print(15 > 6)
print(5 == 6)
print(5 <= 6)
print(5 >= 6)
print(5 == 6)

not and or

a=True
b=False
print(a and b)
print(not b)
print(a and b)


20. if Statement

word = "abc"
if word == 'abc' or word == 'hi':
    print('hello gaurav')

if condition_statement:
    #code
    #print
    pass
if True:
    print('hii')

21. if else Statement

word = "abc"
if word == 'abc' or word == 'hi':
    print('hello gaurav')
else:
    print('hey')

if 5 < 7:
    if 5 > 6:
        print("5 > 6")
else:
    print('5 <= 6')

22. ifelif Statement

if name =='gaurav':
    print('hi gaurav')
elif name =='rahul':
    print('hi rahul')
else:
    print('not name')


num = 3
if( num > 1 and num < 5):
    print(num)
else(num > 2 and num < 4):
    print(num+1)
else:
    print(num-1)


23. Ternary Operator

word = ""
me = 'Hi' if word == 'Hello' or word == 'Hi' else 'Hey'
print(me)

a=3
a=7 if 3**2 > 9 else 14
print(a)


Section: 8

Loops in Python
24. for Loop Part 1

range(start, stop, step)

for i in range(0, 10): # for(int i, i < 10, i++)
    print(1)

for i in range(0, 10, 2): 
    print(1)
25. for Loop Part 2

string = "string traversal!"
for i in range(len(string)):
    print(string[i])

for i in range(3):
    for j in range(2):
        print(j)
26. for Loop Part 3

for i in range(1,11):
    print('{:<3}|'.format(i), end="")
    
    for j in range(1,11):
        print('{:>4}'.format(i * j), end="")

    if i == 1:
        print('\n{:#^44}'.format(""), end="")
    print ""

27. while Loop

condition = 10
while condition !=0:
    print(condition)
	condition = condition - 1

while True:
    print("infinite")
    break

for i in range(1,11):
    i ==5:
        continue
    print(i)
28. break and continue Statements

Section: 9

Functions in Python
29. Defining and Calling Functions and Returning Values

def parameter():
   return "hello" 

result = parameter()
print(result)

def mulival():
    return "this is a result,", 2
print(multival())

30. Passing Arguments, Default Parameters, Scope and Nested Functions

def parameters(a):
    print(a)
parameters("this is a parameter")

def add(a,b):
    c =a + b
    return c
result = add(12,5)
print(result)

def defalt_param(a, b=4, c=5):
    return a+b+c
result = defalt_param(3)
print(result)

def scope(a):
    a=a+1
    print(a)
    return a
scope(5)

def outer(a):
    def nested(b):
        return b+a
    a= nested(a)
    return a
print(outer(4))

def f(a):
    def g(b):
        return a*b
    return g
print(f(5)(2))


def f(a):
    def g(b):
        def h(c):
            return a*b*c
        return h
    return g
print(f(5)(2)(3))

31. Recursive Functions

def factorial(n):
   if n==1:
       return 1
   else:
       return n+factorial(n-1)
print(factorial(5))

def sum(n):
   if n==1:
       return 1
   else:
       return n+sum(n-1)
def tail_sum(n, accumulator = 0):
    if n == 0:
        return accumulator
    else:
        return tail_sum(n-1, accumulator+n)
print(sum(10))
print(tail_sum(10))


print(factorial(5))

32. Lambda Functions

f =lambda x, y:x+y
print(f(2,3))

f = lambda a: lambda b: lambda c: a*b*c
print(f(5)(3)(2))

f = lambda c: lambda a: b:lambda d:(c * (a + b)) % d
print(f(2)(4,3)(11))

Section: 10

Exception Handling
33. Exceptions and Errors

print(5/0)
file = open("file", "r")
int('1.2')

34. Handling Exceptions

try:
    a=5/0
except Exception as e:
    print(e)



try:
    n = int(input('Enter an Integer: '))
except ValueError:
    print('That is not an integer')

try:
    sum=0
    file = open('numbere,txt','r')
    for number in file
        sum = sum + 1.0/int(number)
    print(sum)
except ZeroDivisionError:
    print("Number in file equal to zero!")
except IOError
    print(''file DNE)
finally:
    print(sum)
    file.close()


35. Throwing Exceptions

a='a'

def RaiseException(a):
    if type(a) !=type('a'):
        reise Value('This is not string')

try:
   RaiseException(a)
except ValueError as e:
   print(e)


def TestCase(a, b)
    assert a<b, "a is greater than b"

try:
   TestCase(2,1)
except AssertionError as e:
   print(e)


Section: 11

Data Input
36. Data Input Setup and Input Function
age = input('how old are you:')
print(age)


37. File Management: Reading

file = open('file.txt', 'r')
print(file.read())
file.close()



file = open('file.txt', 'r')
print(file.read(5))
print(file.tell())
file.seek()

file.close()

38. File Management: Writing

file = open('write.txt','w+')
file.write('hello file. I am string!')
file.seek(0)
file.write('this')
print(file.read())
file.close()














