from config_data import config
from requests import get, post, codes


def api_request(method_endswith,  # Меняется в зависимости от запроса. locations/v3/search либо properties/v2/list
                params,  # Параметры, если locations/v3/search, то {'q': 'Рига', 'locale': 'ru_RU'}
                method_type  # Метод\тип запроса GET\POST
                ):
    url = f"https://api.dev.apiship.ru/v1/{method_endswith}"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": config.RAPID_API_KEY,
    }
    if method_type == 'GET':
        return get_request(
            url=url,
            params=params,
            headers=headers
        )
    else:
        return post_request(
            url=url,
            params=params,
            headers=headers
        )


def get_request(url, params, headers):
    try:
        response = get(
            url,
            headers=headers,
            params=params,
            timeout=15
        )
        if response.status_code == codes.ok:
            return response.json()
    except ValueError as error:
        print('Ошибка приложения: ' + str(error))


def post_request(url, params, headers):
    try:
        headers["content-type"] = "application/json"
        response = post(
            url,
            headers=headers,
            json=params,
            timeout=15
        )

        print(response.status_code)
        print(response.json())

        if response.status_code == codes.ok:
            return response.json()
    except ValueError as error:
        print('Ошибка приложения: ' + str(error))
