# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import Question
from .models import Gallery


def home(request):
    all_gallery = Gallery.objects.order_by('image_info')
    return render(request, 'home.html', {'all_gallery': all_gallery})


def answer(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

