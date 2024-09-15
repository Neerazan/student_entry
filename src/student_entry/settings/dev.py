DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # type: ignore  # noqa:F821
    }
}

INSTALLED_APPS += [  # type: ignore  # noqa:F821
    'debug_toolbar',
]

MIDDLEWARE += [  # noqa: F821  #type: ignore
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]