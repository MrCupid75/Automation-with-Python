from bs4 import BeautifulSoup
import requests

url = "https://jiji.com.gh/cars"

try:
    response = requests.get(url)
except Exception as e:
    print(f"Error fetching webpage {e}")
else:
    soup = BeautifulSoup(response.content, 'html.parser')

main_container = soup.find('div', class_='container')

car_cards = main_container.find_all('div', class_='js-advert-list-item')

print(car_cards)

for card in car_cards:
    car_name = card.find('div', class_='qa-advert-title')

    price = card.find('div', class_='qa-advert-price')

    print(car_name)