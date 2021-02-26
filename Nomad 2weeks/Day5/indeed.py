import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=hyundai&l=%EC%9A%B8%EC%82%B0&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pagination = soup.find("div", {"class":"pagination"})  
    
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string)) # == int(link.string)
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)