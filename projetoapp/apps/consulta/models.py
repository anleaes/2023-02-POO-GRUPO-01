from django.db import models
from animal.models import Animal
from veterinario.models import Veterinario

# Create your models here.

class Consulta(models.Model):
    data_consulta = models.DateField('Data_Consulta')
    anamnese = models.TextField('Anamnese', max_length=100)
    medicamentos = models.TextField('Medicamentos', max_length=100)
    vacinas = models.TextField('Vacinas', max_length=100)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        ordering =['id']

    def __str__(self):
        return self.data_consulta
