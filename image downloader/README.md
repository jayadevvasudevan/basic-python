# Bulk Image Downloader

A Python script that downloads images in bulk from URLs listed in a text file. This tool is perfect for downloading multiple images at once with built-in error handling and progress tracking.

## Features

- **Bulk downloading**: Download multiple images from a list of URLs
- **Smart filename handling**: Automatically generates filenames and handles duplicates
- **Error handling**: Robust error handling with detailed status reporting
- **Progress tracking**: Shows download progress with success/failure counts
- **Respectful downloading**: Includes delays between downloads to be server-friendly
- **Content validation**: Checks if URLs actually point to images
- **Custom headers**: Uses browser-like headers to avoid blocking

## Requirements

- Python 3.6+
- Required packages:
  - `requests`
  - `pathlib` (built-in)
  - `urllib.parse` (built-in)

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install requests
   ```

## Usage

### Basic Usage

1. Create a text file with image URLs (one per line)
2. Run the script:
   ```bash
   python Bulk_downloader.py
   ```

### Input File Format

Create a text file (default: `image_urls.txt`) with one URL per line:

```
https://example.com/image1.jpg
https://example.com/image2.png
https://example.com/image3.gif
# This is a comment and will be ignored
https://example.com/image4.webp
```

**Notes:**
- Empty lines are ignored
- Lines starting with `#` are treated as comments and ignored
- URLs should be complete and properly formatted

### Interactive Mode

When you run the script, it will prompt you for:

1. **Input file path**: Path to your text file containing URLs
   - Press Enter to use default (`image_urls.txt`)
   - Or specify a custom file path

2. **Download folder**: Where to save the downloaded images
   - Press Enter to use default (`downloaded_images`)
   - Or specify a custom folder name

### Example Run

```
Image Downloader Script
==================================================
Enter the path to your text file (press Enter for 'image_urls.txt'): 
Enter download folder name (press Enter for 'downloaded_images'): 
Reading URLs from: image_urls.txt
Download folder: downloaded_images
--------------------------------------------------
Found 5 URLs to download
--------------------------------------------------

[1/5] Downloading: https://example.com/image1.jpg
✓ Successfully downloaded: image1.jpg

[2/5] Downloading: https://example.com/image2.png
✓ Successfully downloaded: image2.png

[3/5] Downloading: https://invalid-url.com/missing.jpg
✗ Error downloading https://invalid-url.com/missing.jpg: 404 Client Error

[4/5] Downloading: https://example.com/image3.gif
✓ Successfully downloaded: image3.gif

[5/5] Downloading: https://example.com/image4.webp
✓ Successfully downloaded: image4.webp

==================================================
Download completed!
✓ Successful: 4
✗ Failed: 1
Total: 5
```

## Function Reference

### `download_image(url, download_folder="downloaded_images", timeout=30)`

Downloads a single image from a URL.

**Parameters:**
- `url` (str): The URL of the image to download
- `download_folder` (str): The folder to save the image to (default: "downloaded_images")
- `timeout` (int): Request timeout in seconds (default: 30)

**Returns:**
- `bool`: True if download was successful, False otherwise

**Features:**
- Creates download folder if it doesn't exist
- Handles duplicate filenames by adding numbers
- Validates content type
- Uses browser-like headers to avoid blocking

### `download_images_from_file(txt_file_path, download_folder="downloaded_images")`

Downloads all images from URLs listed in a text file.

**Parameters:**
- `txt_file_path` (str): Path to the text file containing URLs
- `download_folder` (str): Folder to save downloaded images (default: "downloaded_images")

**Features:**
- Reads URLs from text file
- Ignores empty lines and comments
- Provides progress tracking
- Reports success/failure statistics

## File Structure

```
image downloader/
├── Bulk_downloader.py     # Main script
├── README.md              # This documentation
├── image_urls.txt         # Sample URL list (create this)
└── downloaded_images/     # Default download folder (created automatically)
    ├── image1.jpg
    ├── image2.png
    └── ...
```

## Error Handling

The script handles various error scenarios:

- **Network errors**: Connection timeouts, DNS failures
- **HTTP errors**: 404 Not Found, 403 Forbidden, etc.
- **File system errors**: Permission issues, disk full
- **Invalid URLs**: Malformed or unreachable URLs
- **Content validation**: Non-image content types

## Limitations

- Only downloads publicly accessible images (no authentication)
- Limited to HTTP/HTTPS protocols
- Depends on server response headers for content type validation
- May be blocked by some websites with strict bot protection

## Troubleshooting

### Common Issues

1. **"File not found" error**
   - Make sure your URL text file exists
   - Check the file path is correct

2. **"Permission denied" error**
   - Make sure you have write permissions in the download folder
   - Try running with administrator privileges if needed

3. **Downloads failing with 403/404 errors**
   - Some URLs might be expired or moved
   - Some websites block automated downloads
   - Try accessing the URLs manually in a browser first

4. **Slow downloads**
   - The script includes a 0.5-second delay between downloads by design
   - Large images will naturally take longer to download
   - Network speed affects download time

### Tips for Better Results

- Use direct image URLs (ending in .jpg, .png, etc.) when possible
- Avoid shortened URLs (bit.ly, tinyurl, etc.)
- Test a few URLs manually before bulk downloading
- Check that images are publicly accessible

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

Suggestions and improvements are welcome! Feel free to submit issues or pull requests.