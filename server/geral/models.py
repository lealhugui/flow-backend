# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import geral.constants as c

class Empresa(models.Model):
    denominacao = models.CharField(max_length=250)


class Estabelecimento(models.Model):
    empresa = models.ForeignKey(Empresa)
    razao_social = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=14)

    
class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    tipo = models.IntegerField(choices=c.TIPO_DE_PESSOA, default=c.PESSOA_FISICA)


class PerfilPessoa(models.Model):
    
    class Meta:
        unique_together = (
            ('pessoa', 'perfil')
        )
    
    pessoa = models.ForeignKey(Pessoa)
    perfil = models.IntegerField(choices=c.PERFIS_DE_PESSOA)
    