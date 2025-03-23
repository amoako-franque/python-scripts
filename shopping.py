# shopping cart

fruits=[]
prices=[]
total=0


while True:
  fruit = input("enter the fruit name (q  to quit): ")
  if fruit.lower() =="q":
    break
  else:
    price = float(input(f"Enter the price of {fruit}: $"))
    fruits.append(fruit)
    prices.append(price)

print("------ Your Cart Details ------")


for fruit in fruits:
  print(fruit)

for price in prices:
  print(f"${price:.2f}")

  # total += price

total = sum(prices)
print(f"Total: ${total:.2f}")











