import requests


def get_random_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        booksData = data["data"]
        title = booksData['volumeInfo']['title']
        authors = booksData['volumeInfo']['authors']
        publishedDate = booksData['volumeInfo']['publishedDate']

        return title, authors, publishedDate
    else:
        raise Exception("Failed to get book data!")


def main():
    print("loading...")

    try:
       title, authors, publishedDate = get_random_book()
       print(f"Title: {title}")
       print(f"Authors: {authors}")
       print(f"published Date: {publishedDate}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
