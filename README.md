# GharChalo-Task : Pizza API with authentication

An online Pizza ordering API where users can signup, log in, and order different types of Pizzas.

Database is able to store information about Pizza, following are the details :

- A Pizza can be of multiple types : Regular or Square
- A Pizza can be of multiple sizes: Small, Medium, Large, etc. (These are just examples; the user should be allowed to add any other size at any point of time)
- A Pizza can consist of many toppings out of the following (Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno etc.), the choice of toppings should not be limited to the ones mentioned above, the user should be allowed to add any type of topping at any point of time)

## Features

### Pizza API

- An API endpoint to create regular pizza and a square pizza.
- An API endpoint which lists the information about all the stored pizza, the response of this should also contain the information about the toppings, size and type of Pizza.
- Filtering the list of pizza returned by the API based on Size & Type of Pizza.
- An API endpoint that allows the user to edit or delete any pizza from the database.

### Authentication API

- On registration the following things will be taken care of
  - Email will be validated on the basis of - Cuss words in email,Company emails should not work.
  - Username will be validated on the basis of - Cuss words in the username , more than 6 words in the username.
  - Password should follow the One capital, one special character and One number way, and must have length greater than 8.

## Tech Stack

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img 
src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/>
<img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>
<img src="https://img.shields.io/badge/mysql-0B96B2?style=for-the-badge&logo=myql&logoColor=white"/>

- **Backend**: Django, Django Rest Framework
- **IDE**: VS Code
- **API Testing**: Postman
- **Version Control**: Git and GitHub
- **Database**: MySQL

### Backend Setup Instructions

## Setup Instructions

First make sure that you have the following installed.

- Python 3 and virtualenv

Now do the following to setup project

```bash
# assuming that the project is already cloned.

cd src

# one time
virtualenv -p $(which python3) pyenv

source pyenv/bin/activate

# one time or whenever any new package is added.
pip install -r requirements.txt

# update settings
cp src/pizza/settings/local.sample.env src/pizza/settings/local.env

# generate a secret key or skip(has a default value) and then replace the value of `SECRET_KEY` in environment file(here local.env)
./scripts/generate_secret_key.sh

# update relevant variables in environment file

# run migrate
cd src
python manage.py migrate
```

To access webserver, run the following command

```bash
cd src
python manage.py runserver
```

## Demo Credentials

**Username:** admin
**Email:** admin@gmail.com
**Password:** pass

## Endpoints

### Pizza API

1. **Get Request:**

   `end-point: pizzas/api/pizza/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found

   `end-point: pizzas/api/size/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found
   `end-point: pizzas/api/topping/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found

   `end-point: pizzas/api/pizza/id`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found

2. **Post Request:**

   `end-point: pizzas/api/pizza/`

   Accepted Response : status 201 Created

   Error Response : {"error": "Invalid choice"} status 400 Bad Request

   `end-point: pizzas/api/size/`

   Accepted Response : status 201 Created

   Error Response : {"error": "Invalid choice"} status 400 Bad Request

   `end-point: pizzas/api/topping/`

   Accepted Response : status 201 Created

   Error Response : {"error": "Invalid choice"} status 400 Bad Request

3. **Patch Request:**

   `end-point: pizzas/api/pizza/id`

   Accepted Response : status 200 OK

   Error Response : {"error": "Invalid choice"} status 400 Bad Request

4. **Delete Request:**

   `end-point: pizzas/api/pizza/id`

   Accepted Response : status 204 No Content

   Error Response : status 404 Not Found

### Authentication API

1. **Get Request:**

   `end-point: accounts/api/token/refresh/`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found

   `end-point: accounts/api/users/<username>`

   Accepted Response : status 200 OK

   Error Response : status 404 Not Found

2. **Post Request:**

   `end-point: accounts/api/register/`

   Accepted Response : status 201 Created

   Error Response : {"error": "Invalid choice"} status 400 Bad Request

   `end-point: accounts/api/login/`

   Accepted Response : status 201 Created

   Error Response : {"error": "Invalid choice"} status 400 Bad Request

# License :memo:

This project follows the [MIT License](https://choosealicense.com/licenses/mit/).
