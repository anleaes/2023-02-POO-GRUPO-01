from django.db import models

# Create your models here.

class Especie(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    reino = models.CharField('Reino', max_length=14)
    reproducao = models.CharField('reproducao', max_length=100)
    
    class Meta:
        verbose_name = 'especie'
        verbose_name_plural = 'especies'
        ordering =['id']

    def __str__(self):
        return self.nome