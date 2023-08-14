import html
import http.cookiejar as cookie
import json
import sys
from time import sleep
from urllib.parse import urlparse

import requests
import requests.utils
from bs4 import BeautifulSoup

jar = cookie.MozillaCookieJar("/home/xk/.local/cookies-reddit-com.txt")
jar.load(ignore_discard=True, ignore_expires=True)

session = requests.Session()
session.headers = {
    "Accept-Language": "en-US,en",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
}
session.cookies = jar

session.get("https://old.reddit.com")

urls = open("/home/xk/d/63_Sounds/scrape_link.urls").readlines()


def get_page_links(url):
    link = url.strip().replace("/old.", "/api.").replace("/www.", "/api.").replace("/new.", "/api.")
    page = session.get(link)

    try:
        print(json.loads(page.text)[0]["data"]["children"][0]["data"]["url"])
    except:
        pass

    try:
        text = json.loads(page.text)[0]["data"]["children"][0]["data"]["selftext_html"]
    except:
        print(link, file=sys.stderr)
        return
    if text is None:
        print(link, file=sys.stderr)
        return

    soup = BeautifulSoup(html.unescape(text), "lxml")
    extlist = set()

    for a in soup.findAll("a", attrs={"href": True}):
        if (
            len(a["href"].strip()) > 1
            and a["href"][0] != "#"
            and "javascript:" not in a["href"].strip()
            and "mailto:" not in a["href"].strip()
            and "tel:" not in a["href"].strip()
        ):
            if "http" in a["href"].strip() or "https" in a["href"].strip():
                if urlparse(link).netloc.lower() in urlparse(a["href"].strip()).netloc.lower():
                    get_page_links(a["href"])
                else:
                    extlist.add(a["href"])
            else:
                print(link, file=sys.stderr)

    for el in extlist:
        print(el)


for link in urls:
    get_page_links(link)
    sleep(1)
