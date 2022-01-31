from django.conf.urls import url
from complaint_table import views
urlpatterns=[
    url('view/',views.view),
    url('reply/',views.reply)

]