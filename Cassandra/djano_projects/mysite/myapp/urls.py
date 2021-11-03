from django.urls import path
from myapp.views import hello

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
]


