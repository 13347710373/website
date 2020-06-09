from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def run_page(request):
    """run_page"""
    return JsonResponse({"response":"ok"})
