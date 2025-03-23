questions= (
  "1. How many elements are in the periodic table?: ",
   "2. Which animal lays the largest egg?: ",
   "3. What is the largest country in the world?: ",
   "4. How many bones are in the human body?: ",
   "5. What is the largest city in the world?: "
)

options=(
  ("A. 116", "B. 117","C. 118","D. 119"),
  ("A. Whale", "B. Crocodile","C. Elephant","D. Ostrich"),
  ("A. Ghana", "B. Nigeria","C. China","D. Russia"),
  ("A. 206", "B. 207","C. 208","D. 209"),
  ("A. Moscow", "B. Lagos","C. SOchi","D. Berlin"),
)


answers=("C","D","A","A","B")
guesses=[]
score=0
question_num=0


for question in questions:
  print()
  print(question)
  for option in options[question_num]:
    print(option)

  guess= input("Enter (A, B, C or D; q to quit: ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("CORRECT")
  else:
    print("INCORRECT")
    print(f"The answer is: {answers[question_num]} is the right answer")
  question_num+=1


print()

print("********************************")
print("*********** RESULTS ************")
print("********************************")

print(answers, end="")
for answer in answers:
  print(f"Answer: {answer} ")
print()

for guess in guesses:
  print(f"Guess: {guess} ", end="")
print()


score = int(score/len(questions) *  100)

print(f"your score is {score}%")