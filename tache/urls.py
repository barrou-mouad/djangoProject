from django.urls import path
from . import views
urlpatterns=[
path('<int:id>', views.upload, name='upload'),
path('', views.all, name='all'),
path('delete', views.delete, name='delete'),
path('save', views.save, name='save'),
path('phase/<int:id>', views.get, name='get'),
]