import uvicorn
from fastapi import FastAPI
from loguru import logger
# from fastapi.middleware.cors import CORSMiddleware
# from starlette.middleware.sessions import SessionMiddleware

from starlette.requests import Request
from starlette.responses import Response


app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     # Получаем информацию о запросе
#     method = request.method
#     url = request.url
#     http_version = request.scope['http_version']
#     client = request.client
#     headers = dict(request.headers)
#
#     # Выводим информацию о запросе
#     logger.info('New request')
#     logger.info(f"Received {method} request on {url} (HTTP/{http_version}) from {client}")
#     logger.info("Headers:")
#     for header, value in headers.items():
#         logger.info(f"{header}: {value}")
#     logger.info('END request')
#
#     # Продолжаем обработку запроса
#     response = await call_next(request)
#
#     return response

@app.post('/smsreceive')
async def sms_receive(request: Request):
    try:
        logger.info(f'New SMS: {await request.json()}')
    except:
        ...
    return Response(status_code=200, content='OK')


# @app.get('/smsreceive')
# async def sms_receive(request: Request):
#     logger.info(f'New SMS: {request.query_params}')
#     return Response(status_code=200)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)