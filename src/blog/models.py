from django.db import models
from django.core.exceptions import ValidationError
import re


def verify_cpf(value):
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
        raise ValidationError('CPF deve estar no formato correto: XXX.XXX.XXX-XX')


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(
        max_length=14, unique=True, validators=[verify_cpf], error_messages={"unique": "CPF ja cadastrado"}
    )

    def __str__(self):
        return self.nome
