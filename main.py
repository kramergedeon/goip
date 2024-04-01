import uvicorn
from fastapi import FastAPI
from loguru import logger

from starlette.requests import Request
from starlette.responses import Response



app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Получаем информацию о запросе
    method = request.method
    url = request.url
    http_version = request.scope['http_version']
    client = request.client
    headers = dict(request.headers)

    # Выводим информацию о запросе
    logger.info('New request')
    logger.info(f"Received {method} request on {url} (HTTP/{http_version}) from {client}")
    logger.info("Headers:")
    for header, value in headers.items():
        logger.info(f"{header}: {value}")
    logger.info('END request')

    # Продолжаем обработку запроса
    response = await call_next(request)

    return response

@app.post('/sms_receive')
async def sms_receive(request: Request):
    logger.info(f'New SMS: {await request.json()}')
    return Response(status_code=200)


@app.get('/sms_receive')
async def sms_receive(request: Request):
    logger.info(f'New SMS: {request.query_params}')
    return Response(status_code=200)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)