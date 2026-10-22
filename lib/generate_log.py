from datetime import datetime
import os

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

    pass
from datetime import datetime
import requests

def fetch_data():
    # Fetch data from public API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

def generate_log_file():
    log_data = ["User logged in", "User updated profile", "Report exported"]
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
            
    # Also fetch and append API post title to log output
    post = fetch_data()
    post_title = post.get("title", "No title found")
    file_name_api = "api_output.txt"
    with open(file_name_api, "w") as api_file:
        api_file.write(f"Fetched Post Title: {post_title}\n")

    print(f"Log written to {filename} and API output written to {file_name_api}")

if __name__ == "__main__":
    generate_log_file()
