import requests
from bs4 import BeautifulSoup

def scrapePage(url):
    job_lists = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("div", class_= "jobs-container").findAll("li")

    for job in jobs:
        if job.get("class") == ['view-all']:
            pass
        else:
            data = job.find("div", class_="tooltip--flag-logo").next_sibling
            if data["href"]:
                url = data["href"]
            title = data.find("span", class_="title").text
            company, positionType, region = job.findAll("span", class_="company")
            job_data = {
                "title" : title,
                "company" : company.text,
                "position" : positionType.text,
                "region" : region.text,
                "url" : f"https://weworkremotely.com{url}"
            }
            job_lists.append(job_data)

    return job_lists

def main(keyword):
    if " " in keyword:
        keyword = keyword.replace(" ", "+")
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    print(url)
    return scrapePage(url)