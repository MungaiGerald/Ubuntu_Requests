import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    """
    Fetch a single image from a URL and save it in the Fetched_Images directory.
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an error for 4xx/5xx responses

        # Extract filename or assign a default name
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Build the save path
        filepath = os.path.join("Fetched_Images", filename)

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors gracefully
        print(f"✗ Connection error: {e}")
    except Exception as e:
        # Handle unexpected issues
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get the image URL from the user
    url = input("Please enter the image URL: ").strip()

    # Call the fetch function
    fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
