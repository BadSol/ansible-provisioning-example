import pytest

from django.urls import reverse


def test_document_form_view(client):  # Use request factory -DR
    response = client.get(reverse('pgx_prototype:document_form'))
    assert(response.status_code == 200)


def test_correct_form_input_labels_in_document_form_view(client):
    labels = ['Podmiot zobowiązany',
              'Opublikowane dane osobowe',
              'Nazwa serwisu',
              'Link do opublikowanych danych',
              'Data']

    response = client.get(reverse('pgx_prototype:document_form'))

    assert(all(label in str(response.context.get('form'))) for label in labels)
