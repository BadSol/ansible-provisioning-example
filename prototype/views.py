from django.shortcuts import render, redirect
from prototype.forms import DocumentForm
from prototype.utils import PgxPrototypeDocument
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

            pdf_output_name = 'pgx_prototype'

            prototype_document.generate_and_save_pdf_to_media(pdf_output_name)

            with open('/vagrant/media/pdf_outputs/{pdf_file_name}.pdf'.format(pdf_file_name=pdf_output_name),
                      'rb') as pdf:

                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="{pdf_file_name}.pdf'.\
                    format(pdf_file_name=pdf_output_name)

                return response
        else:
            return redirect('pgx_prototype:document_form')


