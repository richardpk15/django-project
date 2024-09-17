from django.test import TestCase
from src.blog.models import Pessoa


# create a simple model test for Pessoa
class PessoaTestCase(TestCase):
    def test_create_pessoa(self):
        pessoa = Pessoa.objects.create(
            nome='John Doe',
            idade=30,
            cpf='123.456.789-00'
        )
        self.assertEqual(pessoa.nome, 'John Doe')
        self.assertEqual(pessoa.idade, 30)
        self.assertEqual(pessoa.cpf, '123.456.789-00')
