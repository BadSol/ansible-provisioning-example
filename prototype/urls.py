from django.conf.urls import url
from .views import DocumentFormView


app_name = 'pgx_prototype'
urlpatterns = [
    url(r'^$', DocumentFormView.as_view(), name='document_form'),
]
