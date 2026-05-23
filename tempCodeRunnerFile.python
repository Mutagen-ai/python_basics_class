#Web Scraping
#1
import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (WikiScraper/1.0; educational)"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

#2
def get_title(soup):
    title_tag = soup.find("h1", id = "firstHeading")
    return title_tag.get_text(strip= True) if title_tag else "Title not found"

#3
def get_article_text(soup):
    content_div = soup.find("div", id ="mw-content-text")
    sections = {}
    current_heading = "Introduction"

    for tag in content_div.find_all(["h2", "h3", "p"]):
        if tag.name in ("h2", "h3"):
            current_heading = tag.get_text(strip = True).replace("[edit]", "").strip()
            sections.setdefault(current_heading, [])
        elif tag.name == "p":
            text = tag.get_text(strip = True)
            if text:
                sections.setdefault(current_heading, []).append(text)
    return sections

#4
def get_internal_links(soup):
    links = set()
    for a_tag in soup.find_all("a", href = True):
        href = a_tag["href"]
        if href.startswith("/wiki/") and ":" not in href:
            links.add("https://en.wikipedia.org" + href)
    return sorted(links)

#5
def scrape_wikipedia(url):
    soup     = get_html(url)
    title    = get_title(soup)
    sections = get_article_text(soup)
    links    = get_internal_links(soup)
    return {"title": title, "sections": sections, "links": links}