## 0x05. Python - Exceptions

**What you should learn from this project**

       At the end of this project you are expected
       to be able to explain to anyone, without the help of Google:

* Why Python programming is awesome (don’t forget to tweet today,
  with the hashtag #pythoniscool :))
* What are exceptions and how to use them
* When do we need to use exceptions
* How to handle correctly an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

**Exercises**

**0. Safe list printing**

     Write a function that prints x elements of a list.

* Prototype: def safe_print_list(my_list=[], x=0):
* my_list can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed
  by a new line.
* x represents the number of elements to print
* x can be bigger than the length of my_list
* Returns the real number of elements printed
* You have to use try: / except:
* You are not allowed to import any module
* You are not allowed to use len()