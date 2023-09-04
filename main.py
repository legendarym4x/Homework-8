from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    
    if not users:
        return {}
    # Визначаємо поточну дату та тиждень після неї
    today = date.today()
    next_week = today + timedelta(days=7)  
    
    # Створюємо словники днів тижня (без вихідних) і днів народження
    weekday = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday'}
    birthdays_dict = {day: [] for day in weekday.values()}
    
    #Сортуємо дні народження згідно вимог та добавляємо іменинників до словника 
    for user in users:
        name = user['name'].split()[0]
        birthday = user['birthday'].replace(year=today.year)
        
        if birthday < today:  
            birthday = birthday.replace(year=today.year + 1)
        if today <= birthday <= next_week:
            day_of_week = birthday.strftime("%A")
            if day_of_week not in weekday.values():
                day_of_week = "Monday"
            birthdays_dict[day_of_week].append(name)
             
    birthdays_dict = {day: names for day, names in birthdays_dict.items() if names}             
    return birthdays_dict
    


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
