"""pwnit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from pwnit.schema import schema

from frontend import views as frontend_views
from blockchain import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api$', views.Api.as_view()),
    url(r'^login/$', frontend_views.login, name='login'),
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
