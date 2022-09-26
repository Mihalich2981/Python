goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678'
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42}
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520}
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150}
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97}
    ]
}

for i_key, i_val in goods.items():
    summa = sum(j_quan['quantity'] for j_quan in store[i_val])
    cost = sum(j_cost['quantity'] * j_cost['price'] for j_cost in store[i_val])
    print(i_key, '-', summa, 'шт, стоимость', cost, 'руб')

# зачет!
