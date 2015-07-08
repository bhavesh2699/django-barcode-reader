from django.shortcuts import render
from django.http import HttpResponse
import os
import dbr

# Create your views here.
def home(request):
    return render(request, 'index.htm', {'what':'Online Barcode Reader with Django'})

def upload(request):
    if request.method == 'POST':
        uploadedFile = handle_uploaded_file(request.FILES['RemoteFile'], str(request.FILES['RemoteFile']))
        results = dbr.decodeFile(uploadedFile)
        return HttpResponse(results)

    return HttpResponse("Failed")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    filePath = 'upload/' + filename

    with open(filePath, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return filePath
