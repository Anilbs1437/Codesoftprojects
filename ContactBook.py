class Contact:
    def __init__(self, name: str, phone_number: str, email: str, address: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self) -> str:
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name: str, phone_number: str, email: str, address: str) -> None:
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self) -> None:
        if not self.contacts:
            print("Contact book is empty.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contacts(self, search_query: str) -> None:
        found_contacts = [contact for contact in self.contacts if search_query.lower() in contact.name.lower() or search_query in contact.phone_number]
        if not found_contacts:
            print(f"No contacts found with '{search_query}'.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, search_query: str, new_name: str = None, new_phone_number: str = None, new_email: str = None, new_address: str = None) -> None:
        found_contact = next((contact for contact in self.contacts if search_query.lower() == contact.name.lower() or search_query == contact.phone_number), None)
        if found_contact:
            if new_name:
                found_contact.name = new_name
            if new_phone_number:
                found_contact.phone_number = new_phone_number
            if new_email:
                found_contact.email = new_email
            if new_address:
                found_contact.address = new_address
            print("Contact updated successfully.")
        else:
            print(f"No contact found with '{search_query}'.")

    def delete_contact(self, search_query: str) -> None:
        contact_to_delete = next((contact for contact in self.contacts if search_query.lower() == contact.name.lower() or search_query == contact.phone_number), None)
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            print("Contact deleted successfully.")
        else:
            print(f"No contact found with '{search_query}'.")


def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            contact_book.add_contact(name, phone_number, email, address)

        elif choice == '2':
            print("\nContacts:")
            contact_book.view_contacts()

        elif choice == '3':
            search_query = input("Enter name or phone number to search: ").strip()
            contact_book.search_contacts(search_query)

        elif choice == '4':
            search_query = input("Enter name or phone number of contact to update: ").strip()
            new_name = input("Enter new name (leave blank to keep current): ").strip() or None
            new_phone_number = input("Enter new phone number (leave blank to keep current): ").strip() or None
            new_email = input("Enter new email (leave blank to keep current): ").strip() or None
            new_address = input("Enter new address (leave blank to keep current): ").strip() or None
            contact_book.update_contact(search_query, new_name, new_phone_number, new_email, new_address)

        elif choice == '5':
            search_query = input("Enter name or phone number of contact to delete: ").strip()
            contact_book.delete_contact(search_query)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
