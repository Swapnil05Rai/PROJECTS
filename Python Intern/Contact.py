import colorama
from colorama import Fore, Style
# Define the Contact class to represent a single contact


class Contact:
    def __init__(self, name, phone_number, email, address):
        # Initialize the attributes of the contact
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

# Define the ContactManagementSystem class to manage contacts


class ContactManagementSystem:
    def __init__(self):
        # Initialize an empty list to store contacts
        self.contacts = []


def main():
    # Create a ContactManagementSystem object to start managing contacts
    contact_manager = ContactManagementSystem()

    # Infinite loop to show the menu and handle user input
    while True:
        # Display options for the user
        print(Fore.MAGENTA +
              "-------------- Contact Management System --------------" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit" + Style.RESET_ALL)

        # Ask the user for their choice
        choice = input("Enter your choice: ")

        # If the user chooses to add a contact
        if choice == "1":
            # Get contact details from the user
            name = input("Enter name: ")
            phone = input("Enter phone: ")

            # Check if the phone number is an integer of length 10 using the 'isdigit()' method
            if not phone.isdigit():
                print(Fore.RED+"Invalid phone number. Phone number must be an integer.")
                # Continue the loop to prompt the user again for valid input
                continue

            email = input("Enter email: ")

            # Check if the email contains '@'
            if "@" not in email:
                print(Fore.RED+"Invalid email address. Email must contain '@'.")
                # Continue the loop to prompt the user again for valid input
                continue

            address = input("Enter address: ")

            # Create a Contact object with the given details
            contact = Contact(name, phone, email, address)

            # Add the contact to the ContactManagementSystem's list of contacts
            contact_manager.contacts.append(contact)

        # If the user chooses to view all contacts
        elif choice == "2":
            # If there are no contacts, inform the user
            if not contact_manager.contacts:
                print("No contacts found.")
            else:
                # Display details of each contact in the list
                for contact in contact_manager.contacts:
                    print(Fore.GREEN+f"Name: {contact.name}")
                    print(f"Phone: {contact.phone_number}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}")
                    print("----------------------"+Style.RESET_ALL)

        # If the user chooses to search for a contact
        elif choice == "3":
            # Get the name to search for from the user
            name = input("Enter name: ")

            # Initialize an empty list to store found contacts
            found_contacts = []

            # Search for contacts matching the given name
            for contact in contact_manager.contacts:
                if name.lower() in contact.name.lower():
                    found_contacts.append(contact)

            # Display the found contacts
            if not found_contacts:
                print("No matching contacts found.",Fore.RED)
            else:
                for contact in found_contacts:
                    print(Fore.GREEN+f"Name: {contact.name}")
                    print(f"Phone: {contact.phone_number}")
                    print(f"Email: {contact.email}")
                    print(f"Address: {contact.address}")
                    print("----------------------"+Style.RESET_ALL)

        # If the user chooses to delete a contact
        elif choice == "4":
            # Get the name of the contact to delete from the user
            name = input("Enter name: ")

            # Initialize a variable to track if the contact was deleted
            deleted = False

            # Search for the contact with the given name
            for contact in contact_manager.contacts:
                if contact.name.lower() == name.lower():
                    # Remove the contact from the list
                    contact_manager.contacts.remove(contact)
                    print(Fore.GREEN+f"Contact '{contact.name}' deleted.")
                    deleted = True
                    break

            # If the contact was not found, inform the user
            if not deleted:
                print(Fore.RED+f"Contact with name '{name}' not found.")

        # If the user chooses to exit the program
        elif choice == "5":
            # Exit the loop and end the program
            break

        # If the user provides an invalid choice
        else:
            print("Invalid choice", Fore.RED)


if __name__ == "__main__":
    main()
