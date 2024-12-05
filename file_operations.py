import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            lines = file.readlines()
            for line in lines:
                name, phone, email, address = line.strip().split(", ")
                contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}, {contact['phone']}, {contact['email']}, {contact['address']}\n")
