from django.shortcuts import render, redirect
from prototype.forms import DocumentForm
from prototype.utils import generate_fdf_from_fields



def document_form_view(request):
    if request.method == "GET":
        form = DocumentForm()
        return render(request, 'prototype/main.html', {"form": form})

    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            field_list = form_data.items()
            fdf = generate_fdf_from_fields(field_list)
            string_fdf = fdf.decode("utf-8", "ignore")

            return render(request, 'prototype/success.html', {"test": string_fdf})
        else:
            return redirect('pgx_prototype:document_form')
