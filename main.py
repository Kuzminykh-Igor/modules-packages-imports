from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


# Запуск файла производить в терминале (чтобы отображался прогресс-бар).
if __name__ == '__main__':
    print(f"Добрый день! Сегодня: {datetime.now().strftime('%d.%m.%Y')}")
    calculate_salary()
    get_employees()
