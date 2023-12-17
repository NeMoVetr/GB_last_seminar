import logging
from datetime import datetime

logging.basicConfig(filename='Rectangle.log.', filemode='w', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Класс Rectangle')


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):

        return 2 * (self._width + self._height)

    def area(self):

        return self._width * self._height

    def __add__(self, other):

        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):

        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


def input_data():
    width = int(input('Введите ширину прямоугольника: '))
    height = int(input('Введите высоту прямоугольника (если это крадрат, нажмите 0): '))
    return width, height


def data(command):
    if command == 1:
        print(rectangle1.width)
        logger.info(f'Результат равен {rectangle1.width}')
    elif command == 2:
        print(rectangle1.height)
        logger.info(f'Результат равен {rectangle1.height}')
    elif command == 3:
        print(rectangle1.area())
        logger.info(f'Результат равен {rectangle1.area()}')
    elif command == 4:
        print(rectangle1.perimeter())
        logger.info(f'Результат равен {rectangle1.perimeter()}')
    elif command == 5:
        print(rectangle1)
        logger.info(f'Результат равен {rectangle1}')


while True:
    width1, height1 = input_data()
    if width1 == -1:
        print('Cпасибо')
        break
    try:
        if height1 == 0:
            rectangle1 = Rectangle(width1)
        else:
            rectangle1 = Rectangle(width1, height1)

        logger.info(f'Введена ширина - {width1}; Высота - {height1}')
        print(
            'Введите команду по обработки данных:\n1) Узнать ширину\n2) Узнать высоту\n3) Площадь\n4) Периметр\n5) Вывести полностью прямоугольник\n6) Ввести следующий прямоугольник для дальнейшей работы')
        command = int(input('Введите команду: '))
        logger.info(f'Введена команда обработки - {command = }')
        data(command)
        if command == 6:
            width2, height2 = input_data()
            try:
                if height2 == 0:
                    rectangle2 = Rectangle(width2)
                else:
                    rectangle2 = Rectangle(width2, height2)

                command_2 = int(input(
                    'Введите команду по обработки данных:\n1) Узнать ширину\n2) Узнать высоту\n3) Площадь\n4) Периметр\n5) Вывести полностью прямоугольник\n6) Сложить\n7) Вычесть\n8) Проверка на то что первый меньше второго\nВведите команду: '))
                logger.info(f'Введена команда обработки - {command_2 = }')
                data(command_2)
                if command_2 == 6:
                    print(rectangle1 + rectangle2)
                    logger.info(f'Результат равен {rectangle1 + rectangle2}')
                elif command_2 == 7:
                    print(rectangle1 - rectangle2)
                    logger.info(f'Результат равен {rectangle1 - rectangle2}')
                elif command_2 == 8:
                    print(rectangle1 < rectangle2)
                    logger.info(f'Результат равен {rectangle1 < rectangle2}')

            except Exception as e:
                logging.critical(f'{datetime.now().strftime("%H:%M:%S")} произошла ошибка {e}')
    except Exception as e:
        logging.critical(f'{datetime.now().strftime("%H:%M:%S")} произошла ошибка {e}')
