from django.db import models
from django.db.models import F

# Create your models here.

class Usuario(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['primeiro_nome'], name=["primeiro_nome_usuario"]),
            models.Index(fields=['ultimo_nome'], name=["ultimo_nome_usuario"]),
            models.Index(F('nota1') + F('nota2'), name= "calc_nota"),
            
        ]

    def __str__(self) -> str:
        return self.primeiro_nome