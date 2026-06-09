from django.contrib import admin

# importar nossos models

from .models import Aluno, Turma

admin.site.register(Aluno)
admin.site.register(Turma)