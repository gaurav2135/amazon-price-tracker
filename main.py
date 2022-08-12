import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

my_email = "erenjaeger1607@gmail.com"

amazon_url = "https://www.amazon.in/Street27%C2%AE-Necklace-Investigation-Teenagers-Silver_White_Blue/dp/B09LMV1JP9/ref=sr_1_14?crid=36ZTSA74LKGNO&keywords=necklace+for+men&qid=1651384446&sprefix=necklace+for+men%2Caps%2C262&sr=8-14"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=amazon_url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(name="span", class_="a-price-whole").get_text()
fraction_price = soup.find(name="span", class_="a-price-fraction").get_text()
true_price = soup.find(name="span", class_="a-offscreen").get_text()
total_price = float(price+fraction_price)
print(total_price)

title = soup.find(name="span", id="productTitle").get_text()


print(title)
if total_price <= 330:
    message = f"Subject: Low Price\n\n{title}\n{true_price}\n{amazon_url}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="eren@1607")
        connection.sendmail(from_addr=my_email, to_addrs="gauravchauhan2135@gmail.com", msg=message.encode(errors="ignore"))






