import json
import os
import time

class Admin:
    USERNAME = "admin"
    PASSWORD = "admin"

    def show_books(self):
        with open("./data.json", "r") as file:
            books = json.load(file)

        print("\n\t\t\t>>> ALL BOOKS AVAILABLE <<<\n")

        for book in books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Book ID: {book['id']}")
            print(f"Total Copies: {book['no_of_copies']}")
            print(f"Available Copies: {book['available_copies']}")
            print("--------------------------------")
        
        input("\nPress Enter To Go Back to Admin Panel: ")
        

    def add_book(self):
        print("\n\t\t\t>>> ADD BOOKS <<<\n")

        choice = input("1) Add Existing Book \n2)Add New Book \nSelect: ")

        if choice == "2":
            print("\nADD NEW BOOK :\n")
            title = input("Enter Title Of Book: ")
            author = input("Enter Author Of Book: ")
            copies = int(input("Enter No. of Copies: "))

            with open("./data.json", "r") as file:
                books = json.load(file)

            book_id = len(books) + 62851
            data = {
                "id": book_id,
                "title": title,
                "author": author,
                "no_of_copies": copies,
                "available_copies": copies
            }
            books.append(data)

            with open("./data.json", "w") as file:
                json.dump(books, file, indent=4)
            print("\nSuccessfully Added !!!")
            time.sleep(2)

        elif choice == "1":
            print("\nADD EXISTING BOOK :\n")
            title = input("Enter Title Of Book: ")
            author = input("Enter Author Of Book: ")
            book_id = input("Enter Book ID: ")
            copies_to_add = int(input("Enter No. of Copies to Add: "))

            with open("./data.json", "r") as file:
                books = json.load(file)

            for book in books:
                if book["title"] == title and book["author"] == author and book["id"] == int(book_id):
                    book["available_copies"] += copies_to_add
                    book["no_of_copies"] += copies_to_add
                    print("\nSuccessfully Added !!!")
                    time.sleep(2)
                    break
            else:
                print("\nNo Book Available !!!")
                time.sleep(2)

            with open("./data.json", "w") as file:
                json.dump(books, file, indent=4)
        
        else:
            print("\nInvalid Option !!!")
            time.sleep(2)
        

    def remove_book(self):
        print("\n\t\t\t>>> REMOVE BOOK <<<\n")
        title = input("Enter Title Of Book: ")
        author = input("Enter Author Of Book: ")
        book_id = input("Enter Book ID: ")
        copies_to_remove = int(input("Enter No. of Copies to Remove: "))

        with open("./data.json", "r") as file:
            books = json.load(file)

        new_list = []
        book_found = False
        for book in books:
            if book["title"] == title and book["author"] == author and book["id"] == int(book_id):
                book_found = True
                if book["available_copies"] < copies_to_remove and book["no_of_copies"] >= copies_to_remove:
                    print("\nBook are not available for removal!!!")
                    time.sleep(2)
                elif book["no_of_copies"] < copies_to_remove:
                    print(f"Not Enough Books To Remove!!! , You have total {book['no_of_copies']} copies")
                    time.sleep(2)
                elif book["available_copies"] == book["no_of_copies"] and book["no_of_copies"] == copies_to_remove:
                    print("\nSuccessfully Removed!!!")
                    time.sleep(2)
                    continue  # Skip appending to remove
                elif book["available_copies"] >= copies_to_remove:
                    book["available_copies"] -= copies_to_remove
                    book["no_of_copies"] -= copies_to_remove
                    print("\nSuccessfully Removed!!!")
                    time.sleep(2)
                new_list.append(book)
            else:
                new_list.append(book)

        if not book_found:
            print("\nNo Book Available !!!")
            time.sleep(2)

        with open("./data.json", "w") as file:
            json.dump(new_list, file, indent=4)
        

    def borrowed_books(self):
        print("\n\t\t\t>>> ALL BORROWED BOOKS <<<\n")

        with open("./data.json", "r") as file:
            books = json.load(file)

        with open("./user.json", "r") as files:
            users = json.load(files)

        for book in books:
            if book["no_of_copies"] > book["available_copies"]:
                borrowed_book_user = []
                for user in users:
                    for title in user["b_book_name"]:
                        if title[0] == book["title"]:
                            if title[1] == book["author"]:
                                borrowed_book_user.append([user["user_id"], title[2]])

                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Book ID: {book['id']}")
                print(f"Total Copies: {book['no_of_copies']}")
                print(f"Available Copies: {book['available_copies']}")
                print("Users Data:")
                for data in borrowed_book_user:
                    print(f"  -> User Id: {data[0]} | No. of copies: {data[1]}")
                print("-" * 30)
        
        input("\nPress Enter To Go Back To Admin Panel")
        

    def search_books(self):
        print("\n\t\t\t>>> SEARCH BOOKS <<<\n")

        role = input("1)Title \n2)Author \n3)Id \nEnter Option: ")

        with open("./data.json", "r") as file:
            books = json.load(file)

        if role == "1":
            title = input("Enter Title: ")
            for book in books:
                if title == book["title"]:
                    self._print_book_details(book)
                    break
            else:
                print("\nNo Book Available !!!")
                time.sleep(2)
        elif role == "2":
            author = input("Enter Author Name: ")
            for book in books:
                if author == book["author"]:
                    self._print_book_details(book)
                    break
            else:
                print("\nNo Book Available !!!")
                time.sleep(2)
        elif role == "3":
            id_by_user = input("Enter Book Id: ")
            for book in books:
                if id_by_user == str(book["id"]):
                    self._print_book_details(book)
                    break
            else:
                print("\nNo Book Available !!!")
                time.sleep(2)
        else:
            print("\nInvalid Option !!!")
            time.sleep(2)
        
        input("\nPress Enter To Go Back To Admin Panel")
        

    def search_user(self):
        print("\n\t\t\t>>> SEARCH USER <<<\n")

        role = input("1) Name \n2) Id \n3) CNIC \nEnter Option: ")

        with open("./user.json", "r") as file:
            users = json.load(file)

        if role == "1":
            name = input("Enter Name: ")
            for user in users:
                if name == user["name"]:
                    self._print_user_details(user)
                    break
            else:
                print("\nNo User Found !!!")
                time.sleep(2)
        elif role == "2":
            id_user = input("Enter Id: ")
            for user in users:
                if id_user == str(user["user_id"]):
                    self._print_user_details(user)
                    break
            else:
                print("\nNo User Found !!!")
                time.sleep(2)
        elif role == "3":
            cnic = input("Enter CNIC: ")
            if len(cnic) == 13:
                for user in users:
                    if cnic == user["cnic"]:
                        self._print_user_details(user)
                        break
                else:
                    print("\nNo User Found !!!")
                    time.sleep(2)
            else:
                print("\nCNIC Should have 13 digits !!!")
                time.sleep(2)
        
        else:
            print("\nInvalid Option !!!")
        
        input("\nPress Enter To Go Back To Admin Panel")
        

    def _print_book_details(self, book):
        print("\n")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Book ID: {book['id']}")
        print(f"Total Copies: {book['no_of_copies']}")
        print(f"Available Copies: {book['available_copies']}")
        print("\n")


    def _print_user_details(self, user):
        print("\n")
        print(f"-> Name: {user['name']}")
        print(f"-> CNIC: {user['cnic']}")
        print(f"-> User ID: {user['user_id']}")
        print("-> Borrowed Book: ")
        for book_b_list in user["b_book_name"]:
            print(f"       Title: {book_b_list[0]}")
            print(f"       Author: {book_b_list[1]}")
            print(f"       Copies: {book_b_list[2]}")
            print("-" * 60)
        print("\n")
        
