import requests
from bs4 import BeautifulSoup


result = requests.get('https://www.rrg.com.np/')

# print(result.status_code)
# print(result.headers)

src = result.content

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
# print(links)
# print('\n')

for link in links:
  if "About" in link.text:
    print(link)
    print(link.attrs['href'])