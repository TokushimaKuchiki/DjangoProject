"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from simple_forum_Django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('question/<int:question_id>/', views.question, name = 'question'),
    path('ask/', views.new_question, name = 'ask'),
    path('hot/', views.hot_question, name = 'hot_question'),
    path('tag/', views.tag_question, name = 'tag_question'),
    path('settings/', views.settings, name = 'settings'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
]
