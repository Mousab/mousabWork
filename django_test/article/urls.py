from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    (r'^all/$', 'article.views.articles'),
    (r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
    (r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),

)