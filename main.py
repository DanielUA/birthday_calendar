from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    users_to_greet = {}

    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        if birthday.month == 1:
            birthday = birthday.replace(year=today.year+1)
        else:
            birthday = birthday.replace(year=today.year)

        days_until_birthday = (birthday - today).days        
        if 0 <= days_until_birthday < 7:
            greeting_day = (today + timedelta(days_until_birthday)).strftime("%A")
            
            if greeting_day == "Saturday":
                greeting_day = "Monday"
                birthday += timedelta(days=2)
            elif greeting_day == "Sunday":
                greeting_day = "Monday"
                birthday += timedelta(days=1)
          
            if greeting_day not in users_to_greet:
                users_to_greet[greeting_day] = []
            users_to_greet[greeting_day].append(name)

    return users_to_greet

if __name__ == "__main__":
    users = [
        {"name": "Alice", "birthday": datetime(2000, 1, 1).date()},
        {"name": "Bob", "birthday": datetime(1985, 12, 11).date()},
        {"name": "Charlie", "birthday": datetime(1995, 12, 19).date()},
        {"name": "Charlie1", "birthday": datetime(1995, 12, 21).date()},
        {"name": "Charlie2", "birthday": datetime(1995, 12, 25).date()},
        {"name": "John", "birthday": datetime(1995, 12, 27).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")