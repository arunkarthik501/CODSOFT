contacts = []

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact added successfully!")

    elif choice == '2':
        if not contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(contacts, start=1):
                print(f"{idx}. {contact['name']} - {contact['phone']}")

    elif choice == '3':
        search = input("Enter name or phone number to search: ")
        found = False
        for contact in contacts:
            if contact['name'].lower() == search.lower() or contact['phone'] == search:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif choice == '4':
        update_name = input("Enter the name of the contact to update: ")
        for contact in contacts:
            if contact['name'].lower() == update_name.lower():
                print("Enter new details (leave blank to keep existing):")
                new_name = input(f"New name (current: {contact['name']}): ")
                new_phone = input(f"New phone (current: {contact['phone']}): ")
                new_email = input(f"New email (current: {contact['email']}): ")
                new_address = input(f"New address (current: {contact['address']}): ")

                if new_name:
                    contact['name'] = new_name
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address

                print("Contact updated successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == '5':
        delete_name = input("Enter the name of the contact to delete: ")
        for contact in contacts:
            if contact['name'].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found.")

    elif choice == '6':
        print("Exiting the Contact Book.")
        break

    else:
        print("Invalid choice. Please try again.")