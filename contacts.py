from validators import validate_name, validate_phone

def add_contact(contacts):
    name = input("Enter name: ")
    if not validate_name(name):
        print("Invalid name! Please enter a valid name (only letters and spaces allowed).")
        return

    phone = input("Enter phone number: ")
    if not validate_phone(phone, contacts):
        return
    
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    
    print("----- Contact List -----")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    print("------------------------")

def remove_contact(contacts):
    name = input("Enter the name of the contact to remove: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} removed successfully.")
            return
    print("Contact not found.")

def search_contacts(contacts):
    name = input("Enter name to search: ")
    for contact in contacts:
        if name.lower() in contact["name"].lower():
            print(f"Found contact: {contact}")
            return
    print("Contact not found.")
