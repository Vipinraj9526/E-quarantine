from django.conf.urls import url
from police import views

urlpatterns = [
    url('register/',views.register)

]