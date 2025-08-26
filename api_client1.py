import requests

def fetch_and_display_users(num_users):
   
    url = "https://jsonplaceholder.typicode.com/users"

    try:
       
        response = requests.get(url)

       
        if response.status_code != 200:
            print(f"Error: Received non-200 HTTP status code {response.status_code}")
            return None

      
        users = response.json()

        
        if not isinstance(users, list):
            print("Error: Unexpected JSON structure. Expected a list of users.")
            return None

       
        for i in range(min(num_users, len(users))):  
            user = users[i]
            try:
                name = user.get("name", "N/A")
                email = user.get("email", "N/A")
                city = user.get("address", {}).get("city", "N/A")
                print(f"User {i+1}:")
                print(f"  Name: {name}")
                print(f"  Email: {email}")
                print(f"  City: {city}")
                print("-" * 40)

            except KeyError as e:
                print(f"Error: Missing expected key {e} in user data.")
                return None

    except requests.exceptions.RequestException as e:
        
        print(f"Error: An error occurred while making the request: {e}")
        return None


if __name__ == "__main__":
    print("Fetching 3 users...")
    fetch_and_display_users(3)

    print("\nFetching 15 users (out-of-bounds test)...")
    fetch_and_display_users(15)
