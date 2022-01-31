from django.conf.urls import url
from user import views

urlpatterns = [
    url('view_hospital/', views.view_hospital),
    url('view_police/',views.view_police)

]