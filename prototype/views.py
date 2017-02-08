from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from prototype.forms import DocumentForm
from prototype.utils import generate_fdf_from_fields


class DocumentFormView(FormView):
    template_name = 'prototype/main.html'
    form_class = DocumentForm
    success_url = '/success/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DocumentSuccessView(TemplateView):
    template_name = 'prototype/success.html'
