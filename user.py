import json
import time

class User:
    def show_book(self, user_id):
        print("\n\t\t\t>>> ALL AVAILABLE BOOKS <<<\n")
        with open("./data.json", "r") as file:
            books = json.load(file)

        with open("./user.json", "r") as files:
            users = json.load(files)

        for book in books:
            if book["available_copies"] > 0:
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Book ID: {book['id']}")
                print(f"Available Copies: {book['available_copies']}")
                
                print("--------------------------------------")
        
        def borrowing_book(b_book_id):
            for book in books:
                if book["id"] == b_book_id:
                    book["available_copies"] -= 1
                    for user in users:
                        if user["user_id"] == user_id:
                            user["borrowed_book"] += 1
                            for book_list in user["b_book_name"]:
                                if book_list[0] == book["title"]:
                                    book_list[2] += 1
                                    break
                            else:
                                user["b_book_name"].append([book["title"], book["author"], 1])
                            print(f"Title: {book['title']} Borrowed Successfully !!!")
                            time.sleep(2)
                            break 
                    break

            else:
                print("\nBook Not Found !!!")
                time.sleep(2)  
                                   
        
        borrow = input("\nLike To Borrow Some Book? (y/n): ")
        print("\n")
        while borrow.lower() == 'y':
            borrow_book_id = int(input("Enter The Id of The Book: "))
            borrowing_book(borrow_book_id)
            borrow = input("\nLike To Borrow Some More Books? (y/n): ")
            print("\n")
                    
                    

        with open("./user.json", "w") as update:
            json.dump(users, update, indent=4)
        with open("./data.json", "w") as update_data:
            json.dump(books, update_data, indent=4)

        input("\nPress Enter To Go Back To User Panel")

    def return_book(self, user_id):
        print("\n\t\t\t>>> RETURN BOOK <<<\n")
        title = input("Enter Title Of Book: ")
        author = input("Enter Author Of Book: ")
        copies_to_return = int(input("Enter No. of Copies to Return: "))

        with open("./data.json", "r") as file:
            books = json.load(file)

        with open("./user.json", "r") as files:
            users = json.load(files)

        
        user_found = False
        for user in users:
            if user["user_id"] == user_id:
                user_found = True
                book_found = False
                for book_list in user["b_book_name"]:
                    if book_list[0] == title and book_list[1] == author:
                        book_found = True
                        if book_list[2] > copies_to_return:
                            book_list[2] -= copies_to_return
                            self._update_book_copies(title, author, copies_to_return)
                            user["borrowed_book"] -= copies_to_return
                            print("\nSuccessfully Returned !!!")
                            time.sleep(2)
                        elif book_list[2] == copies_to_return:
                            user["b_book_name"].remove(book_list)
                            self._update_book_copies(title, author, copies_to_return)
                            user["borrowed_book"] -= copies_to_return
                            print("\nSuccessfully Returned !!!")
                            time.sleep(2)
                        else:
                            print("\nNot Enough Copies To Return!!!")
                            time.sleep(2)
                        break
                if not book_found:
                    print("\nBook Not Found !!!")
                    time.sleep(2)
                break
        if not user_found:
            print("\nUser not found!")
            time.sleep(2)


        with open("./user.json", "w") as file:
            json.dump(users, file, indent=4)
        
        with open("./data.json", "w") as file:
            json.dump(books, file, indent=4)


    def _update_book_copies(self, title, author, copies):
        print("call")
        with open("./data.json", "r") as file:
            books = json.load(file)
        for book in books:
            if book["title"] == title and book["author"] == author:
                book["available_copies"] += copies
                print(f"updated!!! {copies} + {book["available_copies"]}")
                break
        with open("./data.json", "w") as file:
            json.dump(books, file, indent=4)


    def borrowed_book(self, user_id):
        print("\n\t\t\t>>> ALL BORROWED BOOKS <<<\n")
        with open("./user.json", "r") as files:
            users = json.load(files)

        with open("./data.json", "r") as file:
            books = json.load(file)

        for user in users:
            if user["user_id"] == user_id:
                print(f"-> Total Number Of Books: {user['borrowed_book']}")
                for book_list in user["b_book_name"]:
                    bookId = 0
                    for book in books:
                        if book["title"] == book_list[0] and book["author"] == book_list[1]:
                            bookId = book["id"]

                    print("---------------------------------")
                    print(f"Title: {book_list[0]}")
                    print(f"Author: {book_list[1]}")
                    print(f"Book ID: {bookId}")
                    print(f"Borrowed Copies: {book_list[2]}")
        
        input("\nPress Enter To Go Back To User Panel")

    def search_book(self, user_id):
        print("\n\t\t\t>>> SEARCH BOOK <<<\n")
        role = input("Search By: \n1)Title \n2)Author \n3)Id \nEnter Option: ")

        with open("./data.json", "r") as file:
            books = json.load(file)

        if role == "1":
            title = input("\nEnter Title: ")
            for book in books:
                if title == book["title"]:
                    self._print_book_details_for_user(book, user_id)
                    break
            else:
                print("\nNo Book Available !!!")
                time.sleep(2)

        elif role == "2":
            author = input("\nEnter Author Name: ")
            for book in books:
                if author == book["author"]:
                    self._print_book_details_for_user(book, user_id)
                    break
            else:
                print("\nNo Book Available !!!")
                time.sleep(2)

        elif role == "3":
            id_by_user = input("\nEnter Book Id: ")
            for book in books:
                if id_by_user == str(book["id"]):
                    self._print_book_details_for_user(book, user_id)
                    break
            else:
                print("\nNo Book Available !!!")
                time.sleep(2)
        
        else:
            print("\nInvalid Option !!!")
            time.sleep(2)

        input("\nPress Enter To Go Back To User Panel")

    def _print_book_details_for_user(self, book, user_id):
        print(f"\nTitle: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Book ID: {book['id']}")
        print(f"Available Copies: {book['available_copies']}")
        borrow = input("\nBorrow this book? (y/n): ")
        if borrow.lower() == 'y':
            with open("./user.json", "r") as files:
                users = json.load(files)
            
            with open("./data.json", "r") as file:
                books = json.load(file)

            for b in books:
                if b['id'] == book['id']:
                    b["available_copies"] -= 1
                    break


            for user in users:
                if user["user_id"] == user_id:
                    user["borrowed_book"] += 1
                    for book_list in user["b_book_name"]:
                        if book_list[0] == book["title"]:
                            book_list[2] += 1
                            break
                    else:
                        user["b_book_name"].append([book["title"], book["author"], 1])
                    print("\nBorrowed Successfully !!!")
                    time.sleep(2)
                    break

            with open("./user.json", "w") as update:
                json.dump(users, update, indent=4)
            
            with open("./data.json", "w") as update_data:
                json.dump(books, update_data, indent=4)
