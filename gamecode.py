# here we start our code for game
import random # imports random module 
class character():
    def __init__(s,name):
        s.name = name
        s.__life = 3 #initially the lives would be three
        s.__score = 0
        s.__coins = 0

    def kick(s):
        s.__score = s.__score + 10 #"Kick" will increase score by 10

    def punch(s):
        s.__score = s.__score + 5 #"Punch" will increase score by 5

    def jump(s):
        s.__coins = s.__coins + 2 #"Jump" will gain two coins, which doesn't has any real use in game but acts like a currency element

    def stab(s):
        s.__life = s.__life - 1 # Stab method decreases lives by 1 whenever it is called

    def displaylife(s): # Displays current no of lives 
        return s.__life 

    def displayscore(s): # Displays current score 
        return s.__score

    def displaycoins(s): # Displays current no of coins
        return s.__coins

    def charinfo(s):
        return f"Name = {s.name} \nLife = {s.__life} \nScore = {s.__score} \nCoins = {s.__coins}"

def main():
    print("WELCOME".center(40,"-"))
    name = input(" Enter your Characters Name: ")
    obj = character(name) #assigns obj as input character name 
    n = 0  

    while(True)and(n==0): #we will make a main menu for game by using "While True" loop
        print("\n1. Start Game \n2. Display Life \n3. Display Score \n4. Display Coins \n5. Quit Game") #'\n' is used for getting every option in new line.
        i = input("Enter Your Selection: ")

        if(i=="1"):
            
            while(True):
                print("\nWelcome to Game\n")
                print("\nK = Kick \nP = Punch \nJ = Jump\n")
                c = input("Enter Your Selection: ").lower()
                value = random.randint(1,4) # chooses random value between 1 to 4 and when it is 3 character is stabbed and looses life by 1
                if (value==3):
                    obj.stab() # whenever value is equal to 3 calls "stab" method
                    v = obj.displaylife() # saves current no of lives in v
                    if(v==0): # checks if the no of lives is 0 yet for every loop
                        print(f"\nGame Over.... \n{obj.charinfo()}")
                        n = n+1 #n increments by 1 when lives become 0 
                        break # terminates the loop and ends game as lives become 0
                    else :
                        print(f"{obj.name} got stabbed. Life: {obj.displaylife()}") #else if lives are still remaining prints remaining lives 

        
                if(c=='k'):
                    obj.kick()
                    print(f"{obj.name} kicked. Score: {obj.displayscore()}")
                    
                elif(c=='p'):
                    obj.punch()
                    print(f"{obj.name} punched. Score: {obj.displayscore()}")
                    
                elif(c=='j'):
                    obj.jump()
                    print(f"{obj.name} jumped. Coins : {obj.displaycoins()}")
                    
                else:
                    print("Invalid Input") # if user input is anything other than K,P or J 
            
        elif(i=="2"):
            print(f"Lives remained for {obj.name}: {obj.displaylife()}")

        elif(i=="3"):
            print(f"Score by {obj.name}: {obj.displayscore()}")
        
        elif(i=="4"):
            print(f"Coins earned by {obj.name}: {obj.displaycoins()}")
        
        elif(i=="5"):
            e = input(f"Do You really want to Quit {obj.name}? Select(Y/N): ").lower() #if player wants to quit ask again for yes or no
            if(e=='y'):
                break # y input breaks while loop and game terminates
            else:
                continue # n input goes back to the beginning of loop and displays main menu
        else:
            print("invalid input, select again")
            

main()    #calls main function and displays main menu as we run the code      

