import requests
from requests.exceptions import ConnectionError, InvalidURL


def is_alive_host(hostname: str) -> bool:
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    url = 'http://' + hostname
    try:
        response = requests.get(url)
        status_code = response.status_code
        if 100 <= status_code < 400:
            return True
        return False
    except ConnectionError:
        return False
    except InvalidURL:
        return False
