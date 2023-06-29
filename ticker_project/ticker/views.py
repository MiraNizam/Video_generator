from django.shortcuts import render

from .run_text import generate_ticker
from .models import UserInquiry


# Create your views here.
def home(request):
    return render(request, "index.html")


def runtext(request):
    text = request.GET.get("text")
    print(type(text))
    if text is None:
        return render(request, "runtext.html")
    else:
        UserInquiry.objects.create(input_text = text)
        generate_ticker(text)
        return render(request, "runtext.html")
