import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.columbia.edu/~fdc/sample.html').content
soup = BeautifulSoup(page, "html.parser")

result = []
for link in soup.find_all('h3'):
    result.append(link.get_text())
print(result)

# зачет!
