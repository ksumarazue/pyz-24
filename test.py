# def example_function(a="closure "):
#     def nest_function(b):
#         print(a * b)
#     return nest_function
#
# alias_for_exp = example_function('eee-')
# alias_for_exp(4)


# def sound_decorator(func_as_param):
#     def nested():
#         print('~hau~hau~hau~')
#         func_as_param()
#         print('~hau~hau~hau~')
#
#     return nested
#
#
#
# @sound_decorator(30)
# def quote_pet():
#     print("Pies to najlepszy przyjeciel człowieka")
#
#
# quote_pet()


def display_options() -> None:
    print("1. Display all contacts")
    print("2. Add a new contact")
    print("3. Delete a contact")
    print("4. Quit the program")


from typing import Tuple
from typing import Optional


def get_numbers() -> Tuple[int, int, int]:
    return 600600600, 600600600, 900900900


def get_numberss(number: Optional[int]) -> Tuple[int, int]:
    if number:
        return number, number
    return 608456789, 600234567



def display_contacts(contact_book: list) -> None:
    if not contact_book:
        print("No available contacts.")
    else:
        for contact in contact_book:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print()


def create_contact(contact_book):
    name = input("Enter the name: ")
    email = input("Enter the email address: ")
    while True:
        phone = input("Enter the phone number: ")
        if phone.isdigit() and len(phone) == 9:
            break
        else:
            print("It is not a valid number phone")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contact_book.append(contact)
    print("New contact added!")


def delete_contact(contact_book):
    name = input("Enter the name of the contact to delete: ")
    for contact in contact_book:
        if contact["name"] == name:
            contact_book.remove(contact)
            print("Contact deleted!")
            return
    print("Contact not found.")


def main():
    print("Welcome to the contact management program!")
    contact_book = []

    while True:
        print()
        display_options()
        user_choice = input("Select an option (1-4): ")

        if user_choice == "1":
            display_contacts(contact_book)
        elif user_choice == "2":
            create_contact(contact_book)
        elif user_choice == "3":
            delete_contact(contact_book)
        elif user_choice == "4":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
