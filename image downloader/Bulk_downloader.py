import os
import requests
from urllib.parse import urlparse
import time
from pathlib import Path

def download_image(url, download_folder="downloaded_images", timeout=30):
    """
    Download an image from a URL and save it to the specified folder.
    
    Args:
        url (str): The URL of the image to download
        download_folder (str): The folder to save the image to
        timeout (int): Request timeout in seconds
    
    Returns:
        bool: True if download was successful, False otherwise
    """
    try:
        # Create download folder if it doesn't exist
        Path(download_folder).mkdir(exist_ok=True)
        
        # Parse the URL to get the filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename in URL, create one based on timestamp
        if not filename or '.' not in filename:
            timestamp = int(time.time())
            filename = f"image_{timestamp}.jpg"
        
        # Full path for the downloaded file
        file_path = os.path.join(download_folder, filename)
        
        # Handle duplicate filenames
        counter = 1
        original_filename = filename
        while os.path.exists(file_path):
            name, ext = os.path.splitext(original_filename)
            filename = f"{name}_{counter}{ext}"
            file_path = os.path.join(download_folder, filename)
            counter += 1
        
        print(f"Downloading: {url}")
        
        # Download the image
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=timeout, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Check if the content is actually an image
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            print(f"Warning: URL might not be an image (Content-Type: {content_type})")
        
        # Save the image
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"✓ Successfully downloaded: {filename}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error downloading {url}: {e}")
        return False

def download_images_from_file(txt_file_path, download_folder="downloaded_images"):
    """
    Download all images from URLs listed in a text file.
    
    Args:
        txt_file_path (str): Path to the text file containing URLs
        download_folder (str): Folder to save downloaded images
    """
    if not os.path.exists(txt_file_path):
        print(f"Error: File '{txt_file_path}' not found!")
        return
    
    print(f"Reading URLs from: {txt_file_path}")
    print(f"Download folder: {download_folder}")
    print("-" * 50)
    
    successful_downloads = 0
    failed_downloads = 0
    
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            urls = [line.strip() for line in file if line.strip() and not line.strip().startswith('#')]
        
        if not urls:
            print("No URLs found in the file!")
            return
        
        print(f"Found {len(urls)} URLs to download")
        print("-" * 50)
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}]", end=" ")
            
            if download_image(url, download_folder):
                successful_downloads += 1
            else:
                failed_downloads += 1
            
            # Small delay to be respectful to servers
            time.sleep(0.5)
        
        print("\n" + "=" * 50)
        print(f"Download completed!")
        print(f"✓ Successful: {successful_downloads}")
        print(f"✗ Failed: {failed_downloads}")
        print(f"Total: {len(urls)}")
        
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    """Main function to run the image downloader."""
    print("Image Downloader Script")
    print("=" * 50)
    
    # Default text file name
    txt_file = "image_urls.txt"
    
    # Ask user for input file if default doesn't exist
    if not os.path.exists(txt_file):
        user_input = input(f"Enter the path to your text file (press Enter for '{txt_file}'): ").strip()
        if user_input:
            txt_file = user_input
    
    # Ask for download folder
    download_folder = input("Enter download folder name (press Enter for 'downloaded_images'): ").strip()
    if not download_folder:
        download_folder = "downloaded_images"
    
    # Start downloading
    download_images_from_file(txt_file, download_folder)

if __name__ == "__main__":
    main()