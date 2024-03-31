import uvicorn
from fastapi import FastAPI
import socket
import logging

from starlette.requests import Request

logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware('http')
async def add_trace_id_header(request: Request, call_next):
    logger.info(f"Listening on {request.method}:{request.items()}")
    response = await call_next(request)
    return response

@app.api_route('*', methods=['GET', 'POST'])
async def test_route():
    logger.info(f"Listening on {Request.method}:{Request}")
# UDP_IP = "0.0.0.0"  # Принимаем запросы с любых адресов
# UDP_PORT = 44444  # Порт, который будет слушать сервер
#
# @app.get("/")
# async def read_root():
#     return {"message": "Hello World"}
#
#
# @app.on_event("startup")
# async def startup_event():
#     global udp_socket
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     udp_socket.bind((UDP_IP, UDP_PORT))
#     logger.info(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")
#
# @app.on_event("shutdown")
# async def shutdown_event():
#     udp_socket.close()
#     logger.info("UDP socket closed")
#
# @app.get("/udp")
# async def read_udp():
#     data, addr = udp_socket.recvfrom(1024)  # Принимаем данные
#     return {"message": f"Received UDP data: {data.decode('utf-8')}"}

#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=44444)