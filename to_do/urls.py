"""to_do URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path

from crud_operations.views import TasksList, TaskOperations

urlpatterns = [
    re_path(r'^list$', TasksList.as_view(), name="todo"),
    re_path(r'^list/(?P<pk>\d+)', TaskOperations.as_view(), name='task_operations'),

    path('admin/', admin.site.urls),
]
