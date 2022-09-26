file = open('zen.txt', 'r', encoding='utf-8')
print()
for i_line in reversed(list(file)):
    print(i_line.rstrip())
file.close()

# зачет!
