import requests
import file
from bs4 import BeautifulSoup

all_jobs = []

def scrapePage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_= "jobs").findAll("li")[0:-1]

    for job in jobs:
        url = job.find("div", class_="tooltip--flag-logo").next_sibling
        if url:
            url = url["href"]
        title = job.find("span", class_="title").text
        company, positionType, region = job.findAll("span", class_="company")
        job_data = {
            "title" : title,
            "company" : company.text,
            "position" : positionType.text,
            "region" : region.text,
            "url" : f"https://weworkremotely.com{url}"
        }
        all_jobs.append(job_data)

def getPages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

def main():
    totalPages = getPages("https://weworkremotely.com/remote-full-time-jobs?page=1")
    for i in range(totalPages):
        url = f"https://weworkremotely.com/remote-full-time-jobs?page={i+1}"
        scrapePage(url)

main()