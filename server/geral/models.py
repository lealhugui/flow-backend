# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import geral.constants as c


class Tenant(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=250, null=True)


class TenantModel(models.Model):
    """Mixin para adicionar tenant nas models"""
    tenant = models.ForeignKey(Tenant)
    
    class Meta:
        abstract = True


class Empresa(TenantModel, models.Model):
    denominacao = models.CharField(max_length=250)


class Estabelecimento(TenantModel, models.Model):
    empresa = models.ForeignKey(Empresa)
    razao_social = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=14)

    
class Pessoa(TenantModel, models.Model):
    nome = models.CharField(max_length=250)
    tipo = models.IntegerField(choices=c.TIPO_DE_PESSOA, default=c.PESSOA_FISICA)


class PerfilPessoa(TenantModel, models.Model):
    
    class Meta:
        unique_together = (
            ('pessoa', 'perfil')
        )
    
    pessoa = models.ForeignKey(Pessoa)
    perfil = models.IntegerField(choices=c.PERFIS_DE_PESSOA)
    