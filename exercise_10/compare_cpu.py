import os

print("CPU comparison:")
os.system("python cpu_non_concurrent.py")
os.system("python cpu_threading.py")
os.system("python cpu_multiprocessing.py")