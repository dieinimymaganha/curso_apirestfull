from django.db import models


class PontoTuristicos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField()
        
    def __str__(self):
        return self.nome