from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, 
    TokenRefreshView, 
) 


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='...'), # views가 이미 있기 때문에, views.py가 굳이 필요하지 않음
    path('api/token/refresh/', TokenRefreshView.as_view(), name='...'), 
]
