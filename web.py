import requests
from bs4 import BeautifulSoup
import certifi   # 👈 add this

url = "https://www.wikipedia.org"

try:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10,
        verify=certifi.where()   # 👈 fix SSL error
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("Headings:\n")
    for heading in soup.find_all("h1"):
        print(heading.get_text(strip=True))

    print("\nLinks:\n")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except Exception as e:
    print("Error:", e)