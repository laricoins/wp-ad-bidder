import schedule
import time

def main():
    proxy_list = [
        "http://proxy1-address:port",
        "http://proxy2-address:port",
        "http://proxy3-address:port",
        # Добавьте другие прокси в этот список
    ]

    for proxy in proxy_list:
        if is_proxy_good(proxy):
            call_wildberries(proxy)
            break
    else:
        print("Нет доступных прокси для использования")
#запуск раз в (1) минуту
schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
