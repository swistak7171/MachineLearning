import os

print("Images download comparison")
os.system("python images_non_concurrent.py")
os.system("python images_threading.py")
os.system("python images_multiprocessing.py")
os.system("python images_asyncio.py")
