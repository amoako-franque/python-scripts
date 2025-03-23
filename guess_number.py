import random

lowest_number=1
highest_number=100

number = random.randint(lowest_number, highest_number)
print(number)
guesses=0

is_running = True

print("------- Number Guessing Game -------")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running:
  guess = input("enter your guess: ")

  if guess.lower() == "q":
    print("Thanks for playing")
    is_running = False
    print(f"You guessed it in {guesses} guesses")

    break

  if guess.isdigit():
    guess = int(guess)
    guesses +=1
    if guess < lowest_number or guess > highest_number:
      print("That is out of acceptable range of numbers")
      print(f"Select a number between {lowest_number} and {highest_number}")
    elif guess < number:
      print("Too low. Try again")
    elif guess > number:
      print("Too high. Try again")
    else:
      print(f"You guessed right. Correct answer is {number}")
      print(f"You guessed it in {guesses} guesses")
      is_running = False
  else:
    print("Invalid guess")
    print(f"Select a number between {lowest_number} and {highest_number}")
