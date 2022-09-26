import os


def data_files(path):
    static = [0, 0, 0]
    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = os.path.getsize(file_path)
            static[0] += file_size
            static[1] += 1
        else:
            result = data_files(os.path.abspath(os.path.join(path, i_elem)))
            static[0] += result[0]
            static[1] += result[1]
            static[2] += 1
    return static


path_file = os.path.abspath(os.path.join('..', '..', 'Module14'))
data = data_files(path_file)

print('\nРазмер каталога (в Кб):', data[0] / 1024)
print('Количество подкаталогов:', data[2])
print('Количество файлов:', data[1])

# зачет!
