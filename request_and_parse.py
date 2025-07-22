import requests
from bs4 import BeautifulSoup

url = "https://www.ampol.com.au/"

response = requests.get(url, headers={"Accept": "text/html"})
parsed_response = BeautifulSoup(response.text, "html.parser")
nav_mega_menu = parsed_response.find("ul", class_="amp-mega-menu__nav")
nav_titles = nav_mega_menu.find_all("li", class_="amp-mega-menu__nav-item", recursive=False)
#how many titles are there?
print(f"Number of navigation titles: {len(nav_titles)}")
# Print the navigation titles
for title in nav_titles:
    nav = title.find("a", class_="amp-mega-menu__nav-link")
    if nav:
        print(nav.get_text(strip=True))
