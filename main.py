from datetime import datetime
from Birthday_Helper.birthday_helper import get_birthdays_per_week
from Bot import bot

#Task_1
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)}
]

# Call the function from birthday_helper.py
get_birthdays_per_week(users)
#Task2

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = bot.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(bot.add_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()