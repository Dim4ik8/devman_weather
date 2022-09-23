import requests


def main():
    places = ['london', 'svo', 'cherepovets']

    payload = {'lang': 'ru', 'T': '', 'M': '', 'n': '', 'q': '', }

    for place in places:
        response = requests.get(f"https://wttr.in/{place}", params=payload)
        if response.status_code == 200:
            print(response.text)

        else:
            print('Ошибка запроса, пожалуйста проверьте данные!')
            break


if __name__ == '__main__':
    main()
