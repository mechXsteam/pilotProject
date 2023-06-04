from django.urls import path

from my_app.views import home

app_name = 'my_app'

urlpatterns = [
    path('', home, name='home'),
]
