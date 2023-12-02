from django.db import models

# Create your models here.
class Nota(models.Model):
    titulo = models.CharField(max_length=30)
    nota = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo