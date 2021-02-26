import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=hyundai&l=%EC%9A%B8%EC%82%B0")

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
#print(indeed_soup)

pagination = indeed_soup.find("div", {"class":"pagination"})

#print(pagination)

pages = pagination.find_all('a')
#print(pages)

spans = []
for page in pages:
    #print(page.find("span"))
    spans.append(page.find("span"))
print(spans[:-1])