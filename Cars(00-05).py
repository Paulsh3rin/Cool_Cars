import pandas as pd
import requests
from bs4 import BeautifulSoup

cars_url = "https://www.kbb.com/car-finder/?manufacturers=bmw&years=2000-2005&seolink=false"

response = requests.get(cars_url)
soup = BeautifulSoup(response.content, "html.parser")

car_names = [car.text.strip() for car in soup.find_all('h2')]

df = pd.DataFrame({'Model':car_names})
print(df)
