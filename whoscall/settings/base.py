import os

DATABASES = {
    'default': {
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': 'root',
        'PASSWORD': os.environ.get('MYSQL_ROOT_PASSWORD'),
        'HOST': os.environ.get('MYSQL_SERVICE'),
        'PORT': 3306
    }
}
