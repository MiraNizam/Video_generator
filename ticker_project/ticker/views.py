from django.shortcuts import render
import os
from .run_text import generate_ticker
from .models import UserInquiry
from django.http import FileResponse


def home(request):
    return render(request, "index.html")


def download_video(request):
    text = request.GET.get("text")
    if text is None:
        return render(request, "runtext.html")
    else:
        file_path = generate_ticker(text)
        UserInquiry.objects.create(input_text=text)
        response = FileResponse(open(file_path, "rb"), content_type="video/mp4")
        response['Content-Disposition'] = 'attachment; filename="video.mp4"'
        return response
