message = list(input('\nСообщение: '))
var = ''
new_message = ''
for i_num in range(len(message)):
    if message[i_num].isalnum():
        var += message[i_num]
        if i_num == len(message) - 1:
            new_message += var[::-1]
    else:
        new_message += var[::-1] + message[i_num]
        var = ''
print('Новое сообщение:', new_message)

# зачет!
