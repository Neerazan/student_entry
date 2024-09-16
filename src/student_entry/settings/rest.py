REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Student Entry API',
    'DESCRIPTION': 'Api for managing student entries',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
