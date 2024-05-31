import requests

def is_proxy_good(proxy):
    test_url = "http://www.google.com"
    proxies = {
        "http": proxy['address'],
        "https": proxy['address'],
    }
    auth = requests.auth.HTTPProxyAuth(proxy['username'], proxy['password'])
    try:
        response = requests.get(test_url, proxies=proxies, auth=auth, timeout=5)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Прокси {proxy['address']} не работает: {e}")
        return False

def call_wildberries(proxy):
    url = "https://www.wildberries.ru"  # Замените на нужный URL Wildberries
    proxies = {
        "http": proxy['address'],
        "https": proxy['address'],
    }
    auth = requests.auth.HTTPProxyAuth(proxy['username'], proxy['password'])
    try:
        response = requests.get(url, proxies=proxies, auth=auth, timeout=5)
        if response.status_code == 200:
            print("Запрос к Wildberries успешен через прокси:", proxy['address'])
        else:
            print(f"Ошибка при запросе к Wildberries через прокси {proxy['address']}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ошибка при запросе к Wildberries через прокси {proxy['address']}: {e}")

def main():
    proxy_list = [
        {'address': 'http://proxy1-address:port', 'username': 'username1', 'password': 'password1'},
        {'address': 'http://proxy2-address:port', 'username': 'username2', 'password': 'password2'},
        {'address': 'http://proxy3-address:port', 'username': 'username3', 'password': 'password3'},
        # Добавьте другие прокси в этот список
    ]

    for proxy in proxy_list:
        if is_proxy_good(proxy):
            call_wildberries(proxy)
            break
    else:
        print("Нет доступных прокси для использования")

if __name__ == "__main__":
    main()
