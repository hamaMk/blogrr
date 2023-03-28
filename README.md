# Blogrr
A blog API built with Django.

## Running the API
1. Create a `.env` file for credentials using the layout outlined in the `.env.example` file
2. Update the `wsgi.py` file under ./blogrr folder

### Database credentials
To use SQLite in the dev environment, leave the settings as is.

To use PostgresSQL in the production environment, set the DATABASE_URL variable in the
`.env` file to your database settings.

### Updating the wsgi.py file
On the line
`os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogrr.settings.dev')`, 
set blogrr.settings.dev to enable the dev environment or blogrr.settings.prod for production

Alternatively set to blogrr.settings and use the DJANGO_SETTINGS_MODULE variable to 
change environments dynamically

