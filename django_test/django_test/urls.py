
from  django.conf.urls import patterns,include,url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^hello/', 'article.views.hello'),
    url(r'^articles/', include('article.urls')),
   # url(r'^hello_templet/', 'article.views.hello_templete'),
   # url(r'^hello_templet_simple/', 'article.views.hello_templete_simple'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django_test.views.login'),
    url(r'^accounts/auth/$', 'django_test.views.auth_view'),
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),
)
