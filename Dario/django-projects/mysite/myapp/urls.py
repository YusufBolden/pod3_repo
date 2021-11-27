from django.urls import path
from myapp.views import hello, goodbye

urlpatterns = [
    # myapp
    path('', hello, name='hello'),
    path('hello/<str:name>', hello, name='hello_name'),
    path('goodbye/<str:name>', goodbye, name='goodbye_name'),
    path('goodbye', goodbye, name='goodbye')
]