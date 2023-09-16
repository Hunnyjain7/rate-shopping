# rate-shopping

Rate Shopping API's for Admin and Client Interfaces Developed in Django REST Framework.

## Technology Stack:
* Python 3.10.6
* Django 4.2.5.

## Steps to Run the API's.
1. Cline the repo
    ```git clone https://github.com/Hunnyjain7/rate-shopping```
2. Checkout main branch
    ```git checkout main```
3. Create Virtual Environment.\
    ```pip install virtualenv``` \
    ```virtualenv venv```\
    Activate Environment:\
    For Windows: ```venv\Scripts\actiavte```\
    For Linux: ```source venv/bin/activate```
4. Install Requirements ```pip install -r requirements.txt```
5. copy `.env.example` file and rename it to `.env` and initialize all the variables in the file.
    for eg: `ENV=local`,`DEBUG=true` and Postgres DB credentials.
6. Run Migrations ```python manage.py makemigrations```
7. Then Migrate ```python manage.py migrate```
8. Run the seed file by below command to dump the required Data in Database.\
    ```python manage.py seed --mode=create_superuser```
9. Run the project ```python manage.py runserver```
