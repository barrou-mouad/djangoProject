from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/fichier/', include('reader.urls')),
    path('api/poste/', include('poste.urls')),
    path('api/secteur/', include('secteur.urls')),
    path('api/phase/', include('phase.urls')),
    path('api/tache/', include('tache.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

