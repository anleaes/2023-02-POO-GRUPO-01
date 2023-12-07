from django.db import models
from especie.models import Especie
from raca.models import Raca
from ong.models import Ong

# Create your models here.

class Animal(models.Model):
    nome = models.CharField('Nome', max_length=50)
    data_nascimento = models.DateField('Data_Nascimento')
    peso = models.FloatField('Peso')
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
        return self.nome
