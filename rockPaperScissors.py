import random 


#set variable keepPLaying to true 
keepPlaying = True 
#while keepPlaying is true:
while(keepPlaying == True ): 
    #print statement welcoming players to the game
    print ("Welcome players")
    #print statement stating the rules (best 2 out of 3 press 'q' to quit)
    print("Best 2 out of 3")
    print("press 'q' to quit")
    #make a key that assigns a number to each choice for the computer
    #(rock is 1, scissors is 2, paper is 3)
    
    #import random function 
    
    #set computer's score to 0
    #set player's score to 0
    player = 0
    computer = 0
    
    #while player's score is less than 2 and the computer's score is less than 2: 
    while (player < 2 and computer <2):
        
    #computer's choice = random number between 1 and 3 
        computerChoice = random.randint (1,3)
    #player's choice = input (ask player to select rock, paper, or scissors)
    playerChoice = input ("please choose (rock, paper, or scissors):")
    playerChoice = playerChoice.lower()
    #if player inputs 'q' or 'Q':
    if(playerChoice == "q"): 
    #set keepPlaying to False
        keepPlaying = False 
    #stop the loop
        break 
    #else if (player inputs rock and computer chooses rock) or
    elif ((playerChoice == "rock" and computerChoice == "rock") or (playerChoice == "paper" and computerChoice == "paper") or
          (playerChoice == "scissors" and computerChoice == "scisssors")):
        print("DRAW")
        print("player score =" + player._str_() + "computer score = " + computer._str_())
    
    #else if (player inputs rock and computer inputs scissors) or 
    elif((playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "scissors" and computerChoice == "paper") or 
         (playerChoice == "paper" and computerChoice == "rock")):
    #add one to player's score
        player = player + 1 
        print("round win")
        print("player score =" + player._str_() + "computer score = " + computer._str_())
        
    #else if (player inputs rock and computer inputs paper) or 
    elif((playerChoice == "rock" and computerChoice == "paper") or (playerChoice == "scissors" and computerChoice == "rock") or 
         (playerChoice == "paper" and computerChoice == "scissors")): 
    #add one to compute's score 
        computer = computer + 1 
        
        print("player score =" + player._str_() + "computer score = " + computer._str_())
else: 
    print("your input is not valid")
    print("thank you for playing")
    if(player ==2): 
        print("the computer won")
        print("player score =" + player._str_() + "computer score = " + computer._str_())
        
