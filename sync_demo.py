import time,os
import requests
from pathlib import Path
from typing import List, Optional
import requests
"""
Demo for Sequential way of downloading images from pexels.com

"""
def download_file(photo_id: str, dirname: Optional[str] ="images_01") -> None:
    # download file from Pexels 
    try:
        url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=640&h=480"
        print(f"Downloading:{photo_id}.jpeg")

        filepath = Path(f"{dirname}/{photo_id}.jpeg")

        # To accept the direct python request to the browser. So, the request will look like it apears from webbrowser
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            with open(filepath, "wb") as img_file:
                img_file.write(response.content)
            print(f"Downloaded: {photo_id}.jpeg")

    except Exception as e:
        print(e)


def download_all(list_photo_ids: List[str], dirname: Optional[str]= "images_01") -> None:

    # download all the photos from the given lists 

    os.makedirs(dirname,exist_ok = True)
    for photo_id in list_photo_ids:
        download_file(photo_id= photo_id,dirname=dirname)
        print(f"-----\n")





if __name__ == "__main__" :
    # get the list of all photos
    with open("list_photos_ids.txt","r") as f:
        list_photo_ids = [ line.rstrip() for line in f.readlines()]
    print(list_photo_ids)

    start_time = time.time()
    download_all(list_photo_ids=list_photo_ids)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed_time:{elapsed_time} seconds")