from django.db import models

# Create your models here.

class Raca(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    porte = models.TextField('Porte', max_length=100)
    
    class Meta:
        verbose_name = 'Raca'
        verbose_name_plural = 'Racas'
        ordering =['id']

    def __str__(self):
        return self.nome
