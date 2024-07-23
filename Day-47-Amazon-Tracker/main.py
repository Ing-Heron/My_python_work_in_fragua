from bs4 import BeautifulSoup
import requests
import smtplib

GMAIL = "heronrobot4@gmail.com"
PASSWORD = "hzds nqcf ozak plms"
# AMAZON_URL = "https://appbrewery.github.io/instant_pot/"
AMAZON_URL = ("https://www.amazon.com.mx/Apple-Nuevo-MacBook-Chip-Pulgadas/dp/B08N6Q71P7/ref=sr_1_6?__mk_es_"
              "MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dib=eyJ2IjoiMSJ9.j_2I9qrGeZsDolaofoxYGpRhmKNuaRhCN1SnrzfLelw0HakNF7Y"
              "TRwTSSNZHxnakqwQ6EjjjJHmRrfoNRZQgiqVUKs6-uoH2PvPlMgFVvF92WXWZ-EzmNtO9bAG37fFJl1XOkVxhXTxGYCpAq409XfB2ry3"
              "Fr7SQKQMZC9eAkc2b4KAlOIPwOMYb9skLfM-3AiGhiSUrr0FftJniO0afYeHVWqb24Scuvp8RNX6pPzIEjX1VCopoMDIWoo1M0dz35Dy"
              "u_h1F4KzR7hx8FJOVXpKcsv2YjPDIVkTgbPH6cao.xNKBPZJmL9u67Qst2wD1gsrh74II8UCsCNCz1pb8i0Y&dib_tag=se&keywords"
              "=macbook&qid=1721687289&s=electronics&sr=1-6&ufe=app_do%3Aamzn1.fos.47e6034e-121d-4b4a-ac82-cf82115f6ad8"
              )

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/126.0.0.0 Safari/537.36",
    "Accepted-Language": "es-419,es;q=0.9",
}

response = requests.get(url=AMAZON_URL, verify=False, headers=headers)
amazon_website = response.text
soup = BeautifulSoup(amazon_website, "html.parser")
amazon_item = soup.find(id="productTitle")
title = amazon_item.get_text().strip()
# amazon_price = soup.find(name="span", class_="aok-offscreen")
# price = float(amazon_price.get_text().strip()[1:])
amazon_price = soup.find(name="span", class_="a-price-whole")
try:
    price = float(amazon_price.get_text().replace(",", ""))
except AttributeError:
    print("El producto no esta disponible")
else:
    if price < 11000:
        print(f"Subject:Amazon Price Alert!\n\n{title} ${price} \n {AMAZON_URL}")
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(GMAIL, PASSWORD)
        #     connection.sendmail(
        #         from_addr=GMAIL,
        #         to_addrs=GMAIL,
        #         msg=f"Subject:Amazon Price Alert!\n\n{title} ${price} \n {AMAZON_URL}".encode("utf-8")
        #     )
        #     print("Ok")
