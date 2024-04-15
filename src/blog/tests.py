from django.test import TestCase
from src.blog.models import Pessoa


# create a simple model test for Pessoa
class TestModel(TestCase):
    def setUp(self):
        self.pessoa = Pessoa.objects.create(
            nome='John Doe',
            idade=30,
            cpf='123.456.789-00'
        )

    def test_create_pessoa(self):
        self.assertEqual(self.pessoa.nome, 'John Doe')
        self.assertEqual(self.pessoa.idade, 30)
        self.assertEqual(self.pessoa.cpf, '123.456.789-00')
