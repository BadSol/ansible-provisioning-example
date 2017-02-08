from django.shortcuts import render
from django.views.generic import FormView
from prototype.forms import DocumentForm


class DocumentFormView(FormView):
    template_name = 'prototype/main.html'
    form_class = DocumentForm
    success_url = '/success/'
