from django.urls import path
from helloapp.views import hello, goodbye

urlpatterns = [
    # helloapp/
    path('', hello, name='hello'),
    # helloapp/<str:name>
    path('<str:name>', hello, name='hello_name'),
    # goodbye/django
    path('goodbye/django', goodbye, name='goodbye_name'),
    # goodbye/django/<str:name>
    path('goodbye/django/<str:name>', goodbye, name='goodbye_name'),
]
