import os

print("IO comparison:")
os.system("python io_non_concurrent.py")
os.system("python io_threading.py")
os.system("python io_asyncio.py")
os.system("python io_multiprocessing.py")