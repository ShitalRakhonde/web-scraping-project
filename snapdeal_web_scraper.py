import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape_snapdeal_html(max_products=40):

    print("scraper started")

    url = "https://www.snapdeal.com/products/mens-tshirts-polos"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print("status_code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("p", class_="product-title")

    print("Total products found:", len(products))

    products_list = []

    for p in products[:max_products]:
        name = p.text.strip()

        products_list.append({
            "Product Name": name
        })

    df = pd.DataFrame(products_list)

    df.to_csv("snapdeal_products.csv", index=False)

    print("CSV file saved successfully!")


# RUN FUNCTION
scrape_snapdeal_html(40)