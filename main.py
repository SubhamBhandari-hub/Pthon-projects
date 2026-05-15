def add_password():
    website = input("Enter name of website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")

    print("Password saved successfully")


while True:
    print("\n--- PASSWORD MANAGER ---")
    print("1. ADD PASSWORD")
    print("2. VIEW PASSWORD")
    print("3. EXIT")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        with open("passwords.txt", "r") as file:
            data = file.read()
            print(data)

    elif choice == "3":
        print("Good bye")
        break

    else:
        print("Wrong entry")