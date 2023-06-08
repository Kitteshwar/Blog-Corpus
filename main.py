import os
import requests
from bs4 import BeautifulSoup

def get_page_text(url):
    try:
        response = requests.get(url,headers = {
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'Referer': 'https://www.fisdom.com/blog/',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    })
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        return text
    except Exception as e:
        print(f"An error occurred while fetching data from {url}: {e}")
        return None

def write_to_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"An error occurred while writing to file {filename}: {e}")

def process_links_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            url = line.strip()
            text = get_page_text(url)
            if text is not None:
                safe_filename = url.replace("/", "_").replace(":","").replace(".","(") + '.txt' 
                write_to_file(safe_filename, text)

# provide your text file name that contains the list of urls
process_links_file("C:/Users/tanya/Desktop/filtered_links.txt")
