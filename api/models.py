from django.db import models

class Financiadores(models.Model):
    id = models.AutoField(primary_key=True)
    financiador = models.CharField(max_length=100)

    def __str__(self):
        return self.financiador
    
class AreasTecnologicas(models.Model):
    id = models.AutoField(primary_key=True)
    area_tecnologica = models.CharField(max_length=100)

    def __str__(self):
        return self.area_tecnologica
    
class Colaboradores(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    dt_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Projetos(models.Model):
    id = models.AutoField(primary_key=True)
    projeto = models.CharField(max_length=100)
    id_financiador = models.ForeignKey(Financiadores, on_delete=models.CASCADE)
    id_area_tecnologica = models.ForeignKey(AreasTecnologicas, on_delete=models.CASCADE)
    coordenador = models.CharField(max_length=100)
    ativo = models.BooleanField()
    inicio_vigencia = models.DateField()
    fim_vigencia = models.DateField()
    valor = models.FloatField(2)
    qtd_membros = models.IntegerField()
    equipe = models.ManyToManyField(Colaboradores)

    def __str__(self):
        return self.projeto