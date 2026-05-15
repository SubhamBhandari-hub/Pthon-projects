def add_password():
    website = input("enter name of web: ")
    username = input("enter username: ")
    password = input("enter password: ")
    
    with open("pass.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")
    print("password saved successfully")


def view_password():
    with open("pass.txt", "r") as file:
        content = file.read()
        if content:
            print(content)
        else:
            print("No passwords saved yet.")


while True:
    print("\n--- PASSWORD MANAGER ---")
    print("1. ADD PASSWORD")
    print("2. VIEW PASSWORD")
    print("3. EXIT")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_password()
    elif choice == "2":
        view_password()
    elif choice == "3":
        print("Good bye")
        break
    else:
        print("Wrong entry")