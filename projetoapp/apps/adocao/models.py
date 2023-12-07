from django.db import models
from animal.models import Animal
from tutor.models import Tutor

# Create your models here.

class Adocao(models.Model):
    data_adocao = models.DateField('Data_Adocao')
    observacao = models.TextField('Observacao', max_length=100)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Adocao'
        verbose_name_plural = 'Adocoes'
        ordering =['id']

    def __str__(self):
        return self.data_adocao
