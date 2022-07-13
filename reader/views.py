from django.shortcuts import render
from django.db import models
import json
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import default_storage
# Create your views here.
def store():
    models.FieldField(blank=True, null=True, upload_to=upload_path)

def read_pdf(name):
    import camelot.io as camelot
    tables = camelot.read_pdf('C:/Users/Mouad/Documents/Stage/Application/django_back/media/'+str(name))
    print(tables)
    return HttpResponse(tables[0].df[5][5])

@api_view(['POST'])
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_name = default_storage.save(uploaded_file.name, uploaded_file)
        import camelot.io as camelot
        import pandas as pd
        tables = camelot.read_pdf('C:/Users/Mouad/Documents/Stage/Application/django_back/media/'+str(uploaded_file.name), encoding='utf-8')
        print(tables[0].df)
        df = pd.DataFrame(tables[0].df,columns=tables[0].df[0])
        print(tables[0].df[0][5])
        print("-----------------")
        tables[0].df.drop([0,len(tables[0].df)-1,len(tables[0].df)-2,len(tables[0].df)-3], axis=0, inplace=True)
        tables[0].df.drop([0,len(tables[0].df.iloc[0,])-1], axis=1, inplace=True)
        result =tables[0].df.to_json(orient = 'values',force_ascii=False)
        print(result)
        return HttpResponse(result)
        