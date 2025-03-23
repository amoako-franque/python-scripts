principle = 0
rate=0
time=0

while True:
  principle = float(input("Enter the principle amount: "))
  if principle < 0:
    print("The principle amount must be greater than 0")
  else:
    break
while True:
  rate = int(input("Enter the rate: "))
  if rate < 0:
    print("The rate must be greater than 0")
  else:
    break

while True:
  time = int(input("Enter the time: "))
  if time <=0:
    print("The time must be greater than 0")
  else:
    break
simple_interest = principle *pow((1 + rate  / 100),time)
print(f"The simple interest is: ${simple_interest:.2f}")