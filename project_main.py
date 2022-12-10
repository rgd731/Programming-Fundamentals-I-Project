from importlib import reload
import all_questions
import random
import time
import os


def clear():
  '''Function that clears text on the console'''
  if os.name == 'posix':
    os.system('clear')
  else:
    os.system('cls')


def slow_type(string, delay=0.01):
  '''Function prints string one character at a time'''
  for char in string:
    print(char, end="", flush=True)
    time.sleep(delay)
  print("")


def slow_type_no_newline(string, delay=0.01):
  '''Function prints string one character at a time, modified to not print a new line'''
  for char in string:
    print(char, end="", flush=True)
    time.sleep(delay)


def ask_question(difficulty):
  '''Function asks question to player; takes in string "easy","medium", or "hard" as argument'''
  global points
  global questions_asked
  questions_asked += 1
  print("Question", questions_asked)
  #following code randomly chooses a question from a dictionary from module "all_questions.py"
  question = random.choice(list(all_questions.questions[difficulty].items()))
  slow_type(question[0])
  answer = input().strip()
  print("")
  #following code awards points based on difficulty of question
  if answer.lower() in question[1]:
    slow_type("That's correct!")
    if difficulty == "easy":
      points += 1
    elif difficulty == "medium":
      points += 2
    elif difficulty == "hard":
      points += 3
  else:
    slow_type("Sorry, that's incorrect.")
  #deletes question from dictionary to avoid being randomly chosen again
  del all_questions.questions[difficulty][question[0]]
  time.sleep(3)
  #following code only runs on the last question
  if questions_asked == 9:
    slow_type("That's the end of this quiz!")
    time.sleep(5)
    clear()
    return
  slow_type_no_newline("Your current score is ")
  print(points, end=" ")
  if points == 1:
    slow_type("Point")
  else:
    slow_type("Points")
  time.sleep(1)
  slow_type("Next question!\n")
  time.sleep(1)


def introduction():
  '''Function that introduces the player to the rules; can be skipped to avoid experienced players from being forced to go through the rules everytime'''
  slow_type("Welcome to RDG's Programming Fundamentals I Review Game!")
  slow_type("--------------------------------------------------------", 0.005)
  print("")
  slow_type(
    "This game was created as a way to review some of\nthe concepts learned in Programming Fundamentals I."
  )
  slow_type("Not to mention it's for a grade too!\n")
  slow_type("Type 'start' to begin")
  slow_type("Type 'quit' to exit")
  slow_type("Type 'skip' to just get to the questions!")
  while True:
    start = input().lower().strip()
    if start not in ["start", "quit", "q", "s", "skip"]:
      slow_type("Not a valid response")
      continue
    if start in ["quit", "q"]:
      slow_type("\nMaybe some other time!")
      quit()
    elif start == "skip":
      clear()
      return
    else:
      slow_type("\nAwesome! Let's start with some of the rules.")
      time.sleep(2)
      break
  clear()
  slow_type("The rules are fairly simple:\n")
  slow_type(
    "You will be asked 9 questions total,\n3 easy, medium, and difficult ones.\n"
  )
  slow_type(
    "The more difficult the question,\nthe more points you get per question.\n"
  )
  time.sleep(2)
  slow_type("Type 'ready' whenever you're ready to begin.")
  while True:
    start = input().lower().strip()
    if start not in ["ready", "r", "rdy"]:
      slow_type("Not a valid response")
      continue
    else:
      slow_type("\nLet's begin!")
      break
  time.sleep(2.5)
  clear()


introduction()

high_score = 0
while True:
  questions_asked = 0
  points = 0
  ask_question("easy")
  ask_question("easy")
  ask_question("easy")
  slow_type("These questions are a little harder, but there are\nworth 2 points instead of 1. Good luck!")
  time.sleep(5)
  clear()
  ask_question("medium")
  ask_question("medium")
  ask_question("medium")
  slow_type("These are the hardest questions now. They're pretty tricky\nbut if you get them right, they're are worth 3 points!")
  time.sleep(5)
  clear()
  ask_question("hard")
  ask_question("hard")
  ask_question("hard")
  #Text based on how well the player did
  if points == 18:
    slow_type("You're absolutely amazing! You managed to get a pefect score!")
  elif points >= 12:
    slow_type(
      "You did an awesome job! You are well versed in the basics of Python")
  else:
    slow_type("You're definitely getting there! Some more practice and you'll absolutely be able to nail down the basics of Python!")
  print("")
  #following code displays final score and displays and updates high score if needed
  slow_type_no_newline("Your final score was ")
  print(points, end=" ")
  if points == 1:
    slow_type("Point")
  else:
    slow_type("Points")
  if points > high_score:
    slow_type("That's a new high score that you set!")
  if high_score > 0:
    slow_type_no_newline("The previous high score you set was ")
    print(high_score, end=" ")
  if high_score == 1:
    slow_type("Point")
  else:
    slow_type("Points")
  high_score = points
  #Player can choose to play again
  slow_type("Would you like to play again? yes/no")
  while True:
    continue_to_play = input().lower().strip()
    if continue_to_play not in [
        "no", "n", "esc", "escape", "quit", "bye", "goodbye", "stop", "q",
        "yes", "y", "yeah", "yea", "sure", "ok"]:
      slow_type("Not a valid response")
      continue
    if continue_to_play in ["yes", "y", "yeah", "yea", "sure", "ok"]:
      slow_type("Sounds great! Good luck!")
      time.sleep(4)
      reload(all_questions)
      clear()
      break
    else:
      slow_type("That's alright. See you next time!")
      quit()
