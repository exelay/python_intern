from fastapi import FastAPI

from checker import is_alive_host

app = FastAPI()


@app.get("/healthz")
async def healthz(hostname: str) -> dict:
    """
    Checks if the host is up or down.
    :param hostname: The name of the host being checked.
    """
    status = 'up' if is_alive_host(hostname) else 'down'
    return {'status': status}
