import random

global points
points = 0
global user_input
user_input = ''

while not user_input.startswith('q'):
  result = 'Draw'
  user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
  if (user_input 
      not in ['rock', 'paper', 'scissors'] 
      and not user_input.startswith("q")
    ):
    print("Invalid Input")
    break
  computer_input = ("rock", "paper", "scissors")[random.randint(0, 2)]

  match (user_input, computer_input):
    case "rock", "paper":
      result = "You lose"
      points -= 1
    case "paper", "scissors":
      result = "You lose"
      points -= 1
    case "scissors", "rock":
      result = "You lose"
      points -= 1
    case "paper", "rock":
      result = "You Win"
      points += 1
    case "scissors", "paper":
      result = "You Win"
      points += 1
    case "rock", "scissors":
      result = "You Win"
      points += 1
  print(f"You: {user_input.capitalize()}, Computer: {computer_input.capitalize()}\nResult: {result}\nYour Total Points: {points}")

# R - P
# P - S
# S - R
# P - R
# R - S
# S - P
