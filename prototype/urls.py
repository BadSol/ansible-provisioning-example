from django.conf.urls import url
from .views import document_form_view


app_name = 'pgx_prototype'
urlpatterns = [
    url(r'^$', document_form_view, name='document_form'),
]
