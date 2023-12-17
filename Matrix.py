import logging
from datetime import datetime

import numpy as np

logging.basicConfig(filename='Matrix.log.', filemode='w', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Класс Matrix')


class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols] * rows

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __eq__(self, other):
        return self.data == other.data

    def __add__(self, other):
        result0 = Matrix(self.rows, self.cols)
        result0.data = [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)]
        return result0

    def __mul__(self, other):
        result1 = np.matmul(self.data, other.data)
        return '\n'.join([' '.join(map(str, row)) for row in result1])


def input_data():
    rows = int(input('Введите кол-во строк матрицы: '))
    cols = int(input('Введите кол-во столбцов матрицы: '))
    data = []
    a = []
    for i in range(rows):
        for j in range(cols):
            a.append(int(input('Введите числа матрицы: ')))
        data.append(a)
        a = []
    return rows, cols, data


def data_matr(command, data1):
    if command == 1:
        print(matrix1.cols)
        logger.info(f'Результат равен {matrix1.cols}')
    elif command == 2:
        print(matrix1.rows)
        logger.info(f'Результат равен {matrix1.rows}')
    elif command == 3:
        matrix1.data = data1
        print(matrix1)
        logger.info(f'Результат равен {matrix1}')


while True:
    ex = int(input('Для заверешния работы нажмите 0 иначе 1: '))
    if ex == 0:
        break
    rows1, cols1, data1 = input_data()
    try:
        matrix1 = Matrix(rows1, cols1)
        command1 = int(input(
            'Введите команду для обработки данных:\n1) Показать столбцы\n2) Показать строки\n3) Показать матрицу\n4) Задание второй матрицы\nКоманда: '))
        logger.info(f'Введена команда обработки - {command1 = }')
        data_matr(command1, data1)
        if command1 == 4:
            rows2, cols2, data2 = input_data()
            try:
                matrix2 = Matrix(rows1, cols1)
                command2 = int(input(
                    'Введите команду для обработки данных:\n1) Показать столбцы\n2) Показать строки\n3) Показать матрицу\n4) Проверить равенсво двех матриц\n5) Сложить матрицы\n6) Умножить матрицы\nКоманда: '))
                logger.info(f'Введена команда обработки - {command2 = }')
                data_matr(command2, data2)
                if command2 == 4:
                    print(matrix1 == matrix2)
                    logger.info(f'Результат равен {matrix1 == matrix2}')
                if command2 == 5:
                    print(matrix1 + matrix2)
                    logger.info(f'Результат равен {matrix1 + matrix2}')
                if command2 == 6:
                    print(matrix1 * matrix2)
                    logger.info(f'Результат равен {matrix1 * matrix2}')
            except Exception as e:
                logging.critical(f'{datetime.now().strftime("%H:%M:%S")} произошла ошибка {e}')
    except Exception as e:
        logging.critical(f'{datetime.now().strftime("%H:%M:%S")} произошла ошибка {e}')
