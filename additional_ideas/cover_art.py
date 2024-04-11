import csv
import requests
from bs4 import BeautifulSoup

def extract_cover_url(album_name):
    search_url = f"https://en.wikipedia.org/wiki/{album_name.replace(' ', '_')}"
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        infobox = soup.find('table', {'class': 'infobox'})
        if infobox:
            image_tag = infobox.find('img')
            if image_tag:
                image_url = image_tag['src']
                return image_url
    return None

def update_csv_cover_image(csv_filename):
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        
        for row in rows:
            album_name = row['Album']
            cover_url = extract_cover_url(album_name)
            if cover_url:
                row['Cover'] = cover_url
            else:
                row['Cover'] = 'No cover found'

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    csv_filename = 'rolling_stone_top_500_albums_2020.csv'
    update_csv_cover_image(csv_filename)

if __name__ == "__main__":
    main()