from django.conf.urls import url
from .views import document_form_view, PdfSuccessView  # , some_view


app_name = 'pgx_prototype'
urlpatterns = [
    url(r'^$', document_form_view, name='document_form'),
    url(r'^success$', PdfSuccessView.as_view(), name='success'),
    # url(r'^success$', some_view, name='success'),
]
