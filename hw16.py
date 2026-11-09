# 1
import requests
BASE_URL = "https://jsonplaceholder.typicode.com/"
def get_user(user_id):
    response = requests.get(f"{BASE_URL}users/{user_id}")

    if response.status_code == 404:
        return None

    response.raise_for_status()

    return response.json()

for user_id in [1, 2, 999]:
    user = get_user(user_id)

    if user is None:
        print(f"მომხმარებელი {user_id} ვერ მოიძებნა")
    else:
        print(user["name"], "|" ,user["email"], "|", user["address"]["city"])

# 2

data = {
    "title": "ახალი პოსტი",
    "body": "ტექსტი",
    "userId": 1
}

response = requests.post(f"{BASE_URL}posts", json=data)
my_id = response.json()["id"]

print("CREATE:", response.status_code, f"id={my_id}")

response = requests.get(f"{BASE_URL}posts/{my_id}")
print("READ", my_id, ":", response.status_code)

data = {
    "id": 1,
    "title": "სრულად შეცვლილი",
    "userId": 2
}
response = requests.put(f"{BASE_URL}posts/1", json=data)
title = response.json()["title"]
print("UPDATE(PUT):", response.status_code, "title=", title)

data = {"title": "ნაწილობრივ შეცვლილი"}

response = requests.patch(f"{BASE_URL}posts/1", json=data)
title = response.json()["title"]
print("UPDATE(PATCH):", response.status_code, "title=", title)

response = requests.delete(f"{BASE_URL}posts/1")
result = response.json()
print("DELETE:", response.status_code, result)