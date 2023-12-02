from django.db import models

# Create your models here.

class Tutor(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereco', max_length=100)
    telefone = models.CharField('Telefone', max_length=14)
    email = models.TextField('Email', max_length=100)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =['id']

    def __str__(self):
        return self.name