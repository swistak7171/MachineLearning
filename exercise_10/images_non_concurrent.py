import timeit
from urllib import request

import requests

def download_image(link):
    filename = link.split('id/')[1].replace("/", "-")
    request.urlretrieve(link, f"images_non_concurrent/{filename}.jpg")
    print(f"{filename}.jpg downloaded into /images_non_concurrent folder")


def main():
    response = requests.get("https://picsum.photos/v2/list")
    array = response.json()
    for item in array:
        download_image(item["download_url"])


if __name__ == "__main__":
    print("Time taken to download images synchronously: {}".format(timeit.Timer(main).timeit(number=1)))
