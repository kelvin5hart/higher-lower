import art
import game_data
import random
from replit import clear

# Print Logo
print (art.logo)

# Get the details into one list and the values of the scores into another list
details = []
followers = []
for entry in range(len(game_data.data)):
  importEntry = game_data.data[entry]
  details.append(f"{importEntry['name']} , a {importEntry['description']}, from {importEntry['country']}.")
  followers.append(importEntry['follower_count'])

# Function to generate a random number for B from the followers
def randomB (listOfEntries):
  return random.randint(0, len(followers) - 1)

# # Function to delete the use entry of A from the list to avoid generating a random number that will call it again
# def deleteA (listOfEntries, aInput):
#   return listOfEntries.remove(listOfEntries[aInput])

score = 0
A = randomB(followers)
B = randomB(followers)

while B == A:
  B = randomB(followers)

gameMode = 'yes'

while gameMode == 'yes':
  print(f"Compare A: {details[A]}")
  print(art.vs)
  print(f"Against B: {details[B]}")
  if B == len(followers):
    print(f"You have reached the end. Congratulations; Your score is {score}")
    gameMode = 'No'
  playerChoice = input("Who has more followers? Type 'A' or 'B': ").upper()
  if playerChoice == 'A':
    if followers[A] > followers[B]:
      score += 1
      # deleteA(details, A)
      # deleteA(followers, A)
      # if B != 0:
      #   A = B - 1
      # else:
      #   A = B 
      A = B
      B = randomB(followers)
      while B == A:
        B = randomB(followers)
      clear()
      print (art.logo)
      print(f"You were right. Your score is {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      gameMode = 'No'
  elif playerChoice == 'B':
    if followers[A] < followers[B]:
      score += 1
      # deleteA(details, A)
      # deleteA(followers, A)
      # if B != 0:
      #   A = B - 1
      # else:
      #   A = B
      A = B
      B = randomB(followers)
      while B == A:
        B = randomB(followers)
      clear()
      print (art.logo)
      print(f"You were right. Your score is {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      gameMode = 'No'