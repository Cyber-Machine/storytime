import requests
from bs4 import BeautifulSoup
import pickle
  
URL = "https://www.gutenberg.org/cache/epub/2641/pg2641-images.html"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
content = []
chapter = soup.findAll('div', attrs = {'class':'chapter'})
chapter = chapter[2:-5]
# for row in chapter:
#     print(row)
# print(chapter)
for item in chapter:
    if item.name == "div": # Here the work
       for para in item:
        if(para.name == 'p'):
            content.append(para.text)

wwrite = open('MobyD.txt', 'w')
wwrite.writelines(content)
wwrite.close()