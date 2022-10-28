import requests
from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

def fetch_response(url: str) -> requests.Response:
    return requests.get(url)

if __name__ == "__main__":
    urls = [
        "https://docs.python.org/3/",
        "https://google.com",
        "https://example.com",
        "https://python.org",
        "https://www.youtube.com/",
        "https://github.com/",
    ]

    start = perf_counter()

    with ProcessPoolExecutor() as pool:
        responses = pool.map(fetch_response, urls)
    print([r.status_code for r in responses])
    print(perf_counter() - start)


