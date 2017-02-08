from django.conf.urls import url
from .views import DocumentFormView, DocumentSuccessView


app_name = 'pgx_prototype'
urlpatterns = [
    url(r'^$', DocumentFormView.as_view(), name='document_form'),
    url(r'^success/$', DocumentSuccessView.as_view(), name='success'),
]
