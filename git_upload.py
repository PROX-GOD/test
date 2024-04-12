import requests
import os

def upload_folder():
    repo_name = input("Enter the name of the repository: ")
    folder_path = input("Enter the path of the folder to upload: ")

    # GitHub authentication
    username = "PROX-GOD"
    email = "preshakbhattarai534@gmail.com"
    token = "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"

    # API endpoint
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/"

    # Headers with authentication
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Walk through the directory
    for root, _, files in os.walk(folder_path):
        # Loop through files in current directory
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Read file content
            with open(file_path, "rb") as file:
                file_content = file.read()

            # Base64 encode file content
            import base64
            file_content_encoded = base64.b64encode(file_content).decode()

            # Create file payload
            relative_path = os.path.relpath(file_path, folder_path)
            payload = {
                "message": f"Upload {relative_path}",
                "content": file_content_encoded,
                "branch": "main"
            }

            # Send POST request to create file
            response = requests.put(url + relative_path, headers=headers, json=payload)

            # Check if request was successful
            if response.status_code == 201:
                print(f"File '{relative_path}' uploaded successfully.")
            else:
                print(f"Failed to upload file '{relative_path}'. Error: {response.json().get('message', '')}")

if __name__ == "__main__":
    upload_folder()
