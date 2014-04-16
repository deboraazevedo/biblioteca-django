from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblioteca.views.home', name='home'),
    # url(r'^biblioteca/', include('biblioteca.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^123/', 'sislib.views.indice'),
    url(r'^456/', 'sislib.views.f2'),
    
    url(r'^livro/$', 'sislib.views.mostra_livros'),
    url(r'^usuario/$', 'sislib.views.mostra_usuarios'),
    url(r'^emprestimo/$', 'sislib.views.mostra_emprestimos'),
    url(r'^autor/$', 'sislib.views.mostra_autores'),
    
    url(r'^livro/(?P<id>\d+)/$', 'sislib.views.detalhes_livro'),
    url(r'^usuario/(?P<id>\d+)/$', 'sislib.views.detalhes_usuario'),
    url(r'^emprestimo/(?P<id>\d+)/$', 'sislib.views.detalhes_emprestimo'),
    url(r'^autor/(?P<id>\d+)/$', 'sislib.views.detalhes_autor'),

    #url(r'^$', 'sislib.views.mostra_livros'),
    url(r'^/$', 'sislib.views.indice'),
)
