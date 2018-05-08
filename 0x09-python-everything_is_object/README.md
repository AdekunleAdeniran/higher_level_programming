## 0x09. Python - Everything is object

**What you should learn from this project**

       At the end of this project you are expected to be able to explain
       to anyone, without the help of Google:

* Why Python programming is awesome (don’t forget to tweet today, with the
  hashtag #pythoniscool :))
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address
  in the CPython implementation)
* What is mutable and immutable
* What are the builtin mutable types
* What are the builtin immutable types
* How does Python pass variables to functions

**0. Who I am?**

     What function would you use to print the type of an object? Write the
     name of the function in the file, without the ()

**1. Where are you?**

     How to get variable identifier (which is the memory address in the
     CPython implementation)? Write the name of the function in the file,
     without the ()

**2. Right count**

     In the following code, do a and b point to the same object?
     Answer with Yes or No.

     >>> a = 89
     >>> b = 100

**3. Right count =**

     In the following code, do a and b point to the same object?
     Answer with Yes or No.

     >>> a = 89
     >>> b = 89

**4. Right count =**

     In the following code, do a and b point to the same object?
     Answer with Yes or No.

     >>> a = 89
     >>> b = a

**5. Right count =+**

     In the following code, do a and b point to the same object?
     Answer with Yes or No.

     >>> a = 89
     >>> b = a + 1

**6. Is equal**

     What should those 3 lines print:

     >>> s1 = "Holberton"
     >>> s2 = s1
     >>> print(s1 == s2)

**7. Is the same**

     What should those 3 lines print:

     >>> s1 = "Holberton"
     >>> s2 = s1
     >>> print(s1 is s2)

**8. Is really equal**

     What should those 3 lines print:

     >>> s1 = "Holberton"
     >>> s2 = "Holberton"
     >>> print(s1 == s2)

**9. Is really the same**

     What should those 3 lines print:

     >>> s1 = "Holberton"
     >>> s2 = "Holberton"
     >>> print(s1 is s2)

**10. And with a list, is it equal**

      What should those 3 lines print:

      >>> l1 = [1, 2, 3]
      >>> l2 = [1, 2, 3]
      >>> print(l1 == l2)

**11. And with a list, is it the same**

      What should those 3 lines print:

      >>> l1 = [1, 2, 3]
      >>> l2 = [1, 2, 3]
      >>> print(l1 is l2)

**12. And with a list, is it really equal**

      What should those 3 lines print:

      >>> l1 = [1, 2, 3]
      >>> l2 = l1
      >>> print(l1 == l2)

**13. And with a list, is it really the same**

      What should print those 3 lines:

      >>> l1 = [1, 2, 3]
      >>> l2 = l1
      >>> print(l1 is l2)

**14. List append**

      What does this script print?

      l1 = [1, 2, 3]
      l2 = l1
      l1.append(4)
      print(l2)

**15. List add**

      What does this script print?

      l1 = [1, 2, 3]
      l2 = l1
      l1 = l1 + [4]
      print(l2)