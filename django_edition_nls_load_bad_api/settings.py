# Django settings for myproject project.

...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = [
    ...
    'myapp',  # Добавьте ваше приложение сюда
]

...

TIME_ZONE = 'Asia/Almaty'  # Установите нужную временную зону

...
