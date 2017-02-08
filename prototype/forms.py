from django import forms
import datetime


class DocumentForm(forms.Form):
    subject = forms.CharField(label="Podmiot zobowiązany")
    published_data = forms.CharField(label="Opublikowane dane osobowe")
    service_name = forms.CharField(label="Nazwa serwisu")
    published_data_url_address = forms.CharField(label="Link do opublikowanych danych")
    date = forms.DateField(initial=datetime.date.today, label="Data")



