from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    # Conecta o comentário a um Post. Se o post for deletado, os comentários dele somem junto (models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    # Conecta ao usuário que comentou
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} no post {self.post.titulo}"
        return self.titulo