from django.db import models

class Colaboradores(models.Model):
    id_colaborador = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField()

    def __str__(self):
        return self.nome