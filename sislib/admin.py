'''
Created on 03/09/2013

@author: Debora Azevedo
'''
from django.contrib import admin
from sislib.models import Emprestimo, Livro, Usuario

admin.site.register(Emprestimo)
admin.site.register(Livro)
admin.site.register(Usuario)