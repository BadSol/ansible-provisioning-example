from django.shortcuts import render


def prototype_view(request):
    context = {'objects': 'test'}
    return render(request, 'prototype/main.html', context)
