# presentation_app/views.py
import os
from django.http import HttpResponse
from django.shortcuts import render
from .models import Slide

def presentation(request):
    slides = Slide.objects.order_by('order')
    return render(request, 'presentation.html', {'slides': slides})

def presentation2(request):
    return render(request, 'all_slides.html')

def slide(request, slide_number):
    slide_path = os.path.join('templates','slides', f'slide{slide_number}.html')
    try:
        with open(slide_path, 'r') as file:
            content = file.read()
        return HttpResponse(content)
    except FileNotFoundError:
        return HttpResponse(f"Slide {slide_number} not found.", status=404)

def presentation3(request):
    return render(request, 'all.html')

def slidex(request, slide_number):
    return render(request, f'slides/slide{slide_number}.html')