from django.db import models

# Create your models here.

class Veterinario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    crm = models.CharField('CRM', max_length=10)
    telefone = models.CharField('Telefone', max_length=15)
    
    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        ordering =['id']

    def __str__(self):
        return self.nome