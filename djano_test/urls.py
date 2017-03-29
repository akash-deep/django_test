"""djano_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from article import views
from article import urls
from article.views import HelloTemplate
from djano_test import views

admin.autodiscover()

#from article import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^hello/', views.hello),
    #url(r'^hello_template/', views.hello_template),
    #url(r'^class_tem/', HelloTemplate.as_view()),
    #url(r'^hello_t/', views.hello_simple_template),
    url(r'^articles/', include('article.urls')),
    url(r'^accounts/login/$',views.login),
    url(r'^accounts/auth/$',views.auth_view),
    url(r'^accounts/logout/$',views.logout),
    url(r'^accounts/loggedin/$',views.loggedin),
    url(r'^accounts/invalid/$',views.invalid_login),
    url(r'^accounts/register/$',views.register_user),
    url(r'^accounts/register_success/$',views.register_success),
]
