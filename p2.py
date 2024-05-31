import requests
import json

def set_price(api_key, product_id, new_price):
    url = "https://api-supplier.wildberries.ru/promotion/api/v2/products/setPrice"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "offerId": product_id,
        "price": new_price
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Цена товара успешно обновлена")
    else:
        print(f"Произошла ошибка при обновлении цены товара: {response.text}")

# Укажите свой API ключ, идентификатор товара и новую цену
api_key = "Ваш API ключ"
product_id = "Идентификатор товара"
new_price = 999.99

set_price(api_key, product_id, new_price)
