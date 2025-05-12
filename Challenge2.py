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

soup = BeautifulSoup()