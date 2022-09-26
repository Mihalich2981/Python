students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def function(dictionary):
    lst = []
    cnt = 0
    for i_elem in dictionary.values():
        lst.extend(i_elem['interests'])
        cnt += len(i_elem['surname'])
    return lst, cnt


for i_id, i_val in students.items():
    print(f"{i_id} - {i_val['age']}")

my_lst, length = function(students)
print(my_lst, length)

# зачет!
