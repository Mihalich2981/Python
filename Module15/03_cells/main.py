number_cells = int(input('\nКол-во клеток: '))
unsuitable = []

for i in range(1, number_cells + 1):
    print('Эффективность', i, 'клетки:', end=' ')
    efficiency = int(input())
    if efficiency < i:
       unsuitable.append(efficiency)

print('\nНеподходящие значения:', unsuitable)



# Можно и так решить!

#number_cells = int(input('\nКол-во клеток: '))
#unsuitable = ''
#for i in range(1, number_cells + 1):
#    print('Эффективность', i, 'клетки:', end=' ')
#    efficiency = int(input())
#   if efficiency < i:
#        unsuitable += (str(efficiency) + ' ')
#print('\nНеподходящие значения:', unsuitable)

# зачет!
