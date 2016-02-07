# ********************* PROBLEM STATEMENT *********************
# A primary school teacher wants to test her students mental arithmetic by making
# them complete a test with 10 questions in which they complete operations like;
# adding, subracting and multiplying.
#
# Complete the following tasks;
# 1.   Design and create the algorithm for this new primary school arithmetic quiz
# 2.   Think of and implement a new feature to improve this task.
#
# the teacher also wants to store the student's marks on a text file
#
# 3.   Design and implement this feature into your algorithm.
#
# however, this teacher has two clases for mathematics and she wants to keep the
# class' score separate.
#
# 4.   improve task (3) so that there is more than oneset of class score.
#
#
# ********************* PSEUDOCODE *********************




# import a new function (Random)
import random

# Variables we are going to use
score=0
answer=0
operators=('+','-','x')
 # -------------------------------------------------------------

for i in range(1):
     num = random.randint(5,10)
     num1 = random.randint(1,5)

     # pick out the operator of choice

     operator = random.choice(operators)
     #  mark out the answer
     if operator == "+":
         answer = num + num1

     elif operator == "-":
         answer = num - num1

     elif operator == "x":
         answer = num * num1

# create the users input

print('What is '+str(num) + operator + str(num1))
user_answer= int(input('Enter The answer.'))
