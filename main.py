import uvicorn
from fastapi import FastAPI
from loguru import logger

from starlette.requests import Request
from starlette.responses import Response



app = FastAPI()


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