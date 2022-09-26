def check(str_elem: str):
    if str_elem == '':
        raise IndexError # Если, напишу здесь сообщение, разве оно запишется в файл?
    lst = list(str_elem.split())
    name = lst[0]
    if name.isalpha() is False:
        raise NameError
    mail = lst[1]
    symbols = ('@', '.')
    for i_sym in symbols:
        if i_sym not in mail:
            raise SyntaxError
    age = int(lst[2])
    if age not in range(10, 100):
        raise ValueError


def write_file(string):
    with open('registrations_bad.log', 'a', encoding='utf-8') as file_bad:
        file_bad.write(string)


with open('registrations.txt', 'r', encoding='utf-8') as file:
    for i_line in file:
        if i_line.endswith('\n'):
            i_line = i_line[:-1]
        try:
            check(i_line)
        except IndexError:
            write_file(f'НЕ присутствуют все три поля!\n')
        except NameError:
            write_file(f'{i_line} - поле имени содержит НЕ только буквы\n')
        except SyntaxError:
            write_file(f'{i_line} - поле емейл НЕ содержит @ и .(точку)\n')
        except ValueError:
            write_file(f'{i_line} - поле возраст НЕ является числом от 10 до 99\n')
        else:
            with open('registrations_good.log', 'a', encoding='utf-8') as file_good:
                file_good.write(f'{i_line}\n')
print('\nГотово!')

# зачет!
