############DEBUGGING#####################

# Describe Problem
# i never reaches 20, range needs to be updated
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
# list start from [0], randint need to be updated
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
# 1994 is not caught, elif update
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors
# indent, data type, f-string
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

#Print is Your Friend
# double equal in word_per_page
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
# indent
# https://pythontutor.com/render.html#mode=display 
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])