import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
private_num = re.findall(private, text)
taxi = r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'
taxi_num = re.findall(taxi, text)
print('Список номеров частных автомобилей:', private_num)
print('Список номеров такси:', taxi_num)

# зачет!
