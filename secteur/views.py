from .serializer import SecteurSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .models import Secteurs

@api_view(['GET'])
def upload(request,id):
    print(id)
    snippet = Secteurs.objects.get(pk=id)
    print("------ after first line ---------")
    serialezer=SecteurSerializer(snippet,many=False).data
    print("------ after second line ---------")
    return JsonResponse(serialezer,safe=False)

@api_view(['GET'])
def all(request):
    secteur = Secteurs.objects.all()
    serialezer=SecteurSerializer(secteur,many=True).data
    return JsonResponse(serialezer,safe=False)

@api_view(['DELETE'])
def delete(request,id):
     secteur = Secteurs.objects.get(pk=id)
     secteur.delete()
     return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
