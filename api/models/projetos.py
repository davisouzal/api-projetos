from django.db import models
from api.models.financiadores import Financiadores
from api.models.areas_tecnologicas import AreasTecnologicas
from api.models.colaboradores import Colaboradores

class Projetos(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    projeto = models.CharField(max_length=100)
    id_financiador = models.ForeignKey(Financiadores, on_delete=models.CASCADE)
    id_area_tecnologica = models.ForeignKey(AreasTecnologicas, on_delete=models.CASCADE)
    coordenador = models.CharField(max_length=100)
    ativo = models.BooleanField()
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_membros = models.IntegerField()
    equipe = models.ManyToManyField(Colaboradores)

    def __str__(self):
        return self.projeto