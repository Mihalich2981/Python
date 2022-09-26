file = open('first_tour.txt', 'r', encoding='utf8')
print('\nСодержимое файла first_tour.txt:')
data = file.read()
print(data)
file.close()
file = open('first_tour.txt', 'r', encoding='utf8')
k = int(file.readline())
participants_list = []
for i_line in file:
    line = i_line.split()
    if int(line[-1]) > k:
        participants_list.append(line)
file.close()

new_file = open('second_tour.txt', 'w', encoding='utf8')
new_file.write(f'{str(len(participants_list))}\n')
new_file.close()

participants_list.sort(key=lambda a: int(a[-1]))
participants_list.reverse()
for count, item in enumerate(participants_list, 1):
    participant = str(count) + ') ' + str(item[1][0]) + '. ' + str(item[1]) + ' ' + str(item[-1])
    new_file = open('second_tour.txt', 'a', encoding='utf8')
    new_file.write(f'{participant}\n')
    new_file.close()
print('\nСодержимое файла second_tour.txt:')
new_file = open('second_tour.txt', 'r', encoding='utf8')
new_data = new_file.read()
print(new_data)
file.close()

# зачет!
