import requests
import random
import string

def generate_random_filename(extension, length=16):
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return f"{random_string}.{extension}"


url = "https://....presentation.mp4"
headers = {
    "Referer": "strict-origin-when-cross-origin",
}

cookies = {
}

response = requests.get(url, headers=headers, cookies=cookies)

if response.status_code == 200:
    filename = generate_random_filename("mp4")
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Video downloaded {filename}!")
else:
    print("Error:", response.status_code)
