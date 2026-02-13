import base64
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
import qrcode
from io import BytesIO


def home(request):
    if request.method == "POST":
        data = request.POST.get("link")

        img = qrcode.make(data)

        buffer = BytesIO()
        img.save(buffer, "PNG")
        buffer.seek(0)
        
        response = HttpResponse(buffer, content_type="image/png")
        response['Content-Disposition'] = 'attachment; filename="qrcode.png"'

        return response
    return render(request, 'index.html')