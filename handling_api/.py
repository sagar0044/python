import requests 

def fetch_my_profile():
    url = "https://api.freeapi.app/api/v1/ecommerce/profile"
    response = requests.get(url)
    data = response.json()

    if data["success"] and  "data"in data :
        profile_data = data["data"]
        first_name_user = profile_data["firstName"]
        last_name_user = profile_data["lastName"]
        phone_user = profile_data["phoneNumber"]
        return first_name_user,last_name_user,phone_user
    else:
        raise Exception ("Failed to fetch")
def main():
    try:
      first_name_user,last_name_user,phone_user = fetch_my_profile()
      print(f"FirstName:{first_name_user} \nLastName:{last_name_user} \nPhoneNumber:{phone_user}")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()