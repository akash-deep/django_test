from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^all/$',views.articles),
    url(r'^get/(?P<article_id>\d+)/$',views.article),
    url(r'^language/(?P<language>[a-z\-]+)/$',views.language),
    url(r'^create/$',views.create),
    url(r'^alu/$',views.alu),
]