# Generated by Django 5.1.6 on 2025-03-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_colaboradores_cpf_alter_projetos_qtd_membros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='qtd_membros',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
