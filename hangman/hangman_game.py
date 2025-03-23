# hangman
from words import animal_names
import random


hangman_art={
  0: (
    "    ",
    "    ",
    "    ",
    ),
  1: (
    " o ",
    "   ",
    "   ",
    ),
  2: (
    " o ",
    " | ",
    "   ",
    ),
  3: (
    " o ",
    "/| ",
    "    ",
    ),
  4: (
    " o ",
    "/|\\",
    "      ",
    ),
  5: (
    " o ",
    "/|\\",
    "/    ",
    ),
  6: (
    " o ",
    "/|\\",
    "/ \\",
    ),
}

def display_man(wrong_guesses):
  print("**********************")
  for line in hangman_art[wrong_guesses]:
    print(line)
  print("**********************")
def display_hint(hint):
  print(" ".join(hint))
  print("**********************")


def display_answer(answer):
  print(" ".join(answer))
  print("**********************")


def main():
  answer =  random.choice(animal_names)
  print(answer)
  hint = ["_"] * len(answer)
  wrong_guesses = 0
  guessed_letters = set()
  is_running = True

  while is_running:
    display_man(wrong_guesses)
    display_hint(hint)
    # display_answer(answer)
    guess = input("guess a letter: ").lower()

    if len(guess) !=1 or not guess.isalpha():
      print("**********************")
      print("Invalid input")
      print("**********************")

      continue

    if guess in guessed_letters:
      print("**********************")
      print("Already guessed")
      print("**********************")
      continue

    guessed_letters.add(guess)

    if guess in answer:
      for i in range(len(answer)):
        if answer[i] == guess:
          hint[i] = guess
    else:
      wrong_guesses += 1
    if "_" not in hint:
      display_man(wrong_guesses)
      display_answer(answer)
      print("You Win!🥳")
      is_running = False
    elif wrong_guesses >= len(hangman_art):
      display_man(wrong_guesses)
      display_answer(answer)
      print("You Lose!😭")
      is_running = False

if __name__ == "__main__":
  main()
