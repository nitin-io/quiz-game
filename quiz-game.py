print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower().startswith("y") or playing.lower().startswith("o"):
  print("Great! Let's get started.")
else:
  print("No Problem, Later sometime.")
  quit()

questions = {
  "What does CPU stands for?": "central processing unit",
  "What does RAM stands for?": "random access memory",
  "What does GPU stands for?": "graphics processing unit",
  "What does PSU stands for?": "power supply unit"
}

clean_string = lambda str: str.lower().replace(" ", "")

global points
points = 0

for question, answer in questions.items():

  user_answer = clean_string(input(question + "\n"))
  if user_answer == clean_string(answer):
    points += 1
  else:
    points -= 0.5

if points > round(len(questions) / 2):
  print(f"Great! you got {points} points, which is {round(points / len(questions) * 100, 2)} percent. ;)")
else:
  print(f"Oops! you got {points} points, which is {round(points / len(questions) * 100, 2)} percent, Prepare well next time ;)")