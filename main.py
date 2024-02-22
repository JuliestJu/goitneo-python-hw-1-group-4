from datetime import datetime
from Task_1 import birthday_helper


#Task_1
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)}
]

# Call the function from birthday_helper.py
birthday_helper.get_birthdays_per_week(users)