import requests

def fetch_random_quote():
    url="https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        random_quote = data["data"]
        author_name = random_quote["author"]
        content_name =random_quote["content"]
        return author_name,content_name
    else:
        raise Exception ("Failed to fetch")




def main():
    try:
        author_name,content_name= fetch_random_quote()
        print(f"Author:{author_name} \nContent:{content_name}")
    except Exception as e:
        print(str(e))


if __name__ =="__main__":
    main()