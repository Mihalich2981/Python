class Student:

    def __init__(self, fi, group, evaluations):
        self.fi = fi
        self.group = int(group)
        self.evaluations = evaluations
        self.average_score = sum(evaluations) / len(evaluations)

    def __repr__(self) -> str:
        return f'ст.{self.fi} гр.{self.group} успеваемость:{self.evaluations}   ср.балл: {self.average_score}'


students_lst = list()
for i_stud in range(5):
    sur_name = input(f'\nВведите фамилию и имя {i_stud + 1} студента: ')
    team = int(input('Введите его группу: '))
    eval_lst = [int(input(f'Введите {i + 1} оценку: ')) for i in range(5)]
    student = Student(sur_name, team, eval_lst)
    students_lst.append(student)
sort_lst = sorted(students_lst, key=lambda x: x.average_score, reverse=True)
print('\nОтсортированный список студентов:')
for i_str in sort_lst:
    print(i_str)

# зачет!
