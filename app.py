import requests


def is_alive_host(hostname):
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    url = 'http://' + hostname
    try:
        response = requests.get(url)
        status_code = response.status_code
        if 100 <= status_code <= 400:
            return True
    except Exception:
        return False
