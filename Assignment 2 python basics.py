#!/usr/bin/env python
# coding: utf-8

Number 1 -

Question -
What are the two values of the Boolean data type? How do you write them?

Answer -
True and False, using capital T and F, with the rest of the word in lowercase

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
What are the three different types of Boolean operators?

Answer -
and, or, and not

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

Answer -
True and True is True.
True and False is False.
False and True is False.
False and False is False.
True or True is True.
True or False is True.
False or True is True.
False or False is False.
not True is False.
not False is True.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
What do the following expressions evaluate to?

(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
Answer -
False
False
True
False
False
True
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
What are the six comparison operators?

Answer -
The six different types of reference operators are : ==, !=, <, >, <=, and >=.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
What is the difference between the equal to operator and the assignment operator?

Answer -
== is the equal to operator that compares two values and evaluates to a Boolean, while = is the assignment operator that stores a value in a variable

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
Identify the three blocks in this code:

```
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

```

     
spam
- Answer - >The three blocks are everything inside the if statement
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 8 -

Question -
Explain what a condition is and where you would use one.

Answer -
A condition is an expression used in a flow control statement that evaluates to a Boolean value.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 9 -

Question -
Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

Answer -

spam = int(input("Enter a number : "))
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


     
Enter a number : 2
Howdy
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 10 -

Question -
What keys can you press if your program is stuck in an infinite loop?

Answer -
We need to press CTRL-C to stop a program if it has been stuck in an infinite loop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 11 -

Question -
What is the difference between break and continue?

Answer -
The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 12 -

Question -
What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

Answer -
They all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) explicitly tells the loop to start at 0, and range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iteration.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 13 -

Question -
Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

Answer -

for i in range(1, 11):
    print(i)


     
1
2
3
4
5
6
7
8
9
10

i = 1
while i <= 10:
    print(i)
    i = i + 1


     
1
2
3
4
5
6
7
8
9
10
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 14 -

Question -
If you had a bacon() function within a spam module, what would you call it after importing spam?

Answer -
This function can be called with spam.bacon().

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------