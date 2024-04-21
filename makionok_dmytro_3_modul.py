   # Макійонок Дмитро blended_group_2
   # Task 1 
from datetime import datetime

def get_days_from_today(date):
    try: 
    # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d')
    
    # Отримуємо поточну дату
        current_date = datetime.today()

    # Cповіщення за від'ємність дати
        if input_date > current_date:
            print(f"Задана дата {date}, є пізнішою за поточну")

    # Рахуємо різницю між поточною датою та заданою датою
        difference = current_date.toordinal() - input_date.toordinal()
    
    # Повертаємо різницю у днях як ціле число
        return difference
    except ValueError:
        # Обробляємо виняток у випадку неправильного формату вхідних даних
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."

# Приклад 
date1 = '2026-04-11'
print(get_days_from_today(date1))

 # Є ще варіант цього коду без tordinal() через return difference.days

def get_days_from_today(date1):
    try:
    # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date1, '%Y-%m-%d')
    
    # Отримуємо поточну дату
        current_date = datetime.today()

    # Cповіщення за від'ємність дати
        if input_date > current_date:
            print(f"Задана дата {date1} , є пізнішою за поточну")

    # Рахуємо різницю між поточною датою та заданою датою
        difference = current_date - input_date
    
    # Повертаємо різницю у днях як ціле число
        return difference.days
    except ValueError:
        # Обробляємо виняток у випадку неправильного формату вхідних даних
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД"

# Приклад 
date1 = '2022-04-11'
print(get_days_from_today(date1))

 # Task 2

import random

def get_numbers_ticket(min, max, quantity):
    # Перевіряємо параметри функції
    if min < 1 or max > 1000 or quantity > max - min + 1: 
        return []
    
    # Генеруємо випадковий список чисел у заданому діапазоні без повторювань
    numbers = random.sample(range(min, max + 1), quantity)
    # Повертаємо список
    return sorted(numbers)

# Приклад використання
min = 5
max = 10
quantity = 4
print(get_numbers_ticket(min, max, quantity))

# Task 3 
import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Додаємо міжнародний код '+38', якщо його немає
    if not cleaned_number.startswith('+'):
        # Перевіряємо, чи номер починається з '380'
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    
    return cleaned_number

# Приклад використання
print(normalize_phone("+38(050)123-32-34"))  # +380501233234
print(normalize_phone("0503451234"))         # +380503451234
print(normalize_phone("(050)8889900"))      # +380508889900
print(normalize_phone("38050-111-22-22"))    # +380501112222
print(normalize_phone("38050 111 22 11   ")) # +380501112211
