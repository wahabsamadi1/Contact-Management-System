import os

# Global dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact(name, phone_number):
    if name in contacts:
        print("Error: Contact already exists.")
    else:
        contacts[name] = phone_number
        print(f"Added {name} with phone number {phone_number}.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted contact {name}.")
    else:
        print(f"Contact {name} not found.")

# Function to list all contacts
def list_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contacts List ---")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
        print("--------------------")

# Function to save contacts to a file
def save_contacts():
    try:
        with open('contacts.txt', 'w') as file:
            for name, phone_number in contacts.items():
                file.write(f"{name},{phone_number}\n")
        print("Contacts saved successfully.")
    except IOError as e:
        print(f"Error: Could not save contacts. {e}")

# Function to load contacts from a file
def load_contacts():
    if os.path.exists('contacts.txt'):
        try:
            with open('contacts.txt', 'r') as file:
                for line in file:
                    name, phone_number = line.strip().split(',')
                    contacts[name] = phone_number
            print("Contacts loaded successfully.")
        except IOError as e:
            print(f"Error: Could not load contacts. {e}")
    else:
        print("No saved contacts found.")

# Function to handle the main menu
def main():
    load_contacts()  # Load contacts at the start

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Save Contacts")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                name = input("Enter name: ")
                phone_number = input("Enter phone number: ")
                add_contact(name, phone_number)
            elif choice == 2:
                name = input("Enter name to search: ")
                search_contact(name)
            elif choice == 3:
                name = input("Enter name to delete: ")
                delete_contact(name)
            elif choice == 4:
                list_contacts()
            elif choice == 5:
                save_contacts()
            elif choice == 6:
                print("Exiting program...")
                save_contacts()  # Save contacts before exiting
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
