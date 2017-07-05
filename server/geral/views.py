# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

import geral.models as m
import geral.serializers as g_s


class TenantView(viewsets.ModelViewSet):
    queryset = m.Tenant.objects.all()
    serializer_class = g_s.TenantSerializer
    
class EmpresaView(viewsets.ModelViewSet):
    queryset = m.Empresa.objects.all()
    serializer_class = g_s.EmpresaSerializer
    
class EstabelecimentoView(viewsets.ModelViewSet):
    queryset = m.Estabelecimento.objects.all()
    serializer_class = g_s.EstabelecimentoSerializer
    
class PessoaView(viewsets.ModelViewSet):
    queryset = m.Pessoa.objects.all()
    serializer_class = g_s.PessoaSerializer
    
class PerfilPessoaView(viewsets.ModelViewSet):
    queryset = m.PerfilPessoa.objects.all()
    serializer_class = g_s.PerfilPessoaSerializer