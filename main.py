import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.ca/Apple-AirPods-3rd-Generation-Lightning-Charging/dp/B0BDHB9Y8H/ref=sr_1_5?keywords=airpods&s=electronics&sr=1-5"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(name="span", class_="a-offscreen")
price_text = price.getText().split("$")[1]
price_as_num = float(price_text)

title = soup.find(name="span", id="productTitle")
email_title = title.getText().strip()
email_title = email_title.encode("ascii", errors="ignore")
print(email_title)

if price_as_num < 200:
    my_email = "hasankhanalt@gmail.com"
    password = "dhavwnvdlocelwei"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Amazon Price Alert!\n\n{email_title} is now ${price_as_num}\n{URL}")
