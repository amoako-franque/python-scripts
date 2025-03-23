# CONCESSION STAND

menu ={
  "soda": 1.99,
  "chips": 3.99,
  "popcorn": 4.99,
  "water": 2.99,
  "beer": 5.99,
  "wine": 6.99,
  "brandy": 7.99,
  "whisky": 8.99
}

cart=[]
total=0

print("------- Menu List -------")
for key, value in menu.items():
  print(f"{key:8}: ${value:.2f}")

print("------- End! -------")
num = 8
while True:
  item = input("select an item (q to quit): ").lower()
  if item == "q":
    break
  elif menu.get(item) is not None:
    cart.append(item)


print("--------- Your Order -------")
for item in cart:
  # total += menu[item]
  total += menu.get(item)
  print(item, end=", ")

print(f"Total is: ${total:.2f}")
