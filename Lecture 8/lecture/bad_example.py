import json
import random
import requests
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

FILE_PATH = "statuses.json"

lock = Lock()


def download(url):
    print("fetching", url)
    result = requests.get(url)
    print("fetched", result.status)
    return result

def write_to_file(file_path, status):
    print("writing to file")
    with open(file_path, "r") as f:
        data = f.read()
        statuses = json.loads(data)
    
    print("statuses", statuses)
    statuses.append(status)
    print("statuses append", statuses)
    with open(file_path, "w") as f:
        f.write(json.dumps(statuses))

def routine(url):
    response = download(url)
    print("response", response.status)
    with lock:
        write_to_file(FILE_PATH, response.status)

if __name__ == "__main__":
    urls = [
        "https://docs.python.org/3/",
        "https://google.com",
        "https://example.com",
        "https://python.org",
        "https://www.youtube.com/",
        "https://github.com/",
    ]
    with ThreadPoolExecutor() as pool:
        for r in pool.map(routine, urls):
            print(r)