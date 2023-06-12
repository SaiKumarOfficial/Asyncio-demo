import asyncio
import aiohttp
import time
import os
from pathlib import Path
from typing import List, Optional

"""
Demo for Asynchronous way of downloading images from pexels.com

"""
async def download_file(session: aiohttp.ClientSession, photo_id: str , dirname: Optional[str] ="images_02") -> None:
    # download file from Pexels 

    try:
        url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=640&h=480"
        print(f"Downloading:{photo_id}.jpeg")

        filepath = Path(f"{dirname}/{photo_id}.jpeg")

        # To accept the direct python request to the browser. So, the request will look like it apears from webbrowser
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

        async with session.get(url, headers=headers) as response:
            with open(filepath, "wb") as f:
                async for chunk in response.content.iter_chunked(1024):
                    f.write(chunk)

        print(f"Downloaded: {photo_id}.jpeg")

    except Exception as e:
        print(e)


async def download_all(list_photo_ids: List[str], dirname: Optional[str]= "images_02") -> None:

    # download all the photos from the given lists 

    os.makedirs(dirname,exist_ok = True)
    async with aiohttp.ClientSession() as session:
        for photo_id in list_photo_ids:
            #await is used to while one file is downloading, instead of waiting ,you can move to next request 

            await download_file(session = session,photo_id= photo_id,dirname=dirname)
            print(f"-----\n")





if __name__ == "__main__" :
    # get the list of all photos
    with open("list_photos_ids.txt","r") as f:
        list_photo_ids = [ line.rstrip() for line in f.readlines()]
    print(list_photo_ids)

    start_time = time.time()
    # download images in asynchronous way
    asyncio.run(download_all(list_photo_ids=list_photo_ids))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed_time:{elapsed_time} seconds")