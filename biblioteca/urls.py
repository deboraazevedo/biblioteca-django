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
    
    url(r'^123/', 'sislib.views.f1'),
    url(r'^456/', 'sislib.views.f2'),
    url(r'^livros/', 'sislib.views.mostra_livros'),
    #url(r'^$', 'sislib.views.mostra_livros'),
    #url(r'^$', 'sislib.views.indice'),
)
