from django.urls import path
from .views import index
from .views import formulario_1
from .views import Mapa
from .views import Galeria
from .views import nosotros
from .views import  ListaProducto
from .views import  agregarProducto
from .views import  agregarrec
from .views import  actualizarProducto
from .views import  actualizarrec
from .views import  eliminar
from .views import  exit


from .views import  home

urlpatterns = [
    path('index.html', index, name='index' ),
    path('formulario_1.html', formulario_1, name='formulario_1' ),
    path('Mapa.html', Mapa, name='Mapa' ),
    path('Galeria.html', Galeria, name='Galeria' ),
    
    path('ListaProducto.html', ListaProducto, name='ListaProducto'),
    path('agregarProducto.html', agregarProducto, name='agregarProducto'),
    path('agregarrec', agregarrec, name='agregarrec'),
    path('eliminar/<int:id>', eliminar, name='eliminar'),
    path('actualizarProducto/<int:id>', actualizarProducto, name='actualizarProducto'),
    path('actualizarrec/<int:id>', actualizarrec, name='actualizarrec'),
    #path('actualizarProducto/actualizarrec/<int:id>', actualizarrec, name='actualizarrec'),
    path('logout/',exit, name='exit'),
    path('',home, name='home'),
]