# restaurant-api

## Overview
Django was used to create API. I used this because of the following:
- The ModelViewSet class supports POST, GET, PUT, PATCH and DELETE
requests.
- It deals with managing success and failed responses.
- Handles displaying the PK of each model instance automatically as Model was directly serialized.

## Local Setup

1. Create Virtual env:

```
python3 -m venv env
```

1. Activate Virtual env:

```
source env/bin/activate
```

1. pip install requirements from requirements.txt

```
pip install -r requirements.txt
```

1. Run local server:

```
python manage.py runserver
```

## API
Go to **/api/restaurants/** to see the list of restaurants. This API endpoint natively supports GET and POST requests.

If you would like to send PUT, PATCH or DELETE requests, make sure to target a specific restaurant by going to 
**/api/restaurants/:pk** 

## Next Steps
1. Improvement of app's name and api endpoint depending on the new models and data that I will be persisting to the
database
1. Add user authentication
1. Add UI to be able to add restaurants through a web interface
1. Last but not least, add tests.
1. Be able to handle timezones a little better. Right now the default Time Zone is Los Angeles.
# restaurant-api
