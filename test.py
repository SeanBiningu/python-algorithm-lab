#Question 1

# name={}
# number_student=int(input("enter the number of the students"))

# for i in range(number_student):
#     student_name=input("Please enter your name")
#     score=int(input('Please enter your score:'))
#     student_mark=int(input("please enter your Mark"))
 
#     avarage_mark=(student_mark+score)/2

#     name[student_name]=avarage_mark
# print(name)

# #   Question 2

# while True:
#     score=int(input("enter score"))
#     if 0 <= score <=100:
#         break
#     else:
#         print("invalid score!!! Please try again")

    


  #Question 3

import random 
guess=int(input("Please enter your number"))
number=random.choice(guess)
for i in range(3):
   while True:
      if guess < 100  and guess > 50:
         print("too high")
      elif guess <= 50 and guess >= 0:
        print("too low")


























