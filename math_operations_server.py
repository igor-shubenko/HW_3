from fastapi import FastAPI
import asyncio
import uvicorn
import httpx
import concurrent.futures
from math_operations import MedianCalculator, UniqueNamesCalculator, AgeRangeCalculator

math_operations_server = FastAPI()

url = 'http://localhost:8765/get/all'

@math_operations_server.get("/median")
async def median():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        inst = MedianCalculator(response.json())
        result = await loop.run_in_executor(executor, inst)

    return result

@math_operations_server.get("/unique_names_histogram")
async def unique_names_histogram():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        inst = UniqueNamesCalculator(response.json())
        result = await loop.run_in_executor(executor, inst)

    return result

@math_operations_server.get("/age_range")
async def age_range(frm: int, to: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        inst = AgeRangeCalculator(response.json())
        result = await loop.run_in_executor(executor, inst, frm, to)

    return result


if __name__ == '__main__':
    uvicorn.run("math_operations_server:math_operations_server", host='127.0.0.1', port=8766, reload=True)
