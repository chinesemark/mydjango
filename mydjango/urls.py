"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from learn import views as learn_views  # new



app_name = 'learn'

urlpatterns = [
    #path('', learn_views.index),
    #path('learn', include('mydjango.urls')),# new
    path('root/', admin.site.urls),
# ex: /polls/
        path('', learn_views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', learn_views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', learn_views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', learn_views.vote, name='vote'),
]

