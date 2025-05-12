from bs4 import BeautifulSoup
import requests

url = "https://jiji.com.gh/cars"

try:
    response = requests.get(url)
except Exception as e:
    print(f"Error fetching webpage {e}")
else:
    soup = BeautifulSoup(response.content, 'html.parser')
