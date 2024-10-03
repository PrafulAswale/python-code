import requests

def get_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"

    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        allData = data["data"]
        print(allData["content"])


def main():
    print("loading...")

    try:
        get_random_jokes()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
