from .serializer import PrixSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .models import Prixs

@api_view(['GET'])
def upload(request,id):
    print(id)
    snippet = Prixs.objects.get(pk=id)
    print("------ after first line ---------")
    serialezer=PrixSerializer(snippet,many=False).data
    print("------ after second line ---------")
    return JsonResponse(serialezer,safe=False)

@api_view(['GET'])
def all(request):
    posts = Prixs.objects.all()
    serialezer=PrixSerializer(posts,many=True).data
    return JsonResponse(serialezer,safe=False)

@api_view(['DELETE'])
def delete(request,id):
     posts = Prixs.objects.get(pk=id)
     posts.delete()
     return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
