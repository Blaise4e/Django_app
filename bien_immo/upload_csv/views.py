from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import pathlib

ROOT = ROOT = os.path.dirname(os.path.dirname(__file__))

# Create your views here.
def index(request):
    return TemplateResponse(request, 'index.html')

def test(request):
    return TemplateResponse(request, 'test.html')



def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(type(form))
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            src = r".csv"
            file = pathlib.Path(ROOT).glob(src)
            if file !=0:
                df = pd.read_csv(file, delimiter=',')
            #engine = create_engine('postgresql://utilisateur:root@localhost:5432/postgres')
            conn = psycopg2.connect(
                host="localhost",
                database="test",
                user="utilisateur",
                password="root")
            cur = conn.cursor()
            with open(form, 'r') as f:
               next(f) # Skip the header row.
               cur.copy_from(f, 'lotissement', sep=',', null='')
            conn.commit()
            cur.close()
            conn.close()
            context = {'msg' : '<span style="color: green;">File successfully uploaded</span>'}
            return TemplateResponse(request, 'upload.html', context)
    else:
        form = UploadFileForm()
        return TemplateResponse(request, 'index.html')

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


"""
def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        #file = fss.save(upload.name, upload)
        file = fss.save(, upload.name)
        file_url = fss.url(file)
        return TemplateResponse(request, 'upload.html', {'file_url': file_url})
    return TemplateResponse(request, 'upload.html')


def upload(request):
  if request.method == "POST":  
    if request.files:
            
            csv = request.files["csv"]
            csv = csv.open(csv)
            print("it's good")
            
            image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
            full_filename = os.path.join(app.config['IMAGE_UPLOADS'], image.filename)
            filename = secure_filename(image.filename)
            pred = predict_img(image, model)
            #os.remove(full_filename)
            
            with open(csv) as f:
                reader = csv.reader(f)
                for row in reader:
                    _, created = Teacher.objects.get_or_create(
                    first_name=row[0],
                    last_name=row[1],
                    middle_name=row[2],
                )    
                


    return TemplateResponse(request, 'upload.html')
     """