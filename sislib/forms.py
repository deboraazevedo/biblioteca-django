# -*- coding: utf-8 -*-

'''
Created on 19/09/2013

@author: Debora Azevedo
'''

from sislib.models import Autor, Livro, Emprestimo, Usuario

from django.forms import ModelForm

class AutorForm(ModelForm):
    class Meta:
        model = Autor

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        
class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario