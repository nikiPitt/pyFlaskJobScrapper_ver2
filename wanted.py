from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import file


def playwirghtGO(searchlist):
    for search in searchlist:
        p = sync_playwright().start()
        # Initialize browser and browse
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wanted.co.kr/")
        time.sleep(3)
        page.click("button.Aside_searchButton__Xhqq3")
        time.sleep(3)
        page.get_by_placeholder("검색어를 입력해 주세요.").fill(search)
        time.sleep(3)
        page.keyboard.down("Enter")
        time.sleep(3)
        page.click("a#search_tab_position")

        for _ in range(5):
            page.keyboard.down("End")
            time.sleep(3)

        content = page.content()
        p.stop()
        return scrapeUsingBS(search, content)


def scrapeUsingBS(keyword, content):
    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")
    jobs_lists = []

    for job in jobs:
        url = f"https://www.wanted.co.kr/{job.find('a')['href']}"
        title = job.find("strong", class_="JobCard_title__ddkwM").text
        company = job.find("span", class_="JobCard_companyName__vZMqJ").text
        location = job.find("span", class_="JobCard_location__2EOr5").text

        job = {
            "title": title,
            "company": company,
            "location": location,
            "url": url
        }
        jobs_lists.append(job)

    return jobs_lists