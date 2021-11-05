from django.urls import path
from myapp.views import hello, goodbye


urlpatterns = [
    path('', hello, name='hello'),
    path('<str:name>', hello, name='hello_name'),
    path('goodbye/django', goodbye, name='goodbye'),
]