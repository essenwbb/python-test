import asyncio
import requests


async def hello(n, url):
    print("协程" + str(n) + "启动")
    res = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
    print("协程-----------------------" + str(n) + "结束")
    print(res.status_code)


if __name__ == "__main__":
    tasks = []
    url = 'https://www.baidu.com/'
    for i in range(0, 100):
        tasks.append(hello(i, url))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
