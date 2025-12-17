import json
import os
import time
from admin import Admin
from user import User

def store_userdata(cnic, name_of_user):
    if name_of_user == "":
        print("Invalid Credentials !!!")
        time.sleep(2)
        return None, None
    if len(cnic) != 13:
        print("CNIC should contain 13 digits !!!")
        time.sleep(2)
        return None, None

    with open("./user.json", "r") as file:
        data = json.load(file)

    for user in data:
        if user["cnic"] == cnic:
            print("Already has an account !!")
            time.sleep(2)
            return None, None

    no_of_users = len(data)
    user_id = no_of_users + 72591
    user_data = {
        "user_id": user_id,
        "name": name_of_user,
        "cnic": cnic,
        "borrowed_book": 0,
        "b_book_name": []
    }

    data.append(user_data)

    with open("./user.json", "w") as file:
        json.dump(data, file, indent=4)

    return name_of_user, user_id


def main():
    admin_var = Admin()
    user_var = User()
    
    name_of_user = None
    id_of_user = None
    is_login = False
    admin_state = False
    user_state = False

    while True:
        if not is_login:
            os.system('cls')
            print("\n\t\t\t>>> WELCOME TO DIGITAL LIBRARY SYSTEM <<<")
            print("\t\t\t -- This is a digital library system!!! --\n")
            print("CONTINUE WITH: ")
            choice = input("1) Admin\n2) User\nChoose: ")

            if choice == "1":
                admin_state = True
                user_state = False
            elif choice == "2":
                user_state = True
                admin_state = False
            else:
                print("\nInvalid choice !!!")
                time.sleep(2)
                continue

            if admin_state:
                print("\n\t\t\t>>> Admin Log In <<<\n")
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if admin_var.USERNAME == username and admin_var.PASSWORD == password:
                    is_login = True
                else:
                    print("\nInvalid Credentials !!!")
                    time.sleep(2)
            
            if user_state:
                login_choice = input("\n1) Sign Up\n2) Log In\nChoose: ")
                if login_choice == "1":
                    print("\n\t\t\t>>> User Sign Up <<<\n")
                    cnic = input("Enter CNIC: ")
                    name = input("Enter Your Name: ")
                    name_of_user, id_of_user = store_userdata(cnic, name)
                    if name_of_user:
                        is_login = True

                elif login_choice == "2":
                    print("\n\t\t\t>>> User Log In <<<\n")
                    cnic = input("Enter CNIC: ")
                    name = input("Enter Your Name: ")
                    user_id = input("Enter User Id: ")
                    with open("./user.json", "r") as file:
                        data = json.load(file)
                    for user in data:
                        if str(user["user_id"]) == user_id and user["cnic"] == cnic and user["name"] == name:
                            name_of_user = name
                            id_of_user = user["user_id"]
                            is_login = True
                            break
                    else:
                        print("\nInvalid Credentials !!!")
                        time.sleep(2)

        else:
            if admin_state:
                os.system('cls')
                print("\n\t\t\t>>> Admin Panel <<<\n")
                menu_for_admin = input(
                    "Select Action:\n1) All Books\n2) Add Book\n3) Remove Book\n4) Borrowed Books\n5) Search Book\n6) Search User\n7) Logout\nChoose: "
                )
                if menu_for_admin == "1":
                    os.system('cls')
                    admin_var.show_books()
                    os.system('cls')
                elif menu_for_admin == "2":
                    os.system('cls')
                    admin_var.add_book()
                    os.system('cls')
                elif menu_for_admin == "3":
                    os.system('cls')
                    admin_var.remove_book()
                    os.system('cls')
                elif menu_for_admin == "4":
                    os.system('cls')
                    admin_var.borrowed_books()
                    os.system('cls')
                elif menu_for_admin == "5":
                    os.system('cls')
                    admin_var.search_books()
                    os.system('cls')
                elif menu_for_admin == "6":
                    os.system('cls')
                    admin_var.search_user()
                    os.system('cls')
                elif menu_for_admin == "7":
                    is_login = False
                    admin_state = False
                else:
                    print("\nInvalid choice !!!")
                    time.sleep(2)

            else: # user_state
                os.system('cls')
                print(f"\nWelcome {name_of_user}")
                print(f"- Id # {id_of_user}\n")
                menu_for_user = input(
                    "\nSelect Action:\n1) Show Books\n2) Return Book\n3) Borrowed Books\n4) Search Book\n5) Logout\nChoose: "
                )
                if menu_for_user == "1":
                    os.system('cls')
                    user_var.show_book(id_of_user)
                    os.system('cls')
                elif menu_for_user == "2":
                    os.system('cls')
                    user_var.return_book(id_of_user)
                    os.system('cls')
                elif menu_for_user == "3":
                    os.system('cls')
                    user_var.borrowed_book(id_of_user)
                    os.system('cls')
                elif menu_for_user == "4":
                    os.system('cls')
                    user_var.search_book(id_of_user)
                    os.system('cls')
                elif menu_for_user == "5":
                    is_login = False
                    user_state = False
                else:
                    print("\nInvalid choice !!!")
                    time.sleep(2)


if __name__ == "__main__":
    main()
