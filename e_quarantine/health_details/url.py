from  django.conf.urls import url
from health_details import  views
urlpatterns=[
    url('view_healt/',views.view_health)
]