from .base import *

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # or the port your React app is running on
    "http://admin.localhost:3000"
]

INSTALLED_APPS += [
    'corsheaders'
]

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]
