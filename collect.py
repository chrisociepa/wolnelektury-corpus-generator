import os
import requests
import json
from tqdm import tqdm

API_URL = "https://wolnelektury.pl/api/books/"
TXT_URL_TEMPLATE = "https://wolnelektury.pl/media/book/txt/{}.txt"
TXT_FILES_DIR = "./books/"

# Connect to API and get a list of all files
response = requests.get(API_URL)
json_list = json.loads(response.content)

# Iterate over the list and download the txt files
total_files = len(json_list)
downloaded_files = 0
not_found_files = 0
for json_doc in tqdm(json_list, desc="Downloading files", unit="file"):
    slug = json_doc["slug"]
    txt_url = TXT_URL_TEMPLATE.format(slug)
    txt_filename = os.path.join(TXT_FILES_DIR, slug + ".txt")

    # check if file exists before downloading
    if os.path.isfile(txt_filename):
        downloaded_files += 1
        tqdm.write(f"{slug}.txt already exists")
    else:
        response = requests.get(txt_url)
        if response.status_code == 404:
            not_found_files += 1
            tqdm.write(f"{slug}.txt not found")
        else:
            with open(txt_filename, "wb") as f:
                f.write(response.content)
            downloaded_files += 1
            tqdm.write(f"{slug}.txt downloaded")

    # update progress bar
    progress = downloaded_files / total_files * 100
    tqdm.write(f"Progress: {progress:.2f}%")

# print summary stats
tqdm.write(f"Downloaded files: {downloaded_files}")
tqdm.write(f"Not found files: {not_found_files}")
