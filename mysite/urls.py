"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls', namespace='polls')),
    path('admin/', admin.site.urls),
]

# 동작원리
# ex) 127.0.0/polls/ 에서 진입했다고 가정
#  1. polls를 20행의 path가 잡아내고 polls.urls를 연결함
#  2. 'urlpatterns = [path('', views.index, name='index'),]' 에서 views.index로 연결을 시켜줌
#  3. views 내부의 index함수에서 'hello world' 를 클라이언트에게 전달