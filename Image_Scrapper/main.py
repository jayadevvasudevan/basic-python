import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download images
def download_images(url, folder):
    # Send a request to fetch the HTML content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create a folder to save the images
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Find all <img> tags and extract image URLs
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        # Sometimes images are relative URLs, so convert them to absolute
        img_url = urljoin(url, img_url)
        
        try:
            # Get the image content
            img_data = requests.get(img_url).content
            
            # Extract image name from the URL
            img_name = os.path.basename(img_url)
            
            # Save the image
            with open(os.path.join(folder, img_name), 'wb') as img_file:
                img_file.write(img_data)
            print(f'Downloaded {img_name}')
        except Exception as e:
            print(f"Couldn't download {img_url}. Error: {e}")

# Example usage
website_url = 'https://www.example.com'
folder_name = 'downloaded_images'
download_images(website_url, folder_name)
