from bs4 import BeautifulSoup
import requests
import lxml
from pprint import PrettyPrinter

URL = "https://www.amazon.com/Nintendo-SwitchTM-Neon-Blue-Joy%E2%80%91ConTM-Switch/dp/B0BFJWCYTL/ref=sr_1_3?crid=11M6EXB90KLFF&keywords=nintendo&qid=1697615662&sprefix=nintend%2Caps%2C300&sr=8-3"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
BUY_PRICE = 289.00

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}

response = requests.get(URL, headers=headers)
website_data = response.content

soup = BeautifulSoup(website_data, "lxml")
# pp = PrettyPrinter()
# pp.pprint(soup)
price = soup.find(name="span", class_="a-offscreen").getText().strip()
price_without_dollar = price.split("$")[1]
float_price = round(float(price_without_dollar).{:.2f})
print(float_price)

product_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip()
print(product_name)

if float_price == BUY_PRICE:
    print(f"{product_name} is now ${BUY_PRICE}, buy today!")
