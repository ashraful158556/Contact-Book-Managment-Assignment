def validate_name(name):
    return all(c.isalpha() or c.isspace() for c in name)

def validate_phone(phone, contacts):
    if not phone.isdigit():
        print("Phone number must contain digits only.")
        return False
    for contact in contacts:
        if contact["phone"] == phone:
            print("This phone number already exists.")
            return False
    return True
