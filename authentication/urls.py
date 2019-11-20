from django.conf.urls import url
from rest_framework_simplejwt.views import (TokenRefreshView,)
import views


urlpatterns = [

    url(r'^token/$', views.UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),

]
