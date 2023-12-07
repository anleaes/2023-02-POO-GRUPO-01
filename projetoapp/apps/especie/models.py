from django.db import models

# Create your models here.

class Especie(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    reino = models.TextField('Reino', max_length=100)
    reproducao = models.TextField('Reproducao', max_length=100)
    
    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
        ordering =['id']

    def __str__(self):
        return self.nome