from django.shortcuts import render
from .stam_model import main


def home(request):
    json_res = main()

    return render(request, 'main/home.html', {'json_res': str(json_res)})
