from django.urls import path
from .views import index, login_view

app_name = 'accounts'
urlpatterns = [
  path('', index, name='index'),
  path('login/', login_view, name='login'),
]