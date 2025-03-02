def format_all_projects(instance):
    return {
        'id_projeto': instance.id_projeto,
        'projeto': instance.projeto,
        'id_financiador': instance.id_financiador.id_financiador,
        'financiador': instance.id_financiador.financiador,
        'id_area_tecnologica': instance.id_area_tecnologica.id_area_tecnologica,
        'area_tecnologica': instance.id_area_tecnologica.area_tecnologica,
        'coordenador': instance.coordenador,
        'ativo': instance.ativo,
        'inicio_vigencia': instance.inicio_vigencia,
        'fim_vigencia': instance.fim_vigencia,
        'valor': instance.valor,
        'qtd_membros': instance.qtd_membros,
        'equipe': [
            {'id_colaborador': colaborador.id_colaborador, 'nome': colaborador.nome}
            for colaborador in instance.equipe.all()
        ],
    }
    
def format_team_project(instance):
    return {
        'equipe': [
            {
                'id_colaborador': colaborador.id_colaborador,
                'nome': colaborador.nome,
                'cpf': colaborador.cpf,
                'dt_nascimento': colaborador.dt_nascimento
            }
            for colaborador in instance.equipe.all()
        ]
    }
