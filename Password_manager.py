def add():
    Account_name = input("Enter the account name: ")
    Password = input("Enter ther respective password : ")
    with open("password.txt","a") as f:
        f.write(Account_name + "|" + Password + '\n')

def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name , pasw = data.split("|")
            print(f"User: {name} , Password: {pasw}")

print("Welcome to password storing and view Manager")
while True:
    user = input("You want to add or view your passwords (add/view) or 'q' to Quit : ").lower().strip()
    if user == 'q':
        print("Thank you for visiting")
        break
    elif user == 'add':
        add()
    elif user == 'view':
        view()
    else:
        print("PLease choose right option")