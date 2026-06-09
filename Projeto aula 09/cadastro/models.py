from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    periodo = models.CharField(max_length=20, choices=[
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite'),
    ], default='MANHA')

    def __str__(self):
        return f"{self.nome} ({self.get_periodo_display()})"


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    # Adicionando a relação com a Turma (Se a turma for deletada, o aluno fica com a turma em branco)
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, blank=True, related_name='alunos')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome