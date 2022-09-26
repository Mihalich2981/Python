import requests
import json


episodes = requests.get('https://www.breakingbadapi.com/api/episodes')
deaths = requests.get('https://www.breakingbadapi.com/api/deaths')
data_episodes = json.loads(episodes.text)
data_deaths = json.loads(deaths.text)
my_dct = {}
var = 0
for item in data_deaths:
    if var < item['number_of_deaths']:
        var = item['number_of_deaths']

for item in data_deaths:
    if item['number_of_deaths'] == var:
        for elem in data_episodes:
            if (int(elem['season']) == item['season']) and (int(elem['episode']) == item['episode']):
                my_dct['1. Id эпизода'] = elem['episode_id']
                print('\n1. Id эпизода:', elem['episode_id'])
        my_dct['2. Номер сезона'] = item['season']
        print('2. Номер сезона:', item['season'])
        my_dct['3. Номер эпизода'] = item['episode']
        print('3. Номер эпизода:', item['episode'])
        my_dct['4. Общее количество смертей'] = item['number_of_deaths']
        print('4. Общее количество смертей:', item['number_of_deaths'])
        my_dct['5. Список погибших'] = item['death']
        print('5. Список погибших:', item['death'])
        break

with open('BreakingBad.json', 'w', encoding='utf-8') as file:
    json.dump(my_dct, file, indent=4, ensure_ascii=False)

# зачет!
