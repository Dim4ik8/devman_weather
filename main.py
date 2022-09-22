import requests


def main():
    location = ['london', 'svo', 'cherepovets']

    payload = {'lang': 'ru', 'T': '', 'M': '', 'n': '', 'q': '', }

    try:
        for place in location:
            response = requests.get(f"https://wttr.in/{place}", params=payload)
            print(response.text)

    except requests.exceptions.HTTPError:
        print('Ошибка запроса, пожалуйста проверьте данные!')


if __name__ == '__main__':
    main()
