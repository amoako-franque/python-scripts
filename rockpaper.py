import random

options=("rock","scissors","paper")
running = True

while running:
  player=None
  computer = random.choice(options)
  while player not in options:
    player = input("Enter your selected choice (rock, scissors, paper): ").lower()

  print(f"Player: {player}")
  print(f"Computer: {computer}")

  if player == computer:
    print("Tie")
  elif player == "rock" and computer == "scissors":
      print("Player wins")
  elif player == "scissors" and computer == "paper":
      print("Player wins")
  elif player == "paper" and computer == "rock":
      print("Player wins")
  else:
      print("Computer wins")

  play_again = input("Play again? (y/n): ").lower()
  # if play_again != "y":
  #   running = False
  # if not play_again == "y":
  #   running = False

print("Thanks for playing")  # This will be printed after the loop ends