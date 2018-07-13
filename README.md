# MobileGameRestAPI
A REST API in django for a mobile game

## Install
1. Install python3 (`apt-get install python3`)
2. Install pip3 (`apt-get install python3-pip`)
3. Install virutalenv (`pip3 install virtualenv`)
4. Create new virtual environment (`virtualenv env`)
5. Activate the environment (`source env/bin/activate`)
6. Install requirements (`pip install -r requirements.txt`)

When you are done, use: `deactivate` to exit the virutal environment.

To update requirements just run step 6 again.

## Add new requirements
1. Activate the environment (`source env/bin/activate`)
2. Install the package using pip
3. run `pip freeze --local > requirements.txt`

# Access the API (Token auth)
## Generate a token
1. Create a user (python manage.py createsuperuser).
2. Go to localhost:8000/admin and log in with your user.
3. Go to the table "Tokens".
4. Press "Add token".
5. Choose your user an press "SAVE".

You should now see a token that look like: "02ffe8c6c2851ccc8b458e39049d6b4f94be5a25"

## Access the browsable API
1. Go to localhost:8000/admin and log in with your user.
2. Go to localhost:8000 and you should now have access to the api.

## Access the API using curl
### Scores example
Get all scores
* curl -X GET 'http://localhost:8000/scores/' -H 'Authorization: Token 02ffe8c6c2851ccc8b458e39049d6b4f94be5a25'

Add new score
* curl -X POST 'http://localhost:8000/scores/' -H 'Content-Type: application/json' -H 'Authorization: Token 02ffe8c6c2851ccc8b458e39049d6b4f94be5a25' -d '{"user": "http://localhost:8000/users/1/", "score":"1337"}'