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
                print("You have choices : \n1->climb Tres 'Energy reduce to 1'\n2->Run Back 'Energy Reduces to 1'\n3->stay still 'Energy Reduces to 0'")
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    print("You climb the tree and spot smoke far away")
                    energy -= 1
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
                print("You have choices : \n1->Check Bag 'Energy reduce to 0'\n2->Ignore it  'Energy Reduces to 0'\n3->Take a nap 'Energy gains bt 1'")
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

                    


        else:
            break
    

game()