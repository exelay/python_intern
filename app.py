import requests
from fastapi import FastAPI
from requests.exceptions import ConnectionError, InvalidURL

app = FastAPI()


@app.get("/healthz")
async def healthz(hostname: str) -> dict:
    status = 'up' if is_alive_host(hostname) else 'down'
    return {'status': status}


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
