from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# The Knot wedding venue URL
base_url = "https://www.theknot.com"
url = "https://www.theknot.com/marketplace/wedding-reception-venues-manassas-va?sort=featured"
venue_website = requests.get(url, headers=headers)
web_text = venue_website.text

# Parse the text with BS4
soup = BeautifulSoup(web_text,"html.parser")
venues = []
venues_link_list = soup.findAll(name="a", class_="info-container--2d227")
print(venues_link_list)

