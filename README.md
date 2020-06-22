# bixly_test / Garage_manager

This application is built using Django REST framework.

Authentication is using JSON Web Token specifically the Simple JWT library.

The application also utilizes Django Admin.

It is used to store different types of vehicles (Cars, Trucks, Boats) inside of a "Garage"

---
## Start Up
- After cloning the repository cd in bixly_test folder
- Open pipfile and change python_version to the version you have on your computer.
- Run `pipenv shell`
- Run `pip3 install -r requirements.txt`
- Make migrations `python manage.py makemigrations` and migrate `python manage.py migrate`
- Create a Super User `python manage.py createsuperuser`
- Run ther server `python manage.py runserver`
- Open Browser to http://127.0.0.1:8000/

---

## Authentication
> Depending on your personal prefrence (Insomnia, Postman, ect) you will need to run requests to gain auth access.
> I personally used Insomnia for my HTTP Requests.

### Step One
- Create a **POST** request
- Use this url: **http://localhost:8000/api/token/**
- Change body to **Form URL Encoded**
- Create two new value pairs **username** and **password** their value will be filled in with your superuser info
- Hit send. This will return something like this:
```
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU5Mjg3MzQ4MSwianRpIjoiYzBjOWJkNjhhNzMzNGE1Y2I5ZjE5Y2YyYTk3OGQxNTQiLCJ1c2VyX2lkIjoxfQ.MxE0vCMz-7LqhXMknok83ezvlnJ_pbUT_JF0_FcBOhk",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkyNzg3MzgxLCJqdGkiOiJiNjUxOGY5MjliZDg0MTk1YjBjZmQwN2VhNGVlYmZjNSIsInVzZXJfaWQiOjF9.XFAJlj47XytDOj-kO0DzckfpVuq1_W8JRldwHDzS9aM"
}
```
---

### Step Two (LIST)
- Create a **GET** request
- use any of these routes:
```
http://127.0.0.1:8000/api/trucks/
http://127.0.0.1:8000/api/cars/
http://127.0.0.1:8000/api/boats/
```
- Change Auth to **Bearer Token** you will then paste your access token into the **TOKEN** field. 
- Hit send and it should return any vehicles listed under that specific route. Using this same token you can now go on to test LIST, READ, CREATE, UPDATE, and DELETE for Cars Trucks and Boats using the above urls in the requests.

### Get Refresh Token
If you find that your origina access token has expired you will need to run a **POST** request with the refresh token to get a new access token. 
- Use this URL: **http://localhost:8000/api/token/refresh/**
- Under form  use **Form URL Encoded** create a value pair with **refresh** and the **refresh token**
- Send it to get a new access token.

---

### Selection 
With this application Choices have been created for some of the data that needs to be entered. To prevent errors and make testing the requests easier it is reccomended in your browser to go to the django admin url **http://127.0.0.1:8000/admin** By utilizing this pathway you can view the parameters that each vehicle needs to be created. Note that you can also perform all CRUD functions through the Django admin as well. 

---

### POST (CREATE)
- Using any of the urls for cars, trucks, boats (above) you will create a POST request
- Change the body to JSON. and add in the required JSON formatted information.
- below are examples of the different queries feel free to use them and change the information.

``` 
TRUCK JSON QUERY

{
  "vin": "12365478985216894",
  "current_mileage": 15000,
  "year": 2010,
  "make": "CHEVROLET",
  "model": "Avalanche",
  "seats": "5",
  "bed_length": "6ft",
  "color": "SILVER",
  "service_interval": "6 Months",
  "next_service": "2021-10-18"
}

CAR JSON QUERY

  {
    "vin": "78978978946544546",
    "current_mileage": 4587,
    "year": 2004,
    "make": "DODGE",
    "model": "Avenger",
    "seats": "5",
    "color": "RED",
    "service_interval": "6 Months",
    "next_service": "2020-07-10"
  }
  
BOAT JSON QUERY

 {
    "hin": "hwu125987645",
    "current_hours": 600,
    "year": 2002,
    "make": "NORTHWEST BOATS",
    "model": "22 SIGNATURE",
    "length": "18FT",
    "width": "70IN",
    "service_interval": "12 Months",
    "next_service": "2021-05-21"
  }
  
```
---

### PUT (UPDATE) / DELETE (DELETE) / GET (READ)

To get a specific vehicles information and either view, change, or delete it you will do the following

- Change the method to whichever you are wanting to perform.
- Paste in one of the Urls from above for Cars, Trucks, Boats
- At the end of that url paste in the specific items id you are wanting to work with end end with a /

```
EXAMPLE

http://127.0.0.1:8000/api/trucks/eaa362a7-b343-4d74-99f0-7e99db3a6403/
```
- Change Auth to Bearer Token and add in your access token

**PUT (UPDATE)** 

- Change the body format to JSON and paste in the query for the vehicle you want to alter (examples above).
- Change the fields you want to update then hit send.  


**DELETE (DELETE)**

- Change the method to **DELETE** and add the proper url with id at the end
- Change Auth to **Bearer Token** again and paste in your access token.
- Hit send.

**GET (READ)**

- Change the method to **GET** and add the proper url with id at the end
- Change Auth to **Bearer Token** again and paste in your access token.
- Hit send.
