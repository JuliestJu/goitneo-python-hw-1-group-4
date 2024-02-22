from datetime import datetime, timedelta
from collections import defaultdict

def data_preparation(users):
    birthday_dict = defaultdict(list)
    return birthday_dict

def retrieve_current_date():
    return datetime.today().date()

def sort_users(users, today):
    birthday_dict = defaultdict(list)
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        
        if delta_days < 7:
            weekday = (today + timedelta(days=delta_days)).strftime('%A')
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            
            birthday_dict[weekday].append(name)
    
    return birthday_dict

def display_result(birthday_dict):
    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")

def get_birthdays_per_week(users):
    # Step 1: Data Preparation
    birthday_dict = data_preparation(users)
    
    # Step 2: Retrieval of the Current Date
    today = retrieve_current_date()
    
    # Step 3: Sorting Users
    birthday_dict = sort_users(users, today)
    
    # Step 4: Display Result
    display_result(birthday_dict)