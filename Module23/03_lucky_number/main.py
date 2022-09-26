import random

errors = [ArithmeticError('Арифметическая ошибка'),  AssertionError('Выражение в функции assert ложно'),
          AttributeError('Объект не имеет данного атрибута (значения или метода)'),
          BufferError('Операция, связанная с буфером, не может быть выполнена'),
          EOFError('Функция наткнулась на конец файла и не смогла прочитать то, что хотела'),
          ImportError('Не удалось импортирование модуля или его атрибута'), LookupError('Некорректный индекс или ключ'),
          MemoryError('Недостаточно памяти'), NameError('Не найдено переменной с таким именем'),
          OSError('Ошибка, связанная с системой'), ReferenceError('Попытка доступа к атрибуту со слабой ссылкой'),
          RuntimeError('Возникает, когда исключение не попадает ни под одну из других категорий'),
          SyntaxError('Синтаксическая ошибка'), SystemError('Внутренняя ошибка'),
          TypeError('Операция применена к объекту несоответствующего типа'),
          ValueError('Функция получает аргумент правильного типа, но некорректного значения'),
          Warning('Предупреждение')]

summa = 0
counter = 0
try:
    with open('nums.txt', 'w') as file:
        while summa <= 777:
            num = int(input('Введите целое число: '))
            summa += num
            counter += 1
            if counter % 13 == 0:
                raise random.choice(errors)
            file.write(str(f'\n{num}'))
            print('Сумма:', summa)

except Exception as errors:
    print('\n', errors)

# зачет!
