from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sitelinkedin.views.home', name='home'),
    # url(r'^sitelinkedin/', include('sitelinkedin.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^diplodocus/$', 'diplodocus.views.index'),
    url(r'^diplodocus/companie/$', 'diplodocus.views.companie'),
    url(r'^diplodocus/student/$', 'diplodocus.views.student'),
    url(r'^diplodocus/articol', 'diplodocus.views.articol'),
    url(r'^diplodocus/login', 'diplodocus.views.login'),
    #login with linkedin sends data to this method
    url(r'^diplodocus/api_login', 'diplodocus.views.api_login'),
    )