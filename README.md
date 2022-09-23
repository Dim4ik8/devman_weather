# Погода в разных городах.
Скрипт предназначен для мониторинга погоды в Лондоне, Шереметьево и Череповце. Очень простой и удобный способ.


### Требования к окружению
Устанавливается на любую версию Python.

### Необходимые библиотеки
Для корректной работы скрипта необходимо установить зависимости
> pip install -r requirements.txt

### Текст скрипта достаточно простой

    places = ['london', 'svo', 'cherepovets']

    payload = {'lang': 'ru', 'T': '', 'M': '', 'n': '', 'q': '', }

    for place in places:
        response = requests.get(f"https://wttr.in/{place}", params=payload)
        if response.status_code == 200:
            print(response.text)

        else:
            print('Ошибка запроса, пожалуйста проверьте данные!')
            break

### Результат работы скрипта выводится в терминал
![](example.png)
     