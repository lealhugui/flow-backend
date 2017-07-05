# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Tenant, Empresa, Estabelecimento, Pessoa, PerfilPessoa

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = '__all__'


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class PerfilPessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilPessoa
        fields = '__all__'  