DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': config('DATABASE_USER'),  # noqa: F821 # type: ignore
        'PASSWORD': config('DATABASE_PASSWORD'),  # noqa: F821 # type: ignore
        'NAME': config('DATABASE_NAME'),  # noqa: F821 # type: ignore
        'HOST': config('DATABASE_HOST'),  # noqa: F821 # type: ignore
        'PORT': config('DATABASE_PORT'),  # noqa: F821 # type: ignore
    }
}
