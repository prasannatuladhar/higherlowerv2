from pydoc import describe
from art import logo,vs
from gamedata import data
import random
import os

''' pick a random data from API'''
def pick_person():
  return random.choice(data)


''' Format a text to show user '''
def format_person(data):
  name = data['name']
  description = data['description']
  country = data['country']
  return f"{name} , {description} from {country}"

''' compare result between two pick'''
def compare(first,second):
  user_reply=input("Who has more followers? Type 'A' or 'B':").lower()
  if user_reply=='a' and first>second :
    return 1
  elif user_reply=='b' and first<second:
    return 1
  elif user_reply=='a' and first<second :
    return 0
  else:
    return 0
 
def game():
  print(logo)
  total_score=0
  endofgame = False
  data_of_first_person = pick_person()
  data_of_second_person = pick_person()
  while not endofgame:
    data_of_first_person = data_of_second_person
    data_of_second_person = pick_person()
    
    if data_of_first_person==data_of_second_person:
      data_of_second_person=pick_person()

    first_value=data_of_first_person['follower_count']
    # print(first_value)
    second_value=data_of_second_person['follower_count']
    # print(second_value)
    
    print(f"Compare A:{format_person(data_of_first_person)}")
    print(vs)
    print(f"Against B: {format_person(data_of_second_person)}")
    score = compare(first=first_value,second=second_value)
    if score==1:
      total_score += score
      os.system("cls") 
      print(f"You're right! Current score: {total_score}.")

      
    else:
      os.system("cls") 
      print(f"Sorry that's wrong. Final Score :{total_score}")
      endofgame = True

game()