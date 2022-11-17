from fastapi import FastAPI
import asyncio
import uvicorn
import httpx
import concurrent.futures
from math_operations import MedianCalculator

from time import sleep, strftime

math_operations_server = FastAPI()

url = 'http://localhost:8765/get/all'

@math_operations_server.get("/median")
async def median():
    print('start median', strftime("%H:%M:%S"))
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_running_loop()
        inst = MedianCalculator(response.json())
        result = await loop.run_in_executor(executor, inst)
    print('end median', strftime("%H:%M:%S"))
    return result

@math_operations_server.get("/unique_names_histogram")
async def unique_names_histogram():
    print('start unique', strftime("%H:%M:%S"))
    return

@math_operations_server.get("/age_range")
async def age_range():
    print('start age range', strftime("%H:%M:%S"))
    return


if __name__ == '__main__':
    uvicorn.run("math_operations_server:math_operations_server", host='127.0.0.1', port=8766, reload=True)