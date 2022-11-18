from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    time = datetime.now().strftime('%H:%M:%S  %A %d %B %Y')
    print(f'Здравствуйте! Сейчас:  {time}\n')

    calculate_salary()
    get_employees()