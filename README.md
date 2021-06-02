 # Authentication

## Install pakages
```
pip install djangorestframework
pip install djangorestframework-simplejwt
```
## settings.py
```
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
  'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
  'ROTATE_REFRESH_TOKENS': True,
  'BLACKLIST_AFTER_ROTATION': True,

  'ALGORITHM': 'HS256',
  'SIGNING_KEY': SECRET_KEY,
  'VERIFYING_KEY': None,

  'AUTH_HEADER_TYPES': ('Bearer',),
  'USER_ID_FIELD': 'id',
  'USER_ID_CLAIM': 'user_id',

  'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
  'TOKEN_TYPE_CLAIM': 'token_type',

  'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
  'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
  'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
```