import requests


def main():
    places = ['london', 'svo', 'cherepovets']

    payload = {'lang': 'ru', 'T': '', 'M': '', 'q': '', 'n': ''}

    for place in places:
        response = requests.get(f"https://wttr.in/{place}", params=payload)
        if response.ok:
            print(response.text)

        else:
            print('Ошибка запроса, пожалуйста проверьте данные!')
            break


if __name__ == '__main__':
    main()
