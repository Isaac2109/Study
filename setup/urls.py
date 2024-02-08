from django.contrib import admin
from django.urls import path

from study.views import home, test, result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('test/', test, name='test'),
    path('result/', result, name='result')
]
