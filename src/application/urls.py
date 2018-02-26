from django.conf.urls import url
from application import views

urlpatterns = [
    url(r'^token$', views.create_token, name='create_token'),
    url(r'^token/verify$', views.verify_token, name="verify_token"),
]
