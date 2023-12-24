import requests
from bs4 import BeautifulSoup

url = 'https://www.technodom.kz'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')

    products = soup.find_all('div', class_='Typography ProductCardV_title__rFAYr ProductCardV_loading__TkTOe Typography__M')

    
    products_dict = {}

    
    for index, product in enumerate(products, start=1):
       
        product_info = {
            'название': product.find('h3', class_='Typography ProductCardV_title__rFAYr ProductCardV_loading__TkTOe Typography__M').text.strip(),
            'цена': product.find('span', class_='Typography ProductCardPrices_price__5dlTx Typography__Subtitle').text.strip(),
           
        }

        
        products_dict[index] = product_info

  
    print(products_dict)

else:
    print(f"Ошибка при запросе: {response.status_code}")
