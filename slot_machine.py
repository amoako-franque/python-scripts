
import random
def spin_row ():
  symbols= ["🍒", "🍉","🍋", "🔔" ,"⭐️"]

  return [ random.choice(symbols) for symbol in range(3)]

  # results=[]

  # for symbol in range(3):
  #   symbol = random.choice(symbols)
  #   results.append(symbol)
  # return results

def print_row(row):
  print("***************")
  print(" | ".join(row))
  print("***************")


def get_payout(row, bet):
  if row[0] == row[1] == row[2]:
    if row[0] == "🍒":
      return bet * 4
    elif row[0] == "🍉":
      return bet * 7
    elif row[0] == "🍋":
      return bet * 10
    elif row[0] == "🔔":
      return bet * 20
    elif row[0] == "⭐️":
      return bet * 50

  return 0

def main():
  balance = 120

  print("*******************")
  print("Welcome to Python Slots ")
  print("Symbols 🍒 🍉 🍋 🔔 ⭐️")
  print("*******************")


  while balance > 0:
    print(f"Your balance is ${balance:.2f}")
    print("*****************************")
    bet = input("Place your bet amount: ")

    if not bet.isdigit():
      print("Invalid bet amount. Enter a valid positive number")
      continue

    bet = int(bet)

    if bet > balance:
      print(f"Insufficient funds. Your balance is ${balance:.2f}")
      continue

    if bet <= 0:
      print("Invalid bet amount. Must be greater than 0")
      continue

    balance -= bet


    print("*****************************")
    row = spin_row()

    print("SPinning ...\n")
    print_row(row)

    payout = get_payout(row, bet)

    if payout > 0:
      print(f"You won ${payout:.2f}")
    else:
      print("Sorry, you lost")

    balance += payout


    play_again = input("Do you want spin more? (Y/N): ").upper()

    if play_again != "Y":
      break

  print("*****************************")
  print(f"Your final balance is ${balance:.2f}. Have a nice day!")
  print("******************************")

if __name__ == "__main__":
  main()