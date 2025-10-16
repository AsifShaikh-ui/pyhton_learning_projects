import random
Directions = ["n","e","w","s"]

def game():
    energy = 10
    print("🌲 Welcome to 'Lost in the Woods'🌲")
    print("You wake up in the dark forest with no memmory of how you got here 👻")
    print("Find your 'way' to go 'out' before your 'energy' runs out!☠️\n")
    print(f"Your energy status: {energy}")
    print("You have directions: \nn->North\ns->South\ne->East\nw->West")
    print("Each Decision Cost -1 Energy")
    while True:
        user = input("Choose direction you want to move: ")
        if user not in Directions:
            print("Please choose correct direction")
        elif user == 'n':
            energy -= 1
            if energy >0:
                print("\nYou see tall trees and hear wolves howling🐺🐺")
                print("You have choices : \n1->climb Trees 'Energy reduce to 1'\n2->Run Back 'Energy Reduces to 1'\n3->stay still 'Energy Reduces to 0'")
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    print("You climb the tree and spot smoke far away - may be a camp a village🏡")
                    energy -= 1
                    print("\n You have choices : \n1->Go Toward Smoke 'Energy reduce to 1'\n2->Rest on branch Energy Reduces to 0'")
                    if energy > 0:
                        sub_choice = int(input("Enter your choice : "))
                        if(sub_choice == 1):
                            print("You follow the smoke and find an abandoned campfire🔥")
                            print("There is a narrow path leading out of the forest! YOu survived🌄")
                        elif sub_choice == 2:
                            print("You stay up there too long and loose balance , falling down")
                            print("From your falling voice the wolf🐺 occured and you died☠️")
                elif choice==2:
                    print("You rush back to the Starting point")
                    energy -= 1
                else:
                    print("A wolf passes by without noticing you")
            else:
                print("You run out of your energy")
                print("Game Over!☠️")
                break
        elif user == 'e':
            energy -= 1
            if energy > 0 :
                print("\nYou found an abandoned campfire and a bag of supplies.")
                print("You have choices : \n1->Check Bag 'Energy reduce to 0'\n2->Ignore it  'Energy Reduces to 0'\n3->Take a nap 'Energy gains by 1'")
                choice = int(input("Enter Your choice : "))
                if choice == 1:
                    print("You found food inside!😃 ~~~Energy gains by 2")
                    energy += 2
                elif choice==2:
                    print("You move on carefully")
                else:
                    energy +=1
                    print("You were attacked by insects!🕷️🦟🪰 ~~~Energy Reduces bt 2")
                    energy -= 2
            else:
                print("You run out of your energy")
                print("Game Over!☠️")
                break
        elif user == 's':
            energy -= 1
            if energy > 0 :
                print("\nThere’s a wide river with a broken bridge.")
                print("You have choices : \n1->Try crossing 'Energy reduce to 1'\n2->Search Around  'Energy Reduces to 0'\n3->Rest 'Energy gains by 1'")
                choice = int(input("Enter Your choice : "))
                if choice == 1:
                    energy -= 1
                    print("You slipped but managed to swim across ~~~Energy Reduces by 2")
                    energy -= 2
                elif choice==2:
                    print("You found a dry path leading Gate.~~~Energy gains by 1")
                    energy +=1
                else:
                    energy +=1
                    print("You rest by the water.~~~Energy gains by 1")

            else:
                print("You run out of your energy")
                print("Game Over!☠️")
                break
        elif user == 'w':
            energy -= 1
            if energy > 0 :
                print("\nYou found a dark cave with a faint glow inside.")
                print("You have choices : \n1->Enter Cave 'Energy reduce to 0'\n2->Shout  'Energy Reduces to 0'\n3->Walk Away 'Energy gains by 0'")
                choice = int(input("Enter Your choice : "))
                if choice == 1:
                    print("You found glowing mushrooms. ~~~Energy gains by 2")
                    energy += 2
                elif choice==2:
                    print("Your voice echoes — something growls back!~~~Energy Reduces by 2")
                    energy -= 2
                else:
                    energy +=1
                    print("You stay safe, but waste time.~~~Energy Reduces by 1")
                    energy -= 2
            else:
                print("You run out of your energy")
                print("Game Over!☠️")
                break

        else:
            break
    

game()