# Blogrr
A blog API built with Django.

## Setting up
1. Create a `.env` file for credentials using the layout outlined in the `.env.example` file
2. Update the `wsgi.py` file under ./blogrr folder

### Database credentials
To use SQLite in the dev environment, leave the settings as is.

To use PostgresSQL in the production environment, set the DATABASE_URL variable in the
`.env` file to your database settings.

### Updating the wsgi.py file
On the line
`os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogrr.settings')`, 
set `blogrr.settings.dev` to enable the dev environment or `blogrr.settings.prod` for production

Alternatively set to `blogrr.settings` and set the `DJANGO_SETTINGS_MODULE` variable on your environment to 
change environments dynamically

### Updating the manage.py file
By default, the `DJANGO_SETTINGS_MODULE` variable is set to `blogrr.settings.dev`, which
activate the development settings file.
Change `blogrr.settings.dev` to `blogrr.settings.prod` for production settings 

Alternatively set to `blogrr.settings` and set the `DJANGO_SETTINGS_MODULE` variable on your environment to 
change environments dynamically



## Running the API
1. Make migrations: `python manage.py makemigrations`  
2. Migrate: `python manage.py migrate`  
3. Create Admin user: `python manage.py createsuperuser` and follow instructions  
4. Run: `python manage.py runserver`


#API DOCS
The API provides the following endpoints
1. api/posts
2. api/users
3. api/tags

##Posts
###List posts  
curl --request GET --url 'http://127.0.0.1:8000/api/posts'

###Search posts  
curl --request GET \
--url 'http://127.0.0.1:8000/api/posts?search=an%20epic'

###Filter posts
by Owner  
curl --request GET \
  --url 'http://127.0.0.1:8000/api/posts?owner=1'


##Users
###List users
curl --request GET \
  --url http://127.0.0.1:8000/api/users \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgwMTg0ODI3LCJpYXQiOjE2ODAxODQ1MjcsImp0aSI6ImNlNGI5ZDg0YjhhMTQ4OWI5NDdhYzNkODM4YmM5MTE5IiwidXNlcl9pZCI6NH0.pIA2G0SSOrd7-exDFRgyxVE136aaLSnDa4KpJpJxuP8'


##Tags
###List Tags
curl --request GET \
  --url http://127.0.0.1:8000/api/tags


##Admin Dashboard
To access the dashboard, open your browser and go to http://127.0.0.1:8000/admin

The dashboard has the following functions
1. Manage users
2. Manage posts
3. Manage Tags
4. Upload images


