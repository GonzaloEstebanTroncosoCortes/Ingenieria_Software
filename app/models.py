from django.db import models

# Create your models here.
class fotografia(models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=40)
    archivo_fotografia=models.ImageField(upload_to='fotografia', null=True)
    Cantidad_alumno=models.IntegerField(null=True)