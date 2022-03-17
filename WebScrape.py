import pandas as pd
import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
    url = f'https://ca.indeed.com/jobs?q=software%20developer&l=Waterloo%2C%20ON&start={page}&vjk=dee3c9ab6b4ae204'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = "job_seen_beacon")
    for item in divs:
        title = item.find('h2').text
        company = item.find('span', class_ = "companyName").text
        try:
            salary = item.find('div', class_ = "salary-snippet").text
        except:
            salary = 'No Information'
        job = {
            'Title': title,
            'Company': company,
            'Salary': salary
        }
        joblist.append(job)
    return

joblist = []
for i in range(0, 70, 10):
    print(f"getting_page, {i}")
    c = extract(i)
    transform(c)
    

df = pd.DataFrame(joblist)
print(df)
df.to_csv('jobs.csv')
