from .base import * 
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default = "sApz-P6Nkb_IWrDed9Mi84tGTBFbrp9xBi-S8vzPdVyrDWjtit4",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]