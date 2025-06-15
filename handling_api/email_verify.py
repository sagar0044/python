import requests

def fetch_verify_email():
    url="https://api.freeapi.app/api/v1/users/verify-email/{verificationToken}"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data :
        email_verify = data["data"]
        isEmailVerified = email_verify["isEmailVerified"]
        return isEmailVerified
    else:
        raise Exception ("Fetching is invalid")
def main():
    try:
        isEmailVerified = fetch_verify_email()
        print(f"EmailVerified:{isEmailVerified}")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()