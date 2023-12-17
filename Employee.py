import logging
from datetime import datetime

logging.basicConfig(filename='Person.log.', filemode='w', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Класс Person')


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


def input_data():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    age = int(input('Введите возраст: '))
    position = input('Введите должность: ')
    raise_salary = int(input('Введите зарпалату: '))
    return last_name, first_name, patronymic, age, position, raise_salary


while True:
    ex = int(input('Введите 0 для заверешения программы иначе 1: '))
    if ex == 0:
        break
    last_name, first_name, patronymic, age, position, raise_salary = input_data()
    try:
        emp = Employee(last_name, first_name, patronymic, age, position, raise_salary)
        command = int(input('Введите конмаду:\n1) Вывести фамилию\n2) Вывести имя\n3) Вывести отчество\n4) Вывести ФИО\n5) Вывести возраст\n6) Увеличить возраст на 1\n7) Узнать зарплату\n8) Узнать должность\nКоманда: '))
        logger.info(f'Введена команда обработки - {command = }')
        if command == 1:
            print(emp.last_name)
            logger.info(f'Результат равен {emp.last_name}')
        elif command == 2:
            print(emp.first_name)
            logger.info(f'Результат равен {emp.first_name}')
        elif command == 3:
            print(emp.patronymic)
            logger.info(f'Результат равен {emp.patronymic}')
        elif command == 4:
            print(emp.full_name())
            logger.info(f'Результат равен {emp.full_name()}')
        elif command == 5:
            print(emp.get_age)
            logger.info(f'Результат равен {emp.get_age}')
        elif command == 6:
            print(emp.birthday)
            logger.info(f'Результат равен {emp.birthday}')
        elif command == 7:
            print(emp.salary)
            logger.info(f'Результат равен {emp.salary}')
        elif command == 8:
            print(emp.position)
    except Exception as e:
        logging.critical(f'{datetime.now().strftime("%H:%M:%S")} произошла ошибка {e}')

