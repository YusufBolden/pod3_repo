from django.urls import path
from helloapp.views import hello, goodbye

urlpatterns = [
    # helloapp/
    path('', hello, name='hello'),
    path('<str:name>', hello, name='hello_name'),
    path('goodbye/django', goodbye, name='goodbye_name')
]