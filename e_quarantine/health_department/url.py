from django.conf.urls import url
from health_department import views
urlpatterns=[
    url('register/',views.register)

]