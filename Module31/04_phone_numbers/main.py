import re

tel_lst = ['9999999999', '999999-999', '99999x9999', '8098876', '812345678', '0123456789', '81234567890']

tel_pattern = r'[89]\d{9}\b'

for key, item in enumerate(tel_lst):
    if re.findall(tel_pattern, item):
        print(f'{key + 1} номер: всё в порядке')
    else:
        print(f'{key + 1} номер: не подходит')

# зачет!
