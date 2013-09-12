# -*- coding: utf-8 -*-
# Create your views here.

from sislib.models import Livro

from django.http import HttpResponse

def f1 (request):
    return HttpResponse('Função 1.')

def f2 (request):
    return HttpResponse('Função 2.')


def indice (request):
    saida = ''
    for l in Livro.objects.all().order_by('titulo'):
        saida += '<br>' + l.titulo + ': ' + l.subtitulo + ' - ' + l.autor
    return HttpResponse(saida)

def mostra_livros(request):
    saida = ['<ul>']
    for l in Livro.objects.all():
        saida.append('<li> {}: {} - {} </li>'.format(l.titulo, l.subtitulo, l.autor))
    saida.append('</ul>')

    return HttpResponse('\n'.join(saida))