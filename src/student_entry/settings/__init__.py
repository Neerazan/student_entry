import os.path
from pathlib import Path

from split_settings.tools import include, optional

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


include(
    'base.py',
    'rest.py',
)

if config('DEBUG', default=True, cast=bool):  # noqa: F821 #type: ignore
    include('dev.py')
else:
    include('prod.py')