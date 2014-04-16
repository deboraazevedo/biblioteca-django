# -*- coding: utf-8 -*-
# Create your views here.

from sislib.models import Livro, Emprestimo, Autor, Usuario

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
    saida = ['<h2> Lista de livros registrados</h2>']
    saida.append('<ul>')
    for l in Livro.objects.all():
        saida.append('<li><a href = "{}/"> {} </a></li>'.format(l.id, l.titulo))
    saida.append('</ul>')    
    return HttpResponse('\n'.join(saida))


def mostra_usuarios(request):
    saida = ['<h2> Lista de usuários registrados</h2>']
    saida.append('<ul>')
    for u in Usuario.objects.all():
        saida.append('<li><a href = "{}/"> {} </a></li>'.format(u.id, u.nome))
    saida.append('</ul>')    
    return HttpResponse('\n'.join(saida))

def mostra_autores(request):
    saida = ['<h2> Lista de autores registrados</h2>']
    saida.append('<ul>')
    for a in Autor.objects.all():
        saida.append('<li><a href = "{}/"> {} </a></li>'.format(a.id, a.nome))
    saida.append('</ul>')    
    return HttpResponse('\n'.join(saida))



# def mostra_autores(request, id, nome):
#     saida = ['<h2> Lista de autores registrados</h2>']
#     saida.append('<ul>')
#     for a in Autor.objects.all():
#         saida.append('<li><a href = "{}/" {} </a></li>'.format(a.id, a.nome))
# 
#     return HttpResponse('\n'.join(saida))


def mostra_emprestimos(request):
    saida = ['<h2> Lista de empréstimos registrados</h2>']
    saida.append('<ul>')
    for e in Emprestimo.objects.all():
        saida.append('<li><a href = "{}/"> {} </a></li>'.format(e.id, e.usuario))
    saida.append('</ul>')    
    return HttpResponse('\n'.join(saida))




def detalhes_livro(request, id):
    ident = int(id)
    resultado = Livro.objects.filter(id = ident)
    if len(resultado) == 0:
        return HttpResponse('Livro de ID {} não cadastrado.'.format(id))
    else:
        
        l = resultado[0]
        
        modelo_pagina = '''
        <!DOCTYPE html>
        <html>
            <head>
                <title> Detalhes do {titulo} </title>
            </head>
            
            <body>
                <h2 align="center"> Detalhes do {titulo} </h2>
                <p>Título: {titulo}</p>
                <p>Subtítulo: {subtitulo}</p>
                <p>Editora: {editora}</p>
                <p>Edição: {edicao}</p>
            </body>
            </html>

        '''
        return HttpResponse(modelo_pagina.format(titulo=l.titulo, 
                                                 subtitulo=l.subtitulo,  
                                                 editora=l.editora, 
                                                 edicao=l.edicao))
        
        
        
def detalhes_autor(request, id):
    ident = int(id)
    resultado = Autor.objects.filter(id = ident)
    if len(resultado) == 0:
        return HttpResponse('Autor de  {} não cadastrado.'.format(id))
    else:
        
        a = resultado[0]
        
        modelo_pagina = '''
        <!DOCTYPE html>
        <html>
            <head>
                <title> Detalhes do {nome} </title>
            </head>
            
            <body>
                <h2 align="center"> {nome} </h2>
                <p>Nome do autor: {nome}</p>
            </body>
            </html>

        '''
        return HttpResponse(modelo_pagina.format(nome=a.nome))
    
    
    


def detalhes_usuario(request, id):
    ident = int(id)
    resultado = Usuario.objects.filter(id = ident)
    if len(resultado) == 0:
        return HttpResponse('Usuario de  {} não cadastrado.'.format(id))
    else:
        
        u = resultado[0]
        
        modelo_pagina = '''
        <!DOCTYPE html>
        <html>
            <head>
                <title> Detalhes do usuário {nome} </title>
            </head>
            
            <body>
                <h2 align="center"> {nome} </h2>
                <p>Nome : {nome}</p>
        <p>Matricula : {matricula}</p>
        <p>Data de nascimento : {datanasc}</p>
        <p>RG : {rg}</p>
        <p>CPF : {cpf}</p>
        <p>Email : {email}</p>
        <p>Telefone : {telefone}</p>
        <p>Endereço : {endereco}</p>
        <p>Cidade : {cidade}</p>
        <p>Estado : {estado}</p>
            </body>
            </html>

        '''
        return HttpResponse(modelo_pagina.format(nome=u.nome,
                        matricula=u.matricula,
                        datanasc=u.datanasc,
                        rg=u.rg,
                        cpf=u.cpf,
                        email=u.email,
                        telefone=u.telefone,
                        endereco=u.endereco,
                        cidade=u.cidade,
                        estado=u.estado))




def detalhes_emprestimo(request, id):
    ident = int(id)
    resultado = Emprestimo.objects.filter(id = ident)
    if len(resultado) == 0:
        return HttpResponse('Empréstimo de  {} não cadastrado.'.format(id))
    else:
        
        e = resultado[0]
        
        modelo_pagina = '''
        <!DOCTYPE html>
        <html>
            <head>
                <title> Detalhes do empreśtimo {id} </title>
            </head>
            
            <body>
                <h2 align="center"> Empréstimo {id} </h2>
                <p>Usuário : {usuario}</p>
        <p>Material : {material}</p>
        <p>Data : {data}</p>
        
        <p>Prazo : {prazo}</p>
            </body>
            </html>

        '''
        return HttpResponse(modelo_pagina.format(id=e.id,
                                            usuario=e.usuario,
                                            material=e.material,
                                            data=e.data,
                                            prazo=e.prazo))    