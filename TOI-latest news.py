import requests
import bs4
from urllib.request import urlopen

url = "https://timesofindia.indiatimes.com/"
response = requests.get(url) # opens the URL
html =   response.content # returns the content of the page

soup = bs4.BeautifulSoup(html, 'html.parser') # parses the page
latsto = soup.find('div', attrs = {'id':'lateststories'})
file = latsto.find('div', attrs = {'class': 'sechead'})
titleplace =latsto.find('div', attrs = {'class':'latestNewContainer'})
x = titleplace.find('ul', attrs = {'class':'list9'})

top = soup.find('div', attrs = {'class':'top-area'})
container = top.find('div', attrs = {'class':'container'})

res = urlopen('http://just-the-time.appspot.com/')
result = res.read().strip()
result_str = result.decode('utf-8')
print()
print("Date and time: ",result_str)
print()


print(file.text)
print()

s = 1

for li in x:
    print(s,".",li.text)
    s+=1
