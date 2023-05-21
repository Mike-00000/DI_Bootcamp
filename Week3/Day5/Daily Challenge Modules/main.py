import requests
import time

def get_page_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time

websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for site in websites:
    load_time = get_page_load_time(site)
    print(f"Load time for {site}: {load_time} seconds")
