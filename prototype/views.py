from django.shortcuts import render, redirect
from prototype.forms import DocumentForm
from prototype.utils import PgxPrototypeDocument
from django.views.generic import TemplateView
from django.http import HttpResponse


def document_form_view(request):
    if request.method == "GET":
        form = DocumentForm()
        return render(request, 'prototype/main.html', {"form": form})

    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            prototype_document = PgxPrototypeDocument(
                subject=form_data['subject'],
                published_data=form_data['published_data'],
                service_name=form_data['service_name'],
                published_data_url_address=form_data['published_data_url_address'],
                date=form_data['date'])

            prototype_document.generate_and_save_pdf_to_media('this_file_is_generated_from_view')

            return render(request, 'prototype/success.html', {"test": 'test'})
        else:
            return redirect('pgx_prototype:document_form')


# def some_view(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="media.pdf_outputs.this_file_is_generated_from_view.pdf"'
#     return response


class PdfSuccessView(TemplateView):  # todo: For now this view, always allows downloading last generated pdf
    template_name = 'prototype/success.html'


