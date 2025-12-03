#TITTLE: LIBRARY INVENTORY MANAGER
#NAME: ANSHIKA SHRIVASTAVA
#DESCRIPTION:A simple console app that helps the library track, issue, return, and manage books using a JSON-based catalogue.

import json
import os


class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"



class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.catalogue = []
        self.load_catalogue()


    def load_catalogue(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    for b in data:
                        self.catalogue.append(Book(**b))
        except (IOError, json.JSONDecodeError):
            print("Error loading file. Starting with empty library.")


    def save_catalogue(self):
        try:
            with open(self.filename, "w") as file:
                json.dump([b.__dict__ for b in self.catalogue], file, indent=4)
        except IOError:
            print("Error saving the library!")


    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        self.catalogue.append(Book(title, author, isbn))
        self.save_catalogue()
        print("Book added successfully!")

    
    def display_books(self):
        if not self.catalogue:
            print("No books in the library.")
            return
        for b in self.catalogue:
            print(b)


    def issue_book(self):
        isbn = input("Enter ISBN to issue: ")
        for b in self.catalogue:
            if b.isbn == isbn:
                if b.status == "available":
                    b.status = "issued"
                    self.save_catalogue()
                    print("Book issued!")
                else:
                    print("Book already issued.")
                return
        print("Book not found.")


    def return_book(self):
        isbn = input("Enter ISBN to return: ")
        for b in self.catalogue:
            if b.isbn == isbn:
                if b.status == "issued":
                    b.status = "available"
                    self.save_catalogue()
                    print("Book returned!")
                else:
                    print("This book was not issued.")
                return
        print("Book not found.")



def menu():
    lib = Library()

    while True:
        print("\n---- Library Inventory Manager ----")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            lib.add_book()
        elif choice == "2":
            lib.display_books()
        elif choice == "3":
            lib.issue_book()
        elif choice == "4":
            lib.return_book()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")


menu()
