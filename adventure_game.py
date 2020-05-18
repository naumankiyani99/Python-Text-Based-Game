import time
import random

def print_pause(response):
	print(response)
	time.sleep(2)

def intro(item, option):
    print_pause("Hello Adventuer"
                "Welcome to the lands of beyond the sea\n")
    print_pause("you must make the right decision if you want to surive in this strange land "
                "be perpared to make some hard choices.\n")
    print_pause("You Get into your friend`s car and head to the rumored Haunted House of the Town\n")
    print_pause("There you find a fornt yard overgrown with weed and bushes\n")
    print_pause("you make your way to the House."
                "There you saw a locked door and a window\n")


def door(item,option):
	if "key" in item:
		print_pause("you look around carefully for a key"
			"you have already found it so its no use \n")
		print_pause("you walk to the door of the house")
	else:
		print_pause("you look around carefully for a key"
			"you see a flower pot to the left of the door")
		print_pause("you look under it and find the key")
		print_pause("you walk back to the door")
		item.append("key")
		frontyard(item,option)

def house(item,option):
	if "key" in item:
		print_pause(" you open the door of the house.")
	
	while True:
		decision2 = input("would you like to go in(1) or stay out and run?(2)")
		if decision2 == "1":
			if "key" in item:
				print_pause("you enter and see a" +option)
				print_pause("togather with your friend you are able to dely"+ option + "its approch,")
				print_pause("and run away with your lives")
				print_pause("You Win!")
			else:
				print_pause("you stay out of the house and" +option+ "ambushes you from behind")
				print_pause("you get knocked out and eaten by the" +option)
				print_pause("You Lose")
			play_again()
			break
		if decision2 == "2":
			print_pause("you stay out and decided to run")
			print_pause("you and your friend dodge and run away with your lives")
			
			frontyard(item,option)
			play_again()
			break
def frontyard(item, option):
    print_pause("Enter 1 to unlock the door of the house.")
    print_pause("Enter 2 to look under the flower pot")
    print_pause("What would you like to do?")
    while True:
        decision1 = input("(Please enter 1 or 2.)\n")
        if decision1 == "1":
            house(item, option)
            break
        elif decision1 == "2":
            door(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()

def play_game():
    item = []
    option = random.choice(["Djinn", "Werewolf", "Dragon", "Vampier",
                            "Knoblod"])
    intro(item, option)
    frontyard(item, option)


play_game()				

		

