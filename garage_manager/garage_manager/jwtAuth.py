import requests

# Below enter the username and password of the superuser you created
# Run in terminal python jwtAuth.py
# This will send back both the Refresh and Access tokens. 

url = "http://localhost:8000/api/token/"

payload = "username=ENTERUSERNAMEHERE&password=ENTERPASSWORDHERE"
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
