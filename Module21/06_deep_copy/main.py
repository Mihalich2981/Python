from copy import deepcopy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {name} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {name}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def find(struct, prod):
    for key, val in struct.items():
        if isinstance(val, dict):
            find(val, prod)
        else:
            struct[key] = val.format(name=prod)
            return struct
    return struct


def func(sit, depth=0):
    for key, val in sit.items():
        print('   ' * depth, key, ':', end=' ')
        if isinstance(val, dict):
            print()
            func(val, depth + 1)
        else:
            print(sit[key])


question = int(input('\nСколько будет сайтов: '))
new_site = deepcopy(site)
for _ in range(question):
    new_site = deepcopy(site)
    product = input('\nВведите название продукта для нового сайта: ').lower()
    print(f'Сайт для {product}:')
    print('site =')
    var = find(new_site, product)
    func(var)

# зачет!
