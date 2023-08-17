Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=open("poem.txt","r")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=open("poem.txt","r")
FileNotFoundError: [Errno 2] No such file or directory: 'poem.txt'
>>> a=open("F:\poem.txt","r")
>>> a.read()
"        WHY?\n\nWe work,we thry to be better\nwe work with full zest\nBut why is that we just don't know any letter.\n\nwe still gave our best.\nBut why is that we still don't get a meal.\n\nwe don't get luxry,\nwe don't get childhood,\nbut we still work,\nnot for us but for all the others,\n\nwhy s that some kids wear shoes,BUT we make them ?\n\nby Mythili, class 5"
>>> a.read(100)
''
>>> a=open("F:\poem.txt","r")
>>> 
SyntaxError: multiple statements found while compiling a single statement
>>> a=open("F:\poem.txt","r")
>>> a.read(100)
"        WHY?\n\nWe work,we thry to be better\nwe work with full zest\nBut why is that we just don't know"
>>> obj1=open("F:\poemBTH.txt","r")
>>> s1=obj1.readline()
>>> s2.readline(10)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s2.readline(10)
NameError: name 's2' is not defined
>>> 
