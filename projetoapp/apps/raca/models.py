from django.db import models

# Create your models here.

class Raca(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    porte = models.CharField('Porte', max_length=14)
    
    
    class Meta:
        verbose_name = 'raca'
        verbose_name_plural = 'racas'
        ordering =['id']

    def __str__(self):
        return self.nome