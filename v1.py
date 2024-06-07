# Ask the user their name
name=input("what's your name?")
# greet the user and introduce the quiz
print ("Welcome to the quiz", name)
try:
  tries = input("How many attempts do you want at each question? 1-10")
  tries = int(tries)
except:
  print("That's not a number")
# ask the user a question
guess=input("what is the capital of France?")
if guess == "Paris":
  print("Correct!")
elif guess == "":
  print("Not sure?")
else:
  print("wrong!")
 
# tell the user the answer
print ("The answer is Paris")
# ask the user a question
guess=input("what is the capital state of the united states?")
if guess == "Washington D.C.":
  print("Correct!")
elif guess == "":
  print("Not sure?")
else:
  print("wrong!")

# tell the user the answer
print ("The answer is Washington D.C.")
input ("hello")
# end the quiz