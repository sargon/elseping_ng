"""elseping_ng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from tasks import views as task

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ball$',task.task_next,name="task-ball-next"),
    url(r'^task/list$', task.task_next,name="task-list"),
    url(r'^task/next$',task.task_next,name="task-next"),
    url(r'^task/(?P<task_id>[0-9]+)/$',task.task_view,name="task-view"),
    url(r'^task/(?P<task_id>[0-9]+)/noneed$', task.task_noneed, name="task-noneed"),
    url(r'^task/(?P<task_id>[0-9]+)/complete$',task.task_complete,name="task-complete"),
    url(r'^$',task.index)
]
