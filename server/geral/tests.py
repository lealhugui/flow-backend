# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.test import TestCase, Client

from .models import Pessoa, Tenant
import geral.constants as c

# Create your tests here.
class APIPessoaTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        t = Tenant.objects.create(name="Test")
        
    def get_pessoa(self):
        resp = self.c.get('/pessoa/')
        self.assertEqual(resp.status_code, 200)
        result = resp.json()
        self.assertEqual(len(result), len(Pessoa.objects.all()))
    
    def post_pessoa(self):
        data = {'nome': 'Foo', 'tipo': 1, 'tenant': 1}
        resp = self.c.post('/pessoa/', data)
        self.assertEqual(resp.status_code, 201)
        self.assertIs(type(resp.json()), dict)
        
    def test_get_pessoa(self):
        self.get_pessoa()
        
    def test_post_pessoa(self):
        self.post_pessoa()
        
    def test_get_and_post(self):
        self.post_pessoa()
        self.get_pessoa()
        
        
    