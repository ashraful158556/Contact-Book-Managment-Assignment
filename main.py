import os
from contacts import add_contact, view_contacts, remove_contact, search_contacts
from file_operations import load_contacts, save_contacts

def display_menu():
    print("---- Contact Book Management ----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
        elif choice == "4":
            search_contacts(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
