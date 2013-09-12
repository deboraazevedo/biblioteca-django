# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Livro (models.Model):
    
    def __unicode__(self):
        return self.titulo
            
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50, blank=True)
    editora = models.CharField(max_length=50)
    edicao = models.IntegerField(max_length=2)
    autor = models.ManyToManyField(Autor)


class Autor():
    def __unicode__(self):
        return self.nome
       
    autor = models.CharField(max_length=50)
    

class Usuario (models.Model):
    
    def __unicode__(self):
        return self.nome
        
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField()
    datanasc = models.DateField()
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)



    

class Emprestimo(models.Model):
    
    def __unicode__(self):
        return 'Empréstimo' + str(id)
    
    usuario = models.ForeignKey(Usuario)
    material = models.ForeignKey(Livro)
    data = models.DateField()
    prazo = models.IntegerField(default=7)
    