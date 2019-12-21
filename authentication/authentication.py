#install
pip install djangorestframework_simplejwt

#add in settngs
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

#create folder authorization insert staticfiles

#main url
url(r'^api/v1/auth/', include('api.v1.authentication.urls',namespace="api_v1_authentication")),

#urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),


]
