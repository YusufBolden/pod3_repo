from django.urls import path
from myapp.views import hello, goodbye


urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    # myapp/<str:name>
    path('<str:name>', hello, name='hello_name'),
    path('goodbye/django', goodbye,name='goodbye') 
]