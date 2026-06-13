from django.contrib import admin

# importar nossos models

from .models import Aluno, Turma, Curso, Campus

admin.site.register(Curso)
admin.site.register(Aluno)

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'periodo', 'campus')

