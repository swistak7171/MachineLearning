import timeit
import requests
import asyncio
import aiohttp


async def download_image(link, session):
    filename = link.split('id/')[1].replace("/", "-")

    async with session.get(link) as response:
        with open(f"images_asyncio/{filename}.jpg", 'wb') as fd:
            async for data in response.content.iter_chunked(1024):
                fd.write(data)


async def main():
    response = requests.get("https://picsum.photos/v2/list")
    array = response.json()
    links = list(map(lambda item: item["download_url"], array))

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(url, session) for url in links]

        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    time_taken = timeit.default_timer() - start_time

    print(f"ASYNCIO - Time taken to download images: {time_taken}")