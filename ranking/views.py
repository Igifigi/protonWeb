from typing import Dict
from django.shortcuts import render

# Create your views here.

def test(request):
    context = {
        'test': 'loldziaua'
    }
    return render(request, context=context, template_name='test.html')