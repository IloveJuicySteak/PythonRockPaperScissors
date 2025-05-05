import random 

Options = ("Rock", "Paper", "Scissors")
running = True 
while running:

  Player = none 

  computer = random.choice(Options)
  
  while Player not in opitons: 
  Player = inout("Enter a choice (Rock, Paper, Scissors): "
  
  print(f"Player: {Player}")
  print(f"Computer: {computer}")
  
  if Player == computer:
                 print ("It's a tie!")
  elif Player == "Rock" and computer == "Scissors":
                 print ("You win!")
  elif Player == "Paper" and computer == "Rock":
                 print ("You win!")
  elif Player == "Scissors" and computer == "Paper":
                 print ("You win!")
  else:
    print ("You Lose!")

  if not input("Play again> (y/n): ").lower == "y":
    running = False
    
print ("Thanks for playing!")
