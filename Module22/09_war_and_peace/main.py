import zipfile


def unzip(archive):
    zip_file = zipfile.ZipFile(archive, 'r')
    for i_file in zip_file.namelist():
        zip_file.extract(i_file)
    zip_file.close()


def stats(name_file):
    result = {}
    if name_file.endswith('zip'):
        unzip(name_file)
        name_file = ''.join((name_file[:-3], 'txt'))
    file_txt = open(name_file, 'r', encoding='utf-8')
    for i_line in file_txt:
        for i_sym in i_line:
            if i_sym.isalpha():
                if i_sym not in result:
                    result[i_sym] = 0
                result[i_sym] += 1
    file_txt.close()
    return result


file = 'voyna-i-mir.zip'
stats_dict = stats(file)
stats_sort = sorted(stats_dict.items(), key=lambda x: x[1], reverse=True)
for nun, letter in stats_sort:
    print(f"Буква '{nun}' в тексте, встречается {letter} раз")

# зачет!
