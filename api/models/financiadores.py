from django.db import models

class Financiadores(models.Model):
    id_financiador = models.AutoField(primary_key=True)
    financiador = models.CharField(max_length=100)
    
    def __str__(self):
        return self.financiador
