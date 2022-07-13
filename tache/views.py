from .serializer import TacheSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .models import Taches

from rest_framework import status
@api_view(['GET'])
def upload(request,id):
    print(id)
    snippet = Phases.objects.get(pk=id)
    print("------ after first line ---------")
    serialezer=TacheSerializer(snippet,many=False).data
    print("------ after second line ---------")
    return JsonResponse(serialezer,safe=False)

@api_view(['GET'])
def get(request,id):
    print(id)
    snippet = Taches.objects.filter(secteur__id=id)
    print("------ after first line ---------")
    serialezer=TacheSerializer(snippet,many=True).data
    print("------ after second line ---------")
    return JsonResponse(serialezer,safe=False)
    
@api_view(['GET'])
def all(request):
    posts = Taches.objects.all()
    serialezer=TacheSerializer(posts,many=True).data
    return JsonResponse(serialezer,safe=False)

@api_view(['DELETE'])
def delete(request,id):
     posts = Taches.objects.get(pk=id)
     posts.delete()
     return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def save(request):    
    if request.method == 'POST':
            data = {
            'code': request.data.get('code') , 
            'description':request.data.get('description'), 
            'secteur': 1
             }
            tutorial_serializer = TacheSerializer(data=data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
