from django.conf.urls import url
from . import views


app_name = 'pgx'
urlpatterns = [
    url(r'^$', views.prototype_view, name='document_form'),
]