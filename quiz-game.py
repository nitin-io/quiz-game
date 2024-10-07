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

global points
points = 0

for question, answer in questions.items():
  user_answer = input(question + "\n")
  if user_answer.lower().replace(" ", "") == answer.lower().replace(" ", ""):
    points += 1
  else:
    points -= 1

print(points)