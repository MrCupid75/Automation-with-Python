"""
    Your task:1. You have the following HTML snippet of a product page:
        <div class="product">
        <h1>Awesome Headphones</h1>
        <p class="price">$99.99</p>
        <p class="description">These headphones offer amazing sound quality!</p>
        </div>
    2. Write a Python script that uses BeautifulSoup to extract the product name, price, and description from this HTML.
"""

from bs4 import BeautifulSoup

html_content = """
    <div class="product">
        <h1>Awesome Headphones</h1>
        <p class="price">$99.99</p>
        <p class="description">These headphones offer amazing sound quality!</p>
    </div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

product_div = soup.select_one('.product')
product_name_tag = product_div.select_one('h1')
product_name = product_name_tag.get_text()

price_tag = product_div.select_one('.price')
price = price_tag.get_text()

print(product_name)
print(price)