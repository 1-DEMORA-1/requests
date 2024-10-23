import time
import requests
import threading
from tqdm import tqdm
print("")
time.sleep(0.3)
print("██████╗░██╗░░░██╗  ██████╗░███████╗███╗░░░███╗░█████╗░██████╗░░█████╗░")
time.sleep(0.3)
print("██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔════╝████╗░████║██╔══██╗██╔══██╗██╔══██╗")
time.sleep(0.3)
print("██████╦╝░╚████╔╝░  ██║░░██║█████╗░░██╔████╔██║██║░░██║██████╔╝███████║")
time.sleep(0.3)
print("██╔══██╗░░╚██╔╝░░  ██║░░██║██╔══╝░░██║╚██╔╝██║██║░░██║██╔══██╗██╔══██║")
time.sleep(0.3)
print("██████╦╝░░░██║░░░  ██████╔╝███████╗██║░╚═╝░██║╚█████╔╝██║░░██║██║░░██║")
time.sleep(0.3)
print("╚═════╝░░░░╚═╝░░░  ╚═════╝░╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝")
time.sleep(0.4)
def create_terms_file():
    with open("Условия пользования.txt", "w", encoding="utf-8") as file:
        file.write("ыыы")

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response Code: {response.status_code}, URL: {url}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    download_terms = input("Скачать файл условий использования? Y/N: ").strip().upper()

    if download_terms == 'Y':
        print("Скачиваем файл с сервера 'Условия пользования.txt'")

        for _ in tqdm(range(5), desc="Создание файла", colour="#009FBD", unit="chunk"):
            time.sleep(0.5)  
        create_terms_file()
        print("файл уже в папке")

    vpp = input("Согласны ли вы с условиями пользования? Y/N: ").strip().upper()
    if vpp == 'N':
        print("Программа завершена.")
        return
    elif vpp == 'Y':
        print("Вы согласились с условиями. Переходим к отправке запросов.")
        mainss()
    else:
        print("Неверный ввод, программа завершена.")

def mainss():
    url = input("Введите URL для нагрузки: ")
    number_of_requests = int(input("Введите количество запросов для отправки: "))

    threads = []

    for _ in range(number_of_requests):
        thread = threading.Thread(target=send_request, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
