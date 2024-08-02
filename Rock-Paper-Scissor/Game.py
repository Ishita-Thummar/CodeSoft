import random

item_list = ["Rock","Paper","Scissor"]
user_choice = input("Enter your move = Rock , Paper , Scissor : ")
comp_choice = random.choice(item_list)

print("User choice : "+ user_choice + "  >>>  "+ "Computer choice : " + comp_choice)

if user_choice == comp_choice:
    print("Both chooses same: Match Tie")
elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock = Computer won !")
        else:
            print("Rock smashes Scissor = You won !")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper , Computer Won !")
    else:
        print("Paper covers Rock = You won !")
        
elif user_choice == "Scissor":
    if comp_choice == "Paper":
      print("Scissor cuts paper , You Won !")
    else:
      print("Rock smashes Scissor = Computer won !")



