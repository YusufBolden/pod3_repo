from django.urls import path
from django.urls.resolvers import URLPattern
from myapp.views import hello
from myapp.views import goodbye

urlpatterns = [
     path('', hello, name='hello'),
     path('<str:name>', hello, name = 'hello_name'),
     path('goodbye/django',goodbye, name = 'goodbye_name')
 ]